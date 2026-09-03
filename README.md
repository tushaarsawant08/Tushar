# Tushar - Folder Comparison Tool

A comprehensive Python tool to compare two folders and generate detailed reports about differences. Now with **file extension filtering**!

## Features

✨ **Comprehensive Comparison**
- Identifies files unique to each folder
- Finds identical files using MD5 hash comparison
- Detects modified files with hash differences
- Generates detailed reports in multiple formats

🎯 **File Extension Filtering** (NEW!)
- Filter comparisons by file type (`.txt`, `.py`, `.json`, `.pdf`, `.csv`, `.xml`, etc.)
- Case-insensitive matching (`.TXT`, `.txt`, `.Txt` all work)
- Extension filter shown in all reports

📊 **Multiple Output Formats**
- **Text**: Console output with organized sections
- **JSON**: Structured data for programmatic access
- **HTML**: Interactive visual report with styling

🚀 **Easy to Use**
- Simple command-line interface
- Works with any folder structure
- Handles large folder hierarchies efficiently

## Installation

No special dependencies required! Just Python 3.6+

```bash
git clone https://github.com/tushaarsawant08/Tushar.git
cd Tushar
```

## Usage

### Compare ALL Files (No Filter)

```bash
python folder_comparison.py /path/to/folder1 /path/to/folder2
```

### Compare Specific File Types (With Extension Filter)

```bash
# Compare only Python files
python folder_comparison.py folder1 folder2 .py

# Compare only JSON files
python folder_comparison.py folder1 folder2 .json

# Compare only text files
python folder_comparison.py folder1 folder2 .txt

# Compare only CSV files
python folder_comparison.py folder1 folder2 .csv

# Compare only PDF files
python folder_comparison.py folder1 folder2 .pdf
```

### Different Output Formats

```bash
# Text output (default - prints to console)
python folder_comparison.py folder1 folder2 .py

# JSON output (creates comparison_report.json)
python folder_comparison.py folder1 folder2 .py json

# HTML output (creates comparison_report.html - open in browser!)
python folder_comparison.py folder1 folder2 .py html

# All formats (generates text, JSON, and HTML reports)
python folder_comparison.py folder1 folder2 .py all
```

## Complete Examples

```bash
# Example 1: Compare all files with text output
python folder_comparison.py backup1 backup2

# Example 2: Compare only Python files
python folder_comparison.py source1 source2 .py

# Example 3: Compare only configuration files
python folder_comparison.py config_v1 config_v2 .json

# Example 4: Compare only text files with HTML report
python folder_comparison.py docs_old docs_new .txt html

# Example 5: Compare all file types and generate all reports
python folder_comparison.py project_a project_b all

# Example 6: Compare only CSV files with JSON output
python folder_comparison.py data1 data2 .csv json
```

## Example Output

### Console Output (Text Format)
```
======================================================================
FOLDER COMPARISON REPORT (.py)
======================================================================

Folder 1: E:\projects\source1
Folder 2: E:\projects\source2

----------------------------------------------------------------------
SUMMARY
----------------------------------------------------------------------
Files only in Folder 1: 3
Files only in Folder 2: 2
Identical files: 15
Different files: 1
Total common files: 16

----------------------------------------------------------------------
FILES ONLY IN FOLDER 1:
----------------------------------------------------------------------
  • utils/helper.py
  • tests/test_helper.py
  • config/settings.py

----------------------------------------------------------------------
FILES ONLY IN FOLDER 2:
----------------------------------------------------------------------
  • new_module.py
  • another_file.py

----------------------------------------------------------------------
IDENTICAL FILES:
----------------------------------------------------------------------
  [=] main.py
  [=] app.py
  [=] database.py
  ... and 12 more

----------------------------------------------------------------------
DIFFERENT FILES:
----------------------------------------------------------------------
  [!] constants.py
    Folder 1 hash: a1b2c3d4e5f6...
    Folder 2 hash: f6e5d4c3b2a1...

======================================================================
```

