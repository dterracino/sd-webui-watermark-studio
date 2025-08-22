#!/usr/bin/env python3
"""
Installation script for Watermark Studio Extension

This script handles automatic installation of dependencies when the extension is loaded.
It's called by AUTOMATIC1111 WebUI during extension initialization.
"""

import os
import subprocess
import sys
from pathlib import Path

def install_requirements():
    """Install Python packages listed in requirements.txt"""
    requirements_file = Path(__file__).parent / "requirements.txt"
    
    if requirements_file.exists():
        print(f"[Watermark Studio] Installing dependencies from {requirements_file}")
        try:
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", "-r", str(requirements_file)
            ])
            print("[Watermark Studio] Dependencies installed successfully")
        except subprocess.CalledProcessError as e:
            print(f"[Watermark Studio] Error installing dependencies: {e}")
            return False
    else:
        print("[Watermark Studio] No requirements.txt found, skipping dependency installation")
    
    return True

def create_directories():
    """Create necessary directories for the extension"""
    base_dir = Path(__file__).parent
    
    # Create directories that might be needed
    directories = [
        base_dir / "temp",
        base_dir / "cache", 
        base_dir / "templates",
        base_dir / "assets"
    ]
    
    for directory in directories:
        directory.mkdir(exist_ok=True)
        
    print("[Watermark Studio] Extension directories created")

def main():
    """Main installation function"""
    print("[Watermark Studio] Starting installation...")
    
    try:
        # Install Python dependencies
        if not install_requirements():
            return False
            
        # Create necessary directories
        create_directories()
        
        print("[Watermark Studio] Installation completed successfully")
        return True
        
    except Exception as e:
        print(f"[Watermark Studio] Installation failed: {e}")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)