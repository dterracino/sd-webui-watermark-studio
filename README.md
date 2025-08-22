# 🏷️ Watermark Studio Extension for AUTOMATIC1111 Stable Diffusion WebUI

A comprehensive watermarking extension that adds professional watermarking capabilities to your Stable Diffusion WebUI.

## ✨ Features

### 🎯 Core Functionality
- **UI Integration**: Seamlessly adds watermarking controls to both txt2img and img2img tabs
- **Interactive Controls**: Real-time feedback and validation for watermark settings
- **Event Handling**: Automatically responds to image generation events
- **Custom Tab**: Dedicated Watermark Studio tab for advanced watermarking operations

### 🛠️ Watermarking Options
- **Text Watermarks**: Add custom text watermarks to your images
- **Position Control**: Place watermarks at 9 different positions on your images
- **Opacity Control**: Adjust watermark transparency from 10% to 100%
- **Auto-Watermarking**: Automatically apply watermarks to all generated images
- **Batch Processing**: Process multiple images at once (prepared for future implementation)

### 🎨 User Interface
- **Responsive Design**: Works on desktop and mobile devices
- **Keyboard Shortcuts**: Quick access with Ctrl+Shift+W
- **Visual Feedback**: Real-time status updates and validation
- **Tooltips**: Helpful hints for all controls

## 📋 Requirements

- AUTOMATIC1111 Stable Diffusion WebUI
- Python 3.7+
- PIL (Python Imaging Library) - usually included with the WebUI

## 🚀 Installation

1. Clone this repository into your `stable-diffusion-webui/extensions` directory:
```bash
cd stable-diffusion-webui/extensions
git clone https://github.com/dterracino/sd-webui-watermark-studio.git
```

2. Restart your Stable Diffusion WebUI

3. The extension will automatically load and be available in:
   - txt2img tab (in the scripts section)
   - img2img tab (in the scripts section) 
   - Dedicated "Watermark Studio" tab

## 💡 Usage

### Basic Watermarking (txt2img/img2img tabs)

1. Expand the "Watermark Studio" accordion in either tab
2. Check "Enable Watermarking"
3. Enter your watermark text (e.g., "© Your Name" or "yourwebsite.com")
4. Adjust opacity and position as desired
5. Enable "Auto-apply watermark" for automatic watermarking
6. Generate images as normal - watermarks will be applied automatically

### Advanced Features (Watermark Studio Tab)

1. Navigate to the "Watermark Studio" tab
2. Use the "Quick Watermark" section for single image processing
3. Access "Batch Processing" for multiple images
4. Save frequently used settings as templates

## ⚙️ Settings

The extension adds the following settings to the WebUI Settings tab:

- **Default watermark text**: Set a default text that appears automatically
- **Enable watermarking by default**: Start with watermarking enabled
- **Preserve image transparency**: Maintain PNG transparency when watermarking

## 🎹 Keyboard Shortcuts

- **Ctrl+Shift+W**: Toggle watermark studio accordion

## 🔧 Extension Architecture

This extension demonstrates best practices for A1111 WebUI extensions:

### 📁 File Structure
```
sd-webui-watermark-studio/
├── scripts/
│   ├── __init__.py                 # Extension initialization
│   ├── watermark_studio.py         # Main script class
│   ├── watermark_studio_tab.py     # Custom tab implementation
│   └── watermark_utils.py          # Utility functions
├── javascript/
│   └── watermark_studio.js         # Client-side enhancements
├── style.css                       # Custom styling
├── README.md                       # This file
└── LICENSE                         # License file
```

### 🏗️ Extension Components

1. **Script Class** (`watermark_studio.py`):
   - Inherits from `modules.scripts.Script`
   - Implements `ui()` method for Gradio components
   - Handles `before_process()` and `postprocess()` events
   - Provides real-time UI interaction

2. **Custom Tab** (`watermark_studio_tab.py`):
   - Registers with `script_callbacks.on_ui_tabs`
   - Creates dedicated watermarking interface
   - Includes batch processing capabilities
   - Template system for saving/loading settings

3. **Event Handling**:
   - `on_image_saved`: Detects when images are saved
   - `on_app_started`: Initializes when WebUI starts
   - `on_ui_settings`: Adds custom settings options

4. **Client-side Enhancements** (`watermark_studio.js`):
   - Keyboard shortcuts
   - Visual feedback
   - Drag-and-drop functionality
   - Tooltips and user experience improvements

## 🔮 Future Development

This extension is prepared for future enhancements:

- **Image Watermarking**: Logo and image-based watermarks
- **Batch Processing**: Full implementation of multi-image processing
- **Template System**: Save and share watermark configurations
- **Advanced Positioning**: Pixel-perfect watermark placement
- **Watermark Preview**: Real-time preview before application
- **Export Options**: Multiple output formats and quality settings

## 🐛 Troubleshooting

### Extension Not Loading
- Ensure the extension is in the correct directory: `stable-diffusion-webui/extensions/`
- Check the WebUI console for error messages
- Restart the WebUI completely

### UI Not Appearing
- Look for "Watermark Studio" accordion in txt2img/img2img tabs
- Check if the "Watermark Studio" tab appears in the main interface
- Verify JavaScript console for any errors

### Settings Not Saving
- Check WebUI Settings tab for Watermark Studio options
- Ensure you have write permissions in the WebUI directory

## 📄 License

This project is released into the public domain under the Unlicense. See [LICENSE](LICENSE) for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## 📚 Extension Development Reference

This extension serves as a reference implementation for A1111 WebUI extension development, demonstrating:

- ✅ Adding controls to the Gradio UI
- ✅ Interacting with UI controls and receiving user input
- ✅ Receiving events from Gradio (image generation, etc.)
- ✅ Creating custom tabs at the main UI level
- ✅ Event handling and callback registration
- ✅ Settings integration
- ✅ JavaScript enhancements
- ✅ CSS styling
- ✅ Proper extension structure and organization

Perfect for developers looking to create their own A1111 WebUI extensions!