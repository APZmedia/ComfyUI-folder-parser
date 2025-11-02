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

# Force stdout to be unbuffered
sys.stdout.flush()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

print("=" * 60, flush=True)
print("ComfyUI Folder Parser - Starting initialization...", flush=True)
print("=" * 60, flush=True)

# Get the current directory path for relative imports
current_dir = os.path.dirname(os.path.realpath(__file__))
print(f"[Folder Parser] Current directory: {current_dir}", flush=True)
print(f"[Folder Parser] __file__: {__file__}", flush=True)

# Importing custom nodes
APZFolderParser = None
try:
    print("[Folder Parser] Attempting to import APZFolderParser from .nodes.apzFolderParser...", flush=True)
    from .nodes.apzFolderParser import APZFolderParser
    print(f"[Folder Parser] Successfully imported APZFolderParser: {APZFolderParser}", flush=True)
    print(f"[Folder Parser] APZFolderParser type: {type(APZFolderParser)}", flush=True)
    
    # Verify node has required attributes
    if hasattr(APZFolderParser, 'INPUT_TYPES'):
        print(f"[Folder Parser] INPUT_TYPES exists: {callable(APZFolderParser.INPUT_TYPES)}", flush=True)
    if hasattr(APZFolderParser, 'RETURN_TYPES'):
        print(f"[Folder Parser] RETURN_TYPES: {APZFolderParser.RETURN_TYPES}", flush=True)
    if hasattr(APZFolderParser, 'FUNCTION'):
        print(f"[Folder Parser] FUNCTION: {APZFolderParser.FUNCTION}", flush=True)
    if hasattr(APZFolderParser, 'CATEGORY'):
        print(f"[Folder Parser] CATEGORY: {APZFolderParser.CATEGORY}", flush=True)
    
    logger.info("Successfully imported APZFolderParser node.")
except Exception as e:
    print(f"[Folder Parser] ERROR: Failed to import APZFolderParser node: {e}", flush=True)
    logger.error("Failed to import APZFolderParser node.", exc_info=True)
    traceback.print_exc()

# Build node mappings
print("\n[Folder Parser] Building NODE_CLASS_MAPPINGS...", flush=True)
NODE_CLASS_MAPPINGS = {}
if APZFolderParser is not None:
    NODE_CLASS_MAPPINGS["APZFolderParser"] = APZFolderParser
    print(f"[Folder Parser] Added APZFolderParser to NODE_CLASS_MAPPINGS", flush=True)
    print(f"[Folder Parser] NODE_CLASS_MAPPINGS: {list(NODE_CLASS_MAPPINGS.keys())}", flush=True)
    print(f"[Folder Parser] NODE_CLASS_MAPPINGS value type: {type(NODE_CLASS_MAPPINGS['APZFolderParser'])}", flush=True)
else:
    print("[Folder Parser] WARNING: APZFolderParser is None, not adding to mappings!", flush=True)

print("\n[Folder Parser] Building NODE_DISPLAY_NAME_MAPPINGS...", flush=True)
NODE_DISPLAY_NAME_MAPPINGS = {}
if "APZFolderParser" in NODE_CLASS_MAPPINGS:
    NODE_DISPLAY_NAME_MAPPINGS["APZFolderParser"] = "APZmedia Folder Parser"
    print(f"[Folder Parser] Added display name mapping", flush=True)
    print(f"[Folder Parser] NODE_DISPLAY_NAME_MAPPINGS: {NODE_DISPLAY_NAME_MAPPINGS}", flush=True)

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

print("\n[Folder Parser] Final registration:", flush=True)
print(f"  NODE_CLASS_MAPPINGS keys: {list(NODE_CLASS_MAPPINGS.keys())}", flush=True)
print(f"  NODE_CLASS_MAPPINGS values: {[str(v) for v in NODE_CLASS_MAPPINGS.values()]}", flush=True)
print(f"  NODE_DISPLAY_NAME_MAPPINGS: {NODE_DISPLAY_NAME_MAPPINGS}", flush=True)
print(f"  __all__: {__all__}", flush=True)

print("=" * 60, flush=True)
print("ComfyUI Folder Parser - Initialization complete", flush=True)
print("=" * 60, flush=True)

logger.info("ComfyUI Folder Parser extension has been loaded successfully.")
