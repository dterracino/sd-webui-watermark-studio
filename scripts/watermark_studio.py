"""
Watermark Studio Extension for AUTOMATIC1111 Stable Diffusion WebUI

This extension provides watermarking functionality for generated images.
It can add controls to the Gradio UI, interact with UI components, and receive events.
"""

from typing import List, Tuple
import gradio as gr
from modules import scripts, script_callbacks, shared
from modules.processing import StableDiffusionProcessing, Processed
from modules.shared import opts
import os

# Import font loading functionality
try:
    from scripts.load_fonts import load_fonts
    FONTS_AVAILABLE = True
except Exception as e:
    print(f"[Watermark Studio] Error loading fonts module: {e}")
    FONTS_AVAILABLE = False


class WatermarkStudioScript(scripts.Script):
    """Main script class for the Watermark Studio extension."""

    def __init__(self):
        self.enabled = False
        self.watermark_text = ""
        self.watermark_opacity = 0.5
        self.watermark_position = "bottom-right"
        self.auto_watermark = False
        self.watermark_font = "arial"  # Default font
        
        # Load available fonts
        self.available_fonts = {}
        if FONTS_AVAILABLE:
            try:
                self.available_fonts = load_fonts()
                if not self.available_fonts:
                    print("[Watermark Studio] No fonts found in assets/fonts directory")
            except Exception as e:
                print(f"[Watermark Studio] Error loading fonts: {e}")
        
    def title(self):
        """Return the title of this script."""
        return "Watermark Studio"
    
    def show(self, is_img2img):
        """Show this script in both txt2img and img2img tabs."""
        return scripts.AlwaysVisible
    
    def ui(self, is_img2img):
        """Create the UI components for this extension."""
        
        tab_name = "img2img" if is_img2img else "txt2img"
        
        with gr.Group():
            with gr.Accordion(f"Watermark Studio ({tab_name})", open=False):
                
                # Enable/disable watermark
                enabled = gr.Checkbox(
                    label="Enable Watermarking",
                    value=self.enabled,
                    elem_id=f"watermark_studio_enabled_{tab_name}"
                )
                
                with gr.Row():
                    # Watermark text input
                    watermark_text = gr.Textbox(
                        label="Watermark Text",
                        value=self.watermark_text,
                        placeholder="Enter watermark text (e.g., your name or website)",
                        elem_id=f"watermark_studio_text_{tab_name}"
                    )
                
                with gr.Row():
                    # Font selection dropdown
                    if self.available_fonts:
                        font_choices = list(self.available_fonts.keys())
                        default_font = self.watermark_font if self.watermark_font in font_choices else font_choices[0]
                    else:
                        font_choices = ["No fonts available"]
                        default_font = "No fonts available"
                    
                    font_selection = gr.Dropdown(
                        choices=font_choices,
                        value=default_font,
                        label=f"Watermark Font ({len(self.available_fonts)} fonts available)" if self.available_fonts else "Watermark Font (No fonts loaded)",
                        elem_id=f"watermark_studio_font_{tab_name}",
                        interactive=bool(self.available_fonts)
                    )
                
                with gr.Row():
                    # Opacity slider
                    opacity = gr.Slider(
                        minimum=0.1,
                        maximum=1.0,
                        step=0.1,
                        value=self.watermark_opacity,
                        label="Watermark Opacity",
                        elem_id=f"watermark_studio_opacity_{tab_name}"
                    )
                    
                    # Position dropdown
                    position = gr.Dropdown(
                        choices=[
                            "top-left",
                            "top-center", 
                            "top-right",
                            "center-left",
                            "center",
                            "center-right",
                            "bottom-left",
                            "bottom-center",
                            "bottom-right"
                        ],
                        value=self.watermark_position,
                        label="Watermark Position",
                        elem_id=f"watermark_studio_position_{tab_name}"
                    )
                
                with gr.Row():
                    # Auto-watermark checkbox
                    auto_watermark = gr.Checkbox(
                        label="Auto-apply watermark to all generated images",
                        value=self.auto_watermark,
                        elem_id=f"watermark_studio_auto_{tab_name}"
                    )
                
                with gr.Row():
                    # Test button for immediate feedback
                    test_button = gr.Button(
                        "Test Watermark Settings",
                        elem_id=f"watermark_studio_test_{tab_name}"
                    )
                    
                    # Status text
                    status_text = gr.HTML(
                        value="<span style='color: gray;'>Ready</span>",
                        elem_id=f"watermark_studio_status_{tab_name}"
                    )
                
                # Event handlers for UI interaction
                enabled.change(
                    fn=self._on_enabled_change,
                    inputs=[enabled],
                    outputs=[status_text]
                )
                
                watermark_text.change(
                    fn=self._on_text_change,
                    inputs=[watermark_text],
                    outputs=[status_text]
                )
                
                font_selection.change(
                    fn=self._on_font_change,
                    inputs=[font_selection],
                    outputs=[status_text]
                )
                
                test_button.click(
                    fn=self._test_watermark,
                    inputs=[enabled, watermark_text, font_selection, opacity, position, auto_watermark],
                    outputs=[status_text]
                )
        
        return [enabled, watermark_text, font_selection, opacity, position, auto_watermark]
    
    def _on_enabled_change(self, enabled):
        """Handle enable/disable events."""
        self.enabled = enabled
        status = "<span style='color: green;'>Enabled</span>" if enabled else "<span style='color: gray;'>Disabled</span>"
        return status
    
    def _on_text_change(self, text):
        """Handle watermark text changes."""
        self.watermark_text = text
        if text:
            return "<span style='color: blue;'>Text updated</span>"
        else:
            return "<span style='color: orange;'>No watermark text</span>"
    
    def _on_font_change(self, font_name):
        """Handle font selection changes."""
        self.watermark_font = font_name
        if font_name and font_name != "No fonts available":
            return f"<span style='color: green;'>Font: {font_name}</span>"
        else:
            return "<span style='color: orange;'>No font selected</span>"
    
    def _test_watermark(self, enabled, text, font, opacity, position, auto_watermark):
        """Test watermark settings and provide feedback."""
        self.enabled = enabled
        self.watermark_text = text
        self.watermark_font = font
        self.watermark_opacity = opacity
        self.watermark_position = position
        self.auto_watermark = auto_watermark
        
        if not enabled:
            return "<span style='color: red;'>Watermarking is disabled</span>"
        
        if not text:
            return "<span style='color: red;'>Please enter watermark text</span>"
        
        font_info = f" in {font}" if font and font != "No fonts available" else ""
        status = f"<span style='color: green;'>✓ Ready: '{text}'{font_info} at {position} ({int(opacity*100)}% opacity)</span>"
        if auto_watermark:
            status += "<br><span style='color: blue;'>Auto-watermark is ON</span>"
        
        return status
    
    def before_process(self, p: StableDiffusionProcessing, enabled, watermark_text, font, opacity, position, auto_watermark):
        """Called before image processing starts."""
        if enabled and auto_watermark and watermark_text:
            print(f"[Watermark Studio] Preparing to watermark with: '{watermark_text}' using {font} at {position}")
            # Store watermark settings in the processing object for later use
            p.watermark_studio_settings = {
                'enabled': enabled,
                'text': watermark_text,
                'font': font,
                'opacity': opacity,
                'position': position,
                'auto_watermark': auto_watermark
            }
    
    def postprocess(self, p: StableDiffusionProcessing, res: Processed, enabled, watermark_text, font, opacity, position, auto_watermark):
        """Called after image processing is complete."""
        if enabled and auto_watermark and watermark_text:
            print(f"[Watermark Studio] Image generation complete. Would apply watermark: '{watermark_text}' using {font}")
            # In a real implementation, this is where we would apply the watermark to res.images
            # For now, we just log the event to demonstrate event handling
            
            # Add watermark info to the generation info
            font_info = f" using {font}" if font and font != "No fonts available" else ""
            if res.info:
                res.info += f"\nWatermark: '{watermark_text}'{font_info} at {position} ({int(opacity*100)}% opacity)"


# Register script callbacks for advanced event handling
def on_image_saved(params):
    """Called when an image is saved."""
    print("[Watermark Studio] Image saved event detected")


def on_app_started(demo, app):
    """Called when the web app starts."""
    print("[Watermark Studio] Web app started - extension is ready")


def on_ui_settings():
    """Add extension settings to the Settings tab."""
    shared.opts.add_option("watermark_studio_default_text", shared.OptionInfo(
        "", "Default watermark text", gr.Textbox
    ))
    
    shared.opts.add_option("watermark_studio_default_enabled", shared.OptionInfo(
        False, "Enable watermarking by default", gr.Checkbox
    ))
    
    shared.opts.add_option("watermark_studio_preserve_transparency", shared.OptionInfo(
        True, "Preserve image transparency when watermarking", gr.Checkbox
    ))


# Register callbacks - this enables the extension to receive various events
script_callbacks.on_image_saved(on_image_saved)
script_callbacks.on_app_started(on_app_started) 
script_callbacks.on_ui_settings(on_ui_settings)

print("[Watermark Studio] Extension loaded successfully")