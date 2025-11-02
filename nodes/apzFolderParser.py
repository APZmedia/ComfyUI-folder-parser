import os
import re
import logging

logger = logging.getLogger(__name__)

print("[APZFolderParser] Module loaded")


class APZFolderParser:
    _sort_modes = ["none", "date_modified", "date_created", "alphabetical"]
    
    RETURN_TYPES = ("STRING", "INT", "STRING")
    RETURN_NAMES = ("file_path", "total_files", "file_list")
    FUNCTION = "parse_folder"
    CATEGORY = "file/input"
    
    def __init__(self):
        print("[APZFolderParser] Instance initialized")
        logger.info("APZFolderParser instance created")
    
    @classmethod
    def INPUT_TYPES(cls):
        print("[APZFolderParser] INPUT_TYPES() called")
        input_def = {
            "required": {
                "folder_path": ("STRING", {"default": "", "multiline": False}),
                "file_index": ("INT", {"default": 0, "min": 0}),
                "enable_extension_filter": ("BOOLEAN", {"default": False}),
                "file_extensions": ("STRING", {"default": "jpg,png,json", "multiline": False}),
                "enable_regex_filter": ("BOOLEAN", {"default": False}),
                "regex_pattern": ("STRING", {"default": "", "multiline": False}),
                "sort_mode": (cls._sort_modes, {"default": "none"}),
                "reverse_sort": ("BOOLEAN", {"default": False}),
            }
        }
        print(f"[APZFolderParser] INPUT_TYPES defined with {len(input_def['required'])} required inputs")
        return input_def
    
    def parse_folder(self, folder_path, file_index, enable_extension_filter, file_extensions, 
                     enable_regex_filter, regex_pattern, sort_mode, reverse_sort):
        """
        Parse files from a folder with optional filtering and sorting.
        
        Returns:
            file_path (str): Full path to the file at the specified index
            total_files (int): Total number of matching files found
            file_list (str): Comma-separated list of all matching file paths
        """
        try:
            # Normalize and validate folder path
            folder_path = os.path.normpath(folder_path.strip())
            
            if not folder_path:
                raise ValueError("Folder path cannot be empty")
            
            if not os.path.exists(folder_path):
                raise ValueError(f"Folder path does not exist: {folder_path}")
            
            if not os.path.isdir(folder_path):
                raise ValueError(f"Path is not a directory: {folder_path}")
            
            # Get absolute path (for internal processing, but keep original for logging)
            original_path = folder_path
            folder_path = os.path.abspath(folder_path)
            
            # Discover files (non-recursive, only in specified folder)
            all_files = []
            try:
                items = os.listdir(folder_path)
                for item in items:
                    item_path = os.path.join(folder_path, item)
                    if os.path.isfile(item_path):
                        all_files.append(item_path)
            except PermissionError:
                raise ValueError(f"Permission denied accessing folder: {folder_path}")
            except Exception as e:
                raise ValueError(f"Error reading folder: {str(e)}")
            
            if not all_files:
                logger.warning(f"No files found in folder: {folder_path}")
                return "", 0, ""
            
            # Apply extension filtering
            if enable_extension_filter:
                extensions = self._normalize_extensions(file_extensions)
                if extensions:
                    all_files = [f for f in all_files if self._match_extension(f, extensions)]
            
            # Apply regex filtering
            if enable_regex_filter:
                if not regex_pattern:
                    logger.warning("Regex filter enabled but pattern is empty, skipping regex filter")
                else:
                    try:
                        pattern = re.compile(regex_pattern)
                        all_files = [f for f in all_files if self._match_regex(os.path.basename(f), pattern)]
                    except re.error as e:
                        logger.warning(f"Invalid regex pattern '{regex_pattern}': {str(e)}, skipping regex filter")
            
            if not all_files:
                logger.warning("No files matched the filter criteria")
                return "", 0, ""
            
            # Apply sorting
            if sort_mode != "none":
                all_files = self._sort_files(all_files, sort_mode, reverse_sort)
            
            # Validate index
            total_files = len(all_files)
            if file_index >= total_files:
                raise ValueError(
                    f"File index {file_index} is out of range. "
                    f"Total files found: {total_files}. Valid indices: 0 to {total_files - 1}"
                )
            
            # Get file at index
            selected_file = all_files[file_index]
            
            # Create file list string for debugging (limit length for readability)
            file_list_str = ",".join(all_files[:10])  # First 10 files
            if len(all_files) > 10:
                file_list_str += f",... (+{len(all_files) - 10} more)"
            
            logger.info(f"FolderParser: Found {total_files} files, returning index {file_index}: {os.path.basename(selected_file)}")
            print(f"[APZFolderParser] Successfully parsed folder: {total_files} files found, selected index {file_index}")
            
            return selected_file, total_files, file_list_str
            
        except ValueError as e:
            logger.error(f"FolderParser error: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error in FolderParser: {str(e)}")
            raise ValueError(f"Unexpected error: {str(e)}")
    
    def _normalize_extensions(self, ext_string):
        """
        Parse and normalize extension list from comma-separated string.
        Returns list of normalized extensions (lowercase, with leading dot).
        """
        if not ext_string:
            return []
        
        extensions = []
        for ext in ext_string.split(','):
            ext = ext.strip().lower()
            if ext:
                # Add leading dot if not present
                if not ext.startswith('.'):
                    ext = '.' + ext
                extensions.append(ext)
        
        return extensions
    
    def _match_extension(self, file_path, extensions):
        """
        Check if file matches any of the provided extensions (case-insensitive).
        """
        _, ext = os.path.splitext(file_path)
        return ext.lower() in extensions
    
    def _match_regex(self, filename, pattern):
        """
        Check if filename matches the regex pattern.
        """
        return bool(pattern.search(filename))
    
    def _sort_files(self, files, sort_mode, reverse_sort):
        """
        Sort files according to the specified mode.
        
        Args:
            files: List of file paths
            sort_mode: "date_modified", "date_created", or "alphabetical"
            reverse_sort: If True, reverse the sort order
        
        Returns:
            Sorted list of file paths
        """
        if sort_mode == "date_modified":
            sorted_files = sorted(files, key=lambda f: os.path.getmtime(f), reverse=reverse_sort)
        elif sort_mode == "date_created":
            sorted_files = sorted(files, key=lambda f: os.path.getctime(f), reverse=reverse_sort)
        elif sort_mode == "alphabetical":
            # Sort by filename (not full path)
            sorted_files = sorted(files, key=lambda f: os.path.basename(f).lower(), reverse=reverse_sort)
        else:
            sorted_files = files
        
        return sorted_files


# Print class attributes after class definition
print(f"[APZFolderParser] Class defined with attributes:")
print(f"  RETURN_TYPES: {APZFolderParser.RETURN_TYPES}")
print(f"  RETURN_NAMES: {APZFolderParser.RETURN_NAMES}")
print(f"  FUNCTION: {APZFolderParser.FUNCTION}")
print(f"  CATEGORY: {APZFolderParser.CATEGORY}")
print(f"  _sort_modes: {APZFolderParser._sort_modes}")
