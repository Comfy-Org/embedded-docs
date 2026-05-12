#!/usr/bin/env python3
"""
Update translation status in missing_nodes_report.json
After completing translations, remove the language from missing_languages
"""

import json
import sys
from pathlib import Path

# Paths
DOC_AUTOMATION_PATH = Path(__file__).parent
REPORT_FILE = DOC_AUTOMATION_PATH / "missing_nodes_report.json"


def update_translation_status(node_name: str, lang: str):
    """Remove a language from a node's missing_languages list"""
    
    if not REPORT_FILE.exists():
        print(f"❌ Error: Report file not found: {REPORT_FILE}")
        return False
    
    with open(REPORT_FILE, 'r', encoding='utf-8') as f:
        report = json.load(f)
    
    # Find the node and remove the language
    updated = False
    for doc in report.get('incomplete_docs', []):
        if doc['node'] == node_name:
            if lang in doc.get('missing_languages', []):
                doc['missing_languages'].remove(lang)
                updated = True
                break
    
    if updated:
        # Save updated report
        with open(REPORT_FILE, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        return True
    
    return False


def batch_update_translations(completed_nodes: dict):
    """
    Batch update translation status
    completed_nodes: {lang: [node1, node2, ...]}
    """
    
    if not REPORT_FILE.exists():
        print(f"❌ Error: Report file not found: {REPORT_FILE}")
        return False
    
    with open(REPORT_FILE, 'r', encoding='utf-8') as f:
        report = json.load(f)
    
    # Update each language's completed nodes
    for lang, nodes in completed_nodes.items():
        for node_name in nodes:
            for doc in report.get('incomplete_docs', []):
                if doc['node'] == node_name:
                    if lang in doc.get('missing_languages', []):
                        doc['missing_languages'].remove(lang)
    
    # Remove nodes that have no missing languages
    report['incomplete_docs'] = [
        doc for doc in report.get('incomplete_docs', [])
        if len(doc.get('missing_languages', [])) > 0
    ]
    
    # Save updated report
    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Updated translation status in {REPORT_FILE}")
    return True


if __name__ == "__main__":
    # For testing
    if len(sys.argv) > 2:
        node = sys.argv[1]
        lang = sys.argv[2]
        if update_translation_status(node, lang):
            print(f"✅ Removed {lang} from {node}'s missing languages")
        else:
            print(f"⚠️  No update needed for {node} ({lang})")

