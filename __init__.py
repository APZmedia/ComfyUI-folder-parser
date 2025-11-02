"""
@author: Pablo Apiolazza
@title: ComfyUI Folder Parser
@nickname: ComfyUI Folder Parser
@description: A ComfyUI custom node for parsing and filtering files from a folder with sorting capabilities.
"""

import os
import sys
import traceback
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

print("=" * 60)
print("ComfyUI Folder Parser - Starting initialization...")
print("=" * 60)

# Get the current directory path for relative imports
current_dir = os.path.dirname(os.path.realpath(__file__))
print(f"[Folder Parser] Current directory: {current_dir}")

# Importing custom nodes
APZFolderParser = None
try:
    print("[Folder Parser] Attempting to import APZFolderParser from .nodes.apzFolderParser...")
    from .nodes.apzFolderParser import APZFolderParser
    print(f"[Folder Parser] Successfully imported APZFolderParser: {APZFolderParser}")
    print(f"[Folder Parser] APZFolderParser type: {type(APZFolderParser)}")
    logger.info("Successfully imported APZFolderParser node.")
except Exception as e:
    print(f"[Folder Parser] ERROR: Failed to import APZFolderParser node: {e}")
    logger.error("Failed to import APZFolderParser node.", exc_info=True)
    traceback.print_exc()

# Build node mappings
print("\n[Folder Parser] Building NODE_CLASS_MAPPINGS...")
NODE_CLASS_MAPPINGS = {}
if APZFolderParser is not None:
    NODE_CLASS_MAPPINGS["APZFolderParser"] = APZFolderParser
    print(f"[Folder Parser] Added APZFolderParser to NODE_CLASS_MAPPINGS")
    print(f"[Folder Parser] NODE_CLASS_MAPPINGS: {list(NODE_CLASS_MAPPINGS.keys())}")
else:
    print("[Folder Parser] WARNING: APZFolderParser is None, not adding to mappings!")

print("\n[Folder Parser] Building NODE_DISPLAY_NAME_MAPPINGS...")
NODE_DISPLAY_NAME_MAPPINGS = {}
if "APZFolderParser" in NODE_CLASS_MAPPINGS:
    NODE_DISPLAY_NAME_MAPPINGS["APZFolderParser"] = "APZmedia Folder Parser"
    print(f"[Folder Parser] Added display name mapping")
    print(f"[Folder Parser] NODE_DISPLAY_NAME_MAPPINGS: {NODE_DISPLAY_NAME_MAPPINGS}")

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

print("\n[Folder Parser] Final registration:")
print(f"  NODE_CLASS_MAPPINGS keys: {list(NODE_CLASS_MAPPINGS.keys())}")
print(f"  NODE_DISPLAY_NAME_MAPPINGS: {NODE_DISPLAY_NAME_MAPPINGS}")
print(f"  __all__: {__all__}")

print("=" * 60)
print("ComfyUI Folder Parser - Initialization complete")
print("=" * 60)

logger.info("ComfyUI Folder Parser extension has been loaded successfully.")
