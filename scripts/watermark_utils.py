"""
Watermark Studio Utilities

This module contains utility functions for watermarking operations.
Currently provides placeholder/mock implementations to demonstrate the extension structure.
"""

from PIL import Image, ImageDraw, ImageFont, ImageEnhance
from typing import Tuple, Optional
import io


class WatermarkProcessor:
    """Handles watermark processing operations."""
    
    def __init__(self):
        self.default_font_size = 24
        self.default_color = "white"
        self.default_opacity = 0.5
    
    def apply_text_watermark(
        self, 
        image: Image.Image, 
        text: str,
        position: str = "bottom-right",
        opacity: float = 0.5,
        font_size: int = 24,
        color: str = "white"
    ) -> Image.Image:
        """
        Apply a text watermark to an image.
        
        Args:
            image: PIL Image to watermark
            text: Watermark text
            position: Position for watermark (e.g., "bottom-right")
            opacity: Watermark opacity (0.0 to 1.0)
            font_size: Font size for text
            color: Text color
            
        Returns:
            Watermarked PIL Image
        """
        if not image or not text:
            return image
        
        # For now, this is a placeholder that just returns the original image
        # In a real implementation, this would:
        # 1. Create a copy of the image
        # 2. Create a transparent overlay
        # 3. Draw the text with specified parameters
        # 4. Composite the overlay onto the image
        
        print(f"[WatermarkProcessor] Would apply text watermark: '{text}' at {position}")
        return image
    
    def get_text_position(self, image_size: Tuple[int, int], text_size: Tuple[int, int], position: str) -> Tuple[int, int]:
        """
        Calculate the position coordinates for text placement.
        
        Args:
            image_size: (width, height) of the image
            text_size: (width, height) of the text
            position: Position string (e.g., "bottom-right")
            
        Returns:
            (x, y) coordinates for text placement
        """
        img_width, img_height = image_size
        text_width, text_height = text_size
        
        margin = 20  # Margin from edges
        
        position_map = {
            "top-left": (margin, margin),
            "top-center": (img_width // 2 - text_width // 2, margin),
            "top-right": (img_width - text_width - margin, margin),
            "center-left": (margin, img_height // 2 - text_height // 2),
            "center": (img_width // 2 - text_width // 2, img_height // 2 - text_height // 2),
            "center-right": (img_width - text_width - margin, img_height // 2 - text_height // 2),
            "bottom-left": (margin, img_height - text_height - margin),
            "bottom-center": (img_width // 2 - text_width // 2, img_height - text_height - margin),
            "bottom-right": (img_width - text_width - margin, img_height - text_height - margin),
        }
        
        return position_map.get(position, position_map["bottom-right"])
    
    def validate_watermark_settings(self, text: str, opacity: float, position: str) -> Tuple[bool, str]:
        """
        Validate watermark settings.
        
        Args:
            text: Watermark text
            opacity: Opacity value
            position: Position string
            
        Returns:
            (is_valid, error_message)
        """
        if not text or not text.strip():
            return False, "Watermark text cannot be empty"
        
        if not (0.0 <= opacity <= 1.0):
            return False, "Opacity must be between 0.0 and 1.0"
        
        valid_positions = [
            "top-left", "top-center", "top-right",
            "center-left", "center", "center-right", 
            "bottom-left", "bottom-center", "bottom-right"
        ]
        
        if position not in valid_positions:
            return False, f"Position must be one of: {', '.join(valid_positions)}"
        
        return True, ""
    
    def batch_process(self, images: list, watermark_settings: dict) -> list:
        """
        Apply watermark to multiple images.
        
        Args:
            images: List of PIL Images
            watermark_settings: Dictionary containing watermark parameters
            
        Returns:
            List of watermarked images
        """
        processed_images = []
        
        for image in images:
            try:
                watermarked = self.apply_text_watermark(
                    image,
                    watermark_settings.get('text', ''),
                    watermark_settings.get('position', 'bottom-right'),
                    watermark_settings.get('opacity', 0.5),
                    watermark_settings.get('font_size', 24),
                    watermark_settings.get('color', 'white')
                )
                processed_images.append(watermarked)
                print(f"[WatermarkProcessor] Processed image {len(processed_images)}")
            except Exception as e:
                print(f"[WatermarkProcessor] Error processing image: {e}")
                processed_images.append(image)  # Return original on error
        
        return processed_images


class WatermarkTemplate:
    """Handles watermark template operations."""
    
    def __init__(self):
        self.templates = {}
    
    def save_template(self, name: str, settings: dict) -> bool:
        """Save a watermark template."""
        try:
            self.templates[name] = settings.copy()
            print(f"[WatermarkTemplate] Template '{name}' saved")
            return True
        except Exception as e:
            print(f"[WatermarkTemplate] Error saving template: {e}")
            return False
    
    def load_template(self, name: str) -> Optional[dict]:
        """Load a watermark template."""
        return self.templates.get(name)
    
    def list_templates(self) -> list:
        """Get list of template names."""
        return list(self.templates.keys())
    
    def delete_template(self, name: str) -> bool:
        """Delete a watermark template."""
        if name in self.templates:
            del self.templates[name]
            print(f"[WatermarkTemplate] Template '{name}' deleted")
            return True
        return False


# Global instances
watermark_processor = WatermarkProcessor()
watermark_template = WatermarkTemplate()


def create_default_templates():
    """Create some default watermark templates."""
    default_templates = {
        "Simple Text": {
            "text": "© Your Name",
            "position": "bottom-right",
            "opacity": 0.7,
            "font_size": 24,
            "color": "white"
        },
        "Website URL": {
            "text": "yourwebsite.com",
            "position": "bottom-center",
            "opacity": 0.5,
            "font_size": 18,
            "color": "gray"
        },
        "Artist Signature": {
            "text": "Artist Name",
            "position": "bottom-left", 
            "opacity": 0.8,
            "font_size": 20,
            "color": "black"
        }
    }
    
    for name, settings in default_templates.items():
        watermark_template.save_template(name, settings)


# Initialize default templates
create_default_templates()

print("[Watermark Studio] Utilities module loaded")