import os
import re
import sys
from pathlib import Path

DOCS_ROOT = Path(__file__).parent.parent.parent / 'comfyui_embedded_docs' / 'docs'

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
                                abs_path = (fpath.parent / link_path).resolve()
                            if not abs_path.exists():
                                errors.append(f"[NOT FOUND] {rel_fpath}:{idx}: {link} (resolved: {abs_path})")
    if errors:
        print("\nThe following issues were found during link checking:")
        for err in errors:
            print(err)
        print(f"\nA total of {len(errors)} invalid links were found. Please fix the above issues.")
        sys.exit(1)
    else:
        print("All local resource links are valid.")

if __name__ == '__main__':
    check_links() 