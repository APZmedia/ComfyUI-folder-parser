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

# Importing custom nodes
try:
    from .nodes.apzFolderParser import APZFolderParser
    logger.info("Successfully imported APZFolderParser node.")
except Exception as e:
    logger.error("Failed to import APZFolderParser node.", exc_info=True)

NODE_CLASS_MAPPINGS = {
    "APZFolderParser": APZFolderParser,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "APZFolderParser": "APZmedia Folder Parser",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']

logger.info("ComfyUI Folder Parser extension has been loaded successfully.")
