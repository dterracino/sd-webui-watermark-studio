"""
Watermark Studio Extension Initialization

This module ensures all components of the Watermark Studio extension are properly loaded.
"""

# Import all extension components to ensure they are loaded
try:
    from scripts.watermark_studio import WatermarkStudioScript
    from scripts.watermark_studio_tab import watermark_studio_tab
    from scripts.watermark_utils import watermark_processor, watermark_template
    
    print("[Watermark Studio] All components loaded successfully")
    print("[Watermark Studio] - Main script: ✓")
    print("[Watermark Studio] - Custom tab: ✓") 
    print("[Watermark Studio] - Utilities: ✓")
    
except ImportError as e:
    print(f"[Watermark Studio] Error loading components: {e}")