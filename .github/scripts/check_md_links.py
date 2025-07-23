import os
import re
import sys
from pathlib import Path

# Try to find the docs directory relative to the script location first
# If that fails, try relative to current working directory
script_based_docs = Path(__file__).parent.parent.parent / 'comfyui_embedded_docs' / 'docs'
cwd_based_docs = Path.cwd() / 'comfyui_embedded_docs' / 'docs'

if script_based_docs.exists():
    DOCS_ROOT = script_based_docs
elif cwd_based_docs.exists():
    DOCS_ROOT = cwd_based_docs
else:
    # Fallback: search for the docs directory
    current = Path.cwd()
    while current != current.parent:  # Stop at filesystem root
        potential_docs = current / 'comfyui_embedded_docs' / 'docs'
        if potential_docs.exists():
            DOCS_ROOT = potential_docs
            break
        current = current.parent
    else:
        DOCS_ROOT = script_based_docs  # Default to original logic

# Supported file extensions
doc_exts = {'.md', '.mdx'}

# Match Markdown images/links and HTML img/video/audio/source tag src attributes
MD_LINK_RE = re.compile(r'!\[[^\]]*\]\(([^)]+)\)|\[[^\]]*\]\(([^)]+)\)')
HTML_SRC_RE = re.compile(r'<(?:img|video|audio|source)[^>]+src=["\']([^"\'>]+)["\']', re.IGNORECASE)

# Only check local relative paths (not starting with http/https/data:)
def is_local_link(link):
    link = link.strip()
    return not (link.startswith('http://') or link.startswith('https://') or link.startswith('data:'))

def find_links_in_line(line):
    links = []
    for m in MD_LINK_RE.finditer(line):
        for g in m.groups():
            if g and is_local_link(g):
                links.append(g)
    for m in HTML_SRC_RE.finditer(line):
        g = m.group(1)
        if g and is_local_link(g):
            links.append(g)
    return links

def check_links():
    if not DOCS_ROOT.exists():
        print(f"ERROR: DOCS_ROOT directory does not exist: {DOCS_ROOT}")
        print(f"Current working directory: {os.getcwd()}")
        print(f"Script location: {Path(__file__)}")
        sys.exit(1)
    
    errors = []
    for root, _, files in os.walk(DOCS_ROOT):
        for fname in files:
            if Path(fname).suffix.lower() in doc_exts:
                fpath = Path(root) / fname
                rel_fpath = fpath.relative_to(DOCS_ROOT.parent.parent)
                with open(fpath, encoding='utf-8') as f:
                    for idx, line in enumerate(f, 1):
                        for link in find_links_in_line(line):
                            # Handle anchors and query parameters
                            link_path = link.split('#')[0].split('?')[0]
                            # Absolute path (starting with /) is relative to docs root
                            if link_path.startswith('/'):
                                abs_path = DOCS_ROOT / link_path.lstrip('/')
                            else:
                                # Use resolve() for relative paths but ensure proper handling
                                try:
                                    abs_path = (fpath.parent / link_path).resolve()
                                    # Additional check: ensure the resolved path is still under expected directory
                                    if not abs_path.exists():
                                        # Try alternative resolution without resolve() for symlink issues
                                        abs_path_alt = (fpath.parent / link_path).absolute()
                                        if abs_path_alt.exists():
                                            abs_path = abs_path_alt
                                except (OSError, ValueError):
                                    # Fallback for path resolution issues
                                    abs_path = (fpath.parent / link_path).absolute()
                            
                            if not abs_path.exists():
                                # Add detailed debugging information
                                debug_info = []
                                debug_info.append(f"Original link: {link}")
                                debug_info.append(f"Link path (no anchor/query): {link_path}")
                                debug_info.append(f"Source file: {fpath}")
                                debug_info.append(f"Source parent: {fpath.parent}")
                                debug_info.append(f"Resolved path: {abs_path}")
                                debug_info.append(f"Path exists: {abs_path.exists()}")
                                
                                # Check if parent directory exists
                                debug_info.append(f"Parent dir exists: {abs_path.parent.exists()}")
                                if abs_path.parent.exists():
                                    try:
                                        parent_contents = list(abs_path.parent.iterdir())
                                        debug_info.append(f"Parent dir contents: {[p.name for p in parent_contents]}")
                                    except Exception as e:
                                        debug_info.append(f"Error reading parent dir: {e}")
                                
                                # Check if it's a case sensitivity issue
                                if abs_path.parent.exists():
                                    actual_name = abs_path.name
                                    try:
                                        for item in abs_path.parent.iterdir():
                                            if item.name.lower() == actual_name.lower() and item.name != actual_name:
                                                debug_info.append(f"Case mismatch found: expected '{actual_name}', found '{item.name}'")
                                    except Exception:
                                        pass
                                
                                error_msg = f"[NOT FOUND] {rel_fpath}:{idx}: {link} (resolved: {abs_path})"
                                error_msg += "\n  DEBUG: " + " | ".join(debug_info)
                                errors.append(error_msg)
    if errors:
        print("\nThe following issues were found during link checking:")
        # Show first 5 errors with full debug info, then just count the rest
        for i, err in enumerate(errors):
            if i < 5:
                print(err)
            elif i == 5:
                print(f"\n... and {len(errors) - 5} more similar errors (showing first 5 with debug info)")
                break
        
        # Show summary of remaining errors without debug info
        if len(errors) > 5:
            print("\nRemaining errors (summary):")
            for err in errors[5:]:
                # Extract just the basic error line
                basic_err = err.split('\n')[0]
                print(basic_err)
        
        print(f"\nA total of {len(errors)} invalid links were found. Please fix the above issues.")
        sys.exit(1)
    else:
        print("All local resource links are valid.")

if __name__ == '__main__':
    check_links() 