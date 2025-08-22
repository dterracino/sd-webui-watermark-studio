"""
Preload script for Watermark Studio Extension

This script is loaded very early in the AUTOMATIC1111 WebUI startup process,
before most other modules. This allows for early setup of the extension.

Place this file in the scripts/ directory for it to be picked up by the WebUI.
"""

import os
import sys
from pathlib import Path

def setup_extension_paths():
    """Setup paths for the extension"""
    # Get the extension root directory
    script_dir = Path(__file__).parent
    extension_dir = script_dir.parent
    
    # Add extension directory to Python path
    if str(extension_dir) not in sys.path:
        sys.path.insert(0, str(extension_dir))
    
    # Set environment variable for extension root
    os.environ["WATERMARK_STUDIO_EXTENSION_ROOT"] = str(extension_dir)

def early_initialization():
    """Perform early initialization tasks"""
    print("[Watermark Studio] Scripts preload: Early initialization started")
    
    # Setup paths
    setup_extension_paths()
    
    # Create necessary directories early
    extension_dir = Path(os.environ.get("WATERMARK_STUDIO_EXTENSION_ROOT", Path(__file__).parent.parent))
    
    dirs_to_create = [
        extension_dir / "temp",
        extension_dir / "cache",
        extension_dir / "templates", 
        extension_dir / "assets"
    ]
    
    for directory in dirs_to_create:
        directory.mkdir(exist_ok=True)
    
    print("[Watermark Studio] Scripts preload: Initialization completed")

# Execute early initialization
try:
    early_initialization()
except Exception as e:
    print(f"[Watermark Studio] Scripts preload error: {e}")