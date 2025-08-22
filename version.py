"""
Version information for Watermark Studio Extension
"""

__version__ = "1.0.0"
__author__ = "Watermark Studio Team"
__email__ = "support@watermarkstudio.dev"
__license__ = "Unlicense"
__copyright__ = "Released into the public domain"

# Version components
VERSION_MAJOR = 1
VERSION_MINOR = 0
VERSION_PATCH = 0
VERSION_BUILD = 0

# Version tuple for programmatic access
VERSION_INFO = (VERSION_MAJOR, VERSION_MINOR, VERSION_PATCH, VERSION_BUILD)

def get_version():
    """Return the version string."""
    return __version__

def get_version_info():
    """Return version information as a dictionary."""
    return {
        "version": __version__,
        "author": __author__,
        "license": __license__,
        "copyright": __copyright__,
        "version_info": VERSION_INFO
    }