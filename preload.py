"""
Preload module for Watermark Studio Extension

This module is loaded early in the AUTOMATIC1111 WebUI startup process,
before other modules are initialized. Use this for early setup that needs
to happen before the main extension loads.
"""

import os
import sys
from pathlib import Path

# Add the extension directory to Python path if needed
extension_dir = Path(__file__).parent
if str(extension_dir) not in sys.path:
    sys.path.append(str(extension_dir))

def initialize_extension():
    """Early initialization for the extension"""
    
    # Set up logging
    print("[Watermark Studio] Preload: Extension initializing...")
    
    # Create temporary directories if needed
    temp_dir = extension_dir / "temp"
    cache_dir = extension_dir / "cache"
    
    temp_dir.mkdir(exist_ok=True)
    cache_dir.mkdir(exist_ok=True)
    
    # Set environment variables if needed
    os.environ["WATERMARK_STUDIO_ROOT"] = str(extension_dir)
    
    print("[Watermark Studio] Preload: Early initialization completed")

def setup_paths():
    """Setup additional paths for the extension"""
    
    # Add scripts directory to path for better imports
    scripts_dir = extension_dir / "scripts"
    if str(scripts_dir) not in sys.path:
        sys.path.insert(0, str(scripts_dir))

# Run preload initialization
try:
    initialize_extension()
    setup_paths()
except Exception as e:
    print(f"[Watermark Studio] Preload error: {e}")