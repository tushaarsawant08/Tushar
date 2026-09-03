import os
import hashlib
import json
from pathlib import Path
from collections import defaultdict

def get_file_hash(file_path):
    """Calculate MD5 hash of a file"""
    try:
        with open(file_path, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
    except Exception as e:
        return None

def get_all_files(folder):
    """Get all files in a folder with relative paths"""
    files = {}
    for root, dirs, filenames in os.walk(folder):
        for filename in filenames:
            full_path = os.path.join(root, filename)
            rel_path = os.path.relpath(full_path, folder)
            files[rel_path] = full_path
    return files

def compare_folders(folder1, folder2, output_format="text"):
    """
    Compare two folders and show differences.
    
    Args:
        folder1: Path to first folder
        folder2: Path to second folder
        output_format: "text" or "json"
    
    Returns:
        Dictionary with comparison results
    """
    
    if not os.path.exists(folder1):
        print(f"Error: {folder1} does not exist")
        return None
    
    if not os.path.exists(folder2):
        print(f"Error: {folder2} does not exist")
        return None
    
    # Get all files
    files1 = get_all_files(folder1)
    files2 = get_all_files(folder2)
    
    files1_set = set(files1.keys())
    files2_set = set(files2.keys())
    
    # Categorize files
    only_in_folder1 = files1_set - files2_set
    only_in_folder2 = files2_set - files1_set
    common_files = files1_set & files2_set
    
    # Compare common files
    identical_files = []
    different_files = []
    
    for file in sorted(common_files):
        hash1 = get_file_hash(files1[file])
        hash2 = get_file_hash(files2[file])
        
        if hash1 == hash2:
            identical_files.append(file)
        else:
            different_files.append({
                "file": file,
                "hash_in_folder1": hash1,
                "hash_in_folder2": hash2
            })
    
    # Prepare results
    results = {
        "folder1": os.path.abspath(folder1),
        "folder2": os.path.abspath(folder2),
        "only_in_folder1": sorted(list(only_in_folder1)),
        "only_in_folder2": sorted(list(only_in_folder2)),
        "identical_files": identical_files,
        "different_files": different_files,
        "summary": {
            "total_unique_to_folder1": len(only_in_folder1),
            "total_unique_to_folder2": len(only_in_folder2),
            "total_identical": len(identical_files),
            "total_different": len(different_files),
            "total_common": len(common_files)
        }
    }
    
    # Output results
    if output_format == "json":
        return results
    else:
        print_text_report(results)
        return results

def print_text_report(results):
    """Print comparison results in text format"""
    print("\n" + "="*70)
    print("FOLDER COMPARISON REPORT")
    print("="*70)
    
    print(f"\nFolder 1: {results['folder1']}")
    print(f"Folder 2: {results['folder2']}")
    
    print("\n" + "-"*70)
    print("SUMMARY")
    print("-"*70)
    summary = results['summary']
    print(f"Files only in Folder 1: {summary['total_unique_to_folder1']}")
    print(f"Files only in Folder 2: {summary['total_unique_to_folder2']}")
    print(f"Identical files: {summary['total_identical']}")
    print(f"Different files: {summary['total_different']}")
    print(f"Total common files: {summary['total_common']}")
    
    # Only in folder1
    if results['only_in_folder1']:
        print("\n" + "-"*70)
        print("FILES ONLY IN FOLDER 1:")
        print("-"*70)
        for f in results['only_in_folder1']:
            print(f"  • {f}")
    
    # Only in folder2
    if results['only_in_folder2']:
        print("\n" + "-"*70)
        print("FILES ONLY IN FOLDER 2:")
        print("-"*70)
        for f in results['only_in_folder2']:
            print(f"  • {f}")
    
    # Identical files
    if results['identical_files']:
        print("\n" + "-"*70)
        print("IDENTICAL FILES:")
        print("-"*70)
        for f in results['identical_files'][:10]:  # Show first 10
            print(f"  ✓ {f}")
        if len(results['identical_files']) > 10:
            print(f"  ... and {len(results['identical_files']) - 10} more")
    
    # Different files
    if results['different_files']:
        print("\n" + "-"*70)
        print("DIFFERENT FILES:")
        print("-"*70)
        for item in results['different_files']:
            print(f"  ✗ {item['file']}")
            print(f"    Folder 1 hash: {item['hash_in_folder1']}")
            print(f"    Folder 2 hash: {item['hash_in_folder2']}")
    
    print("\n" + "="*70 + "\n")

def save_report_to_json(results, filename="comparison_report.json"):
    """Save comparison results to JSON file"""
    with open(filename, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"Report saved to {filename}")

def save_report_to_html(results, filename="comparison_report.html"):
    """Save comparison results to HTML file for better visualization"""
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Folder Comparison Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; background-color: #f5f5f5; }}
            .container {{ max-width: 1000px; margin: 0 auto; background-color: white; padding: 20px; border-radius: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }}
            h1 {{ color: #333; border-bottom: 3px solid #007bff; padding-bottom: 10px; }}
            h2 {{ color: #555; margin-top: 30px; border-left: 4px solid #007bff; padding-left: 10px; }}
            .summary {{ background-color: #e7f3ff; padding: 15px; border-radius: 5px; margin: 15px 0; }}
            .summary-item {{ display: inline-block; margin-right: 20px; }}
            .summary-label {{ font-weight: bold; color: #333; }}
            .summary-value {{ font-size: 18px; color: #007bff; font-weight: bold; }}
            .folder-path {{ background-color: #f9f9f9; padding: 10px; margin: 5px 0; border-left: 3px solid #007bff; }}
            ul {{ list-style-type: none; padding: 0; }}
            li {{ padding: 8px; margin: 5px 0; background-color: #f9f9f9; border-radius: 3px; }}
            .only-folder1 {{ border-left: 4px solid #ff6b6b; }}
            .only-folder2 {{ border-left: 4px solid #51cf66; }}
            .identical {{ border-left: 4px solid #4dabf7; color: #4dabf7; }}
            .different {{ border-left: 4px solid #ffd43b; background-color: #fffbea; }}
            .hash {{ font-family: monospace; font-size: 12px; color: #666; margin-top: 5px; }}
            .icon {{ font-weight: bold; margin-right: 10px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📊 Folder Comparison Report</h1>
            
            <div class="folder-path"><strong>Folder 1:</strong> {results['folder1']}</div>
            <div class="folder-path"><strong>Folder 2:</strong> {results['folder2']}</div>
            
            <div class="summary">
                <div class="summary-item">
                    <div class="summary-label">Only in Folder 1:</div>
                    <div class="summary-value">{results['summary']['total_unique_to_folder1']}</div>
                </div>
                <div class="summary-item">
                    <div class="summary-label">Only in Folder 2:</div>
                    <div class="summary-value">{results['summary']['total_unique_to_folder2']}</div>
                </div>
                <div class="summary-item">
                    <div class="summary-label">Identical:</div>
                    <div class="summary-value">{results['summary']['total_identical']}</div>
                </div>
                <div class="summary-item">
                    <div class="summary-label">Different:</div>
                    <div class="summary-value">{results['summary']['total_different']}</div>
                </div>
            </div>
    """
    
    if results['only_in_folder1']:
        html_content += f"""
            <h2>📁 Files Only in Folder 1 ({len(results['only_in_folder1'])})</h2>
            <ul>
        """
        for f in results['only_in_folder1']:
            html_content += f'<li class="only-folder1"><span class="icon">❌</span>{f}</li>'
        html_content += "</ul>"
    
    if results['only_in_folder2']:
        html_content += f"""
            <h2>📁 Files Only in Folder 2 ({len(results['only_in_folder2'])})</h2>
            <ul>
        """
        for f in results['only_in_folder2']:
            html_content += f'<li class="only-folder2"><span class="icon">➕</span>{f}</li>'
        html_content += "</ul>"
    
    if results['identical_files']:
        html_content += f"""
            <h2>✅ Identical Files ({len(results['identical_files'])})</h2>
            <ul>
        """
        for f in results['identical_files'][:20]:
            html_content += f'<li class="identical"><span class="icon">✓</span>{f}</li>'
        if len(results['identical_files']) > 20:
            html_content += f'<li>... and {len(results["identical_files"]) - 20} more</li>'
        html_content += "</ul>"
    
    if results['different_files']:
        html_content += f"""
            <h2>⚠️ Different Files ({len(results['different_files'])})</h2>
            <ul>
        """
        for item in results['different_files']:
            html_content += f"""
            <li class="different">
                <span class="icon">⚠️</span>{item['file']}
                <div class="hash">
                    Folder 1: {item['hash_in_folder1']}<br>
                    Folder 2: {item['hash_in_folder2']}
                </div>
            </li>
            """
        html_content += "</ul>"
    
    html_content += """
        </div>
    </body>
    </html>
    """
    
    with open(filename, 'w') as f:
        f.write(html_content)
    print(f"HTML report saved to {filename}")

# Example usage
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 3:
        print("Usage: python folder_comparison.py <folder1> <folder2> [output_format]")
        print("\nExample:")
        print("  python folder_comparison.py /path/to/folder1 /path/to/folder2")
        print("  python folder_comparison.py folder1 folder2 json")
        print("\nOutput formats: text (default), json, html, all")
        sys.exit(1)
    
    folder1 = sys.argv[1]
    folder2 = sys.argv[2]
    output_format = sys.argv[3] if len(sys.argv) > 3 else "text"
    
    print(f"Comparing folders: {folder1} and {folder2}")
    print("Please wait...\n")
    
    results = compare_folders(folder1, folder2, output_format="json")
    
    if results:
        if output_format == "text":
            print_text_report(results)
        elif output_format == "json":
            print_text_report(results)
            save_report_to_json(results)
        elif output_format == "html":
            print_text_report(results)
            save_report_to_html(results)
        elif output_format == "all":
            print_text_report(results)
            save_report_to_json(results)
            save_report_to_html(results)
