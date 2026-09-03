# Tushar - Folder Comparison Tool

A comprehensive Python tool to compare two folders and generate detailed reports about differences.

## Features

✨ **Comprehensive Comparison**
- Identifies files unique to each folder
- Finds identical files using MD5 hash comparison
- Detects modified files with hash differences
- Generates detailed reports in multiple formats

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

### Basic Usage (Text Output)

```bash
python folder_comparison.py /path/to/folder1 /path/to/folder2
```

### JSON Output (for programmatic use)

```bash
python folder_comparison.py /path/to/folder1 /path/to/folder2 json
```

This creates `comparison_report.json` with structured data.

### HTML Report (visual report)

```bash
python folder_comparison.py /path/to/folder1 /path/to/folder2 html
```

This creates `comparison_report.html` that you can open in your browser.

### Generate All Formats

```bash
python folder_comparison.py /path/to/folder1 /path/to/folder2 all
```

## Example Output

### Console Output
```
======================================================================
FOLDER COMPARISON REPORT
======================================================================

Folder 1: /path/to/folder1
Folder 2: /path/to/folder2

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
  • file1.txt
  • file2.txt
  • subdir/file3.doc

----------------------------------------------------------------------
FILES ONLY IN FOLDER 2:
----------------------------------------------------------------------
  • newfile.txt
  • another_file.pdf

----------------------------------------------------------------------
DIFFERENT FILES:
----------------------------------------------------------------------
  ✗ config.json
    Folder 1 hash: a1b2c3d4e5f6...
    Folder 2 hash: f6e5d4c3b2a1...
```

## API Usage (Python)

You can also use this as a library in your own Python scripts:

```python
from folder_comparison import compare_folders, save_report_to_html

# Compare folders
results = compare_folders("folder1", "folder2", output_format="json")

# Access results programmatically
print(f"Identical files: {len(results['identical_files'])}")
print(f"Different files: {results['different_files']}")

# Generate HTML report
save_report_to_html(results, "my_report.html")
```

## Report Contents

### Summary Section
- Total files unique to each folder
- Count of identical and different files
- Total common files

### Unique Files (Folder 1)
Lists all files found only in Folder 1

### Unique Files (Folder 2)
Lists all files found only in Folder 2

### Identical Files
Files that exist in both folders with identical content (same MD5 hash)

### Different Files
Files that exist in both folders but have different content
- Shows MD5 hashes for each version

## How It Works

1. **Recursively scans** both folders to get all file paths
2. **Categorizes files** into unique or common
3. **Calculates MD5 hashes** for file content comparison
4. **Generates reports** in requested format(s)

## Performance Notes

- Handles large folders efficiently
- MD5 hashing provides fast comparison
- Memory usage scales with number of files, not file sizes

## Use Cases

- 📦 Compare backup folders
- 🔄 Sync verification before backup
- 📝 Detect accidental file changes
- 🗂️ Database/directory reconciliation
- 📊 Project version comparison
- 🔍 Quality assurance checks

## License

Open source - free to use and modify

## Author

tushaarsawant08

---

**Happy comparing! 🎉**