### HTML Report (Visual)
The HTML report provides:
- 📊 Summary statistics with file counts
- 📁 Color-coded sections for easy scanning
- 🔍 File-by-file comparison results
- 🏷️ Extension filter badge
- 📍 Full folder paths
- ✨ Professional styling

Open `comparison_report.html` in your browser to view!

### JSON Report (Programmatic)
```json
{
  "folder1": "/path/to/folder1",
  "folder2": "/path/to/folder2",
  "extension_filter": ".py",
  "only_in_folder1": ["file1.py", "file2.py"],
  "only_in_folder2": ["file3.py"],
  "identical_files": ["main.py", "utils.py"],
  "different_files": [
    {
      "file": "config.py",
      "hash_in_folder1": "a1b2c3d4...",
      "hash_in_folder2": "f6e5d4c3..."
    }
  ],
  "summary": {
    "total_unique_to_folder1": 2,
    "total_unique_to_folder2": 1,
    "total_identical": 2,
    "total_different": 1,
    "total_common": 3
  }
}
```

## API Usage (Python)

You can also use this as a library in your own Python scripts:

```python
from folder_comparison import compare_folders, save_report_to_html, print_text_report

# Compare folders with extension filter
results = compare_folders("folder1", "folder2", extension=".py", output_format="json")

# Access results programmatically
print(f"Identical Python files: {len(results['identical_files'])}")
print(f"Different Python files: {results['different_files']}")

# Generate HTML report
save_report_to_html(results, "python_files_comparison.html")

# Print to console
print_text_report(results)
```

## Supported Extensions

Works with any file extension! Common examples:

**Programming Languages:**
- `.py` - Python
- `.java` - Java
- `.js`, `.ts` - JavaScript/TypeScript
- `.cpp`, `.c` - C/C++
- `.go` - Go
- `.rs` - Rust

**Data Files:**
- `.json` - JSON
- `.csv` - CSV
- `.xml` - XML
- `.yaml`, `.yml` - YAML
- `.sql` - SQL

**Documents:**
- `.txt` - Plain text
- `.md` - Markdown
- `.pdf` - PDF
- `.docx`, `.doc` - Word

**Web:**
- `.html` - HTML
- `.css` - CSS
- `.php` - PHP

**Configuration:**
- `.conf` - Configuration
- `.ini` - INI files
- `.env` - Environment files

## How It Works

1. **Recursively scans** both folders to get all file paths
2. **Filters by extension** (if specified)
3. **Categorizes files** into unique or common
4. **Calculates MD5 hashes** for file content comparison
5. **Generates reports** in requested format(s)

## Performance Notes

- Handles large folders efficiently
- MD5 hashing provides fast comparison
- Memory usage scales with number of files, not file sizes
- Filtering by extension improves performance (fewer files to compare)

## Use Cases

- 📦 Compare backup folders
- 🔄 Sync verification before backup
- 📝 Detect accidental file changes
- 🗂️ Database/directory reconciliation
- 📊 Project version comparison
- 🔍 Quality assurance checks
- 💾 Database comparison
- 🖼️ Compare media libraries
- 📄 Document version control

## Troubleshooting

### Issue: `UnicodeEncodeError` on Windows
**Solution:** The script now uses UTF-8 encoding. If you encounter issues, ensure you're using Python 3.6+

### Issue: Permission denied errors
**Solution:** Run the script with appropriate permissions or ensure you have read access to both folders

### Issue: No files found
**Solution:** 
- Check folder paths are correct
- For extension filter, ensure files have the extension (e.g., `.py` for Python files)
- Use without extension filter to verify folders are accessible

## Supported Platforms

- ✅ Windows
- ✅ macOS
- ✅ Linux

## Requirements

- Python 3.6+
- No external dependencies (uses only Python standard library)

## License

Open source - free to use and modify

## Author

tushaarsawant08

---

**Happy comparing! 🎉**

For more information or issues, visit: https://github.com/tushaarsawant08/Tushar
