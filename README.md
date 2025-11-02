# ComfyUI Folder Parser

A ComfyUI custom node that parses files from a folder with filtering and sorting capabilities. Outputs file paths for use in other ComfyUI nodes.

## Features

- **File Filtering**: Filter by file extension or regex pattern on filename
- **Sorting**: Sort by date (modified/created) or alphabetically, with reverse option
- **Index Selection**: Select a specific file by index from the filtered/sorted list
- **Cross-Platform**: Works on Windows, macOS, and Linux

## Installation

Copy this repository to your ComfyUI `custom_nodes` directory and restart ComfyUI.

## Usage

### Inputs

- `folder_path` - Path to the folder to parse
- `file_index` - Index of file to output (0-based)
- `enable_extension_filter` - Enable filtering by extension
- `file_extensions` - Comma-separated extensions (e.g., "jpg,png,json")
- `enable_regex_filter` - Enable filtering by regex pattern
- `regex_pattern` - Regex pattern to match filenames
- `sort_mode` - Sort mode: "none", "date_modified", "date_created", or "alphabetical"
- `reverse_sort` - Reverse the sort order

### Outputs

- `file_path` - Full absolute path to the selected file
- `total_files` - Total number of matching files
- `file_list` - Comma-separated list of all matching files

## Examples

**Get first JPG file:**
```
folder_path: "C:\Images"
enable_extension_filter: true
file_extensions: "jpg"
file_index: 0
```

**Get most recently modified file:**
```
folder_path: "C:\Images"
sort_mode: "date_modified"
reverse_sort: true
file_index: 0
```

**Get file matching pattern:**
```
folder_path: "C:\Images"
enable_regex_filter: true
regex_pattern: "^IMG_\\d{4}\\.jpg$"
file_index: 0
```

## Notes

- Searches only the specified folder (non-recursive)
- Node will error if file index is out of range
- Extension filtering is case-insensitive
- Regex matching is performed on filename only

## Requirements

- Python 3.7+
- ComfyUI
- No external dependencies

## License

See LICENSE file.
