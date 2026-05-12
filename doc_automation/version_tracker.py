#!/usr/bin/env python3
"""
Node Version Tracking and Change Detection Tool
"""

import os
import json
import hashlib
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple


class NodeVersionTracker:
    """Node version tracker for detecting source code changes"""
    
    def __init__(self, ai_input_path: Path):
        self.ai_input_path = ai_input_path
        self.version_db_path = ai_input_path.parent / "node_versions.json"
        self.version_db = self._load_version_db()
    
    def _load_version_db(self) -> Dict:
        """Load version database from JSON file"""
        if self.version_db_path.exists():
            with open(self.version_db_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {"nodes": {}, "last_scan": None}
    
    def _save_version_db(self):
        """Save version database to JSON file"""
        with open(self.version_db_path, 'w', encoding='utf-8') as f:
            json.dump(self.version_db, f, indent=2, ensure_ascii=False)
    
    @staticmethod
    def calculate_source_hash(source_code: str) -> str:
        """Calculate SHA256 hash of source code"""
        return hashlib.sha256(source_code.encode('utf-8')).hexdigest()
    
    @staticmethod
    def get_current_timestamp() -> str:
        """Get current timestamp in ISO format"""
        return datetime.now().isoformat()
    
    def record_node_version(self, node_name: str, source_code: str, metadata: Dict = None) -> Dict:
        """Record node version information with source code hash
        
        If the hash is the same as current_hash, only update last_updated timestamp.
        If the hash is different, append a new version record.
        """
        current_hash = self.calculate_source_hash(source_code)
        timestamp = self.get_current_timestamp()
        
        # Save to version database
        if node_name not in self.version_db["nodes"]:
            self.version_db["nodes"][node_name] = {"versions": []}
        
        node_data = self.version_db["nodes"][node_name]
        existing_hash = node_data.get("current_hash")
        
        # If hash is the same, only update timestamp (don't create duplicate record)
        if existing_hash == current_hash:
            node_data["last_updated"] = timestamp
            # Return existing version info structure for compatibility
            version_info = {
                "node_name": node_name,
                "extracted_at": timestamp,
                "source_hash": current_hash,
                "source_length": len(source_code),
                "metadata": metadata or {}
            }
        else:
            # Hash is different, create new version record
            version_info = {
                "node_name": node_name,
                "extracted_at": timestamp,
                "source_hash": current_hash,
                "source_length": len(source_code),
                "metadata": metadata or {}
            }
            node_data["versions"].append(version_info)
            node_data["current_hash"] = current_hash
            node_data["last_updated"] = timestamp
        
        self.version_db["last_scan"] = timestamp
        self._save_version_db()
        return version_info
    
    def check_node_changed(self, node_name: str, current_source: str) -> Tuple[bool, Optional[str]]:
        """Check if node source code has changed
        
        Returns:
            (is_changed, previous_hash)
        """
        if node_name not in self.version_db["nodes"]:
            return True, None  # New node
        
        current_hash = self.calculate_source_hash(current_source)
        previous_hash = self.version_db["nodes"][node_name].get("current_hash")
        
        return current_hash != previous_hash, previous_hash
    
    def get_node_version_history(self, node_name: str) -> List[Dict]:
        """Get version history of a node"""
        if node_name not in self.version_db["nodes"]:
            return []
        return self.version_db["nodes"][node_name].get("versions", [])
    
    def get_changed_nodes(self, comfyui_path: Path) -> List[Dict]:
        """Compare each prepared node's recorded hash to live ComfyUI class source (same rule as scan/prepare).

        Uses the latest known ``file_path`` / ``class_name`` in version history metadata; skips nodes
        whose bundle was never fingerprinted against a real ``.py`` path.
        """
        from node_source_extract import extract_node_class_source

        changed_nodes = []
        root = Path(comfyui_path)

        for node_name, node_data in self.version_db["nodes"].items():
            ai_bundle = self.ai_input_path / node_name / "source_code.py"
            if not ai_bundle.exists():
                continue

            meta: Dict = {}
            vers = node_data.get("versions") or []
            if vers:
                meta = vers[-1].get("metadata") or {}

            rel = meta.get("file_path")
            cls_nm = meta.get("class_name") or node_name
            if not rel:
                continue

            fp = root / rel
            if not fp.is_file():
                continue

            class_src = extract_node_class_source(fp, cls_nm)
            if not (class_src or "").strip():
                continue

            is_changed, old_hash = self.check_node_changed(node_name, class_src)
            if is_changed:
                changed_nodes.append(
                    {
                        "node_name": node_name,
                        "old_hash": old_hash,
                        "new_hash": self.calculate_source_hash(class_src),
                        "last_updated": node_data.get("last_updated"),
                    }
                )

        return changed_nodes


def compare_versions(version1: Dict, version2: Dict) -> Dict:
    """Compare differences between two versions"""
    return {
        "hash_changed": version1["source_hash"] != version2["source_hash"],
        "length_changed": version1["source_length"] != version2["source_length"],
        "length_diff": version2["source_length"] - version1["source_length"],
        "time_diff": version2["extracted_at"]
    }


def main():
    """Main function: Check changed nodes"""
    import sys
    
    ai_input_path = Path(__file__).parent / "ai_input"
    tracker = NodeVersionTracker(ai_input_path)
    
    if len(sys.argv) > 1 and sys.argv[1] == "check":
        # Check which nodes have changes
        print("🔍 Checking node changes...")
        print("=" * 80)
        
        changed = tracker.get_changed_nodes(Path("/Users/linmoumou/Documents/local_env/ComfyUI"))
        
        if changed:
            print(f"\n📊 Found {len(changed)} nodes with changes:\n")
            for node in changed:
                print(f"  - {node['node_name']}")
                print(f"    Old hash: {node['old_hash'][:16]}...")
                print(f"    New hash: {node['new_hash'][:16]}...")
                print(f"    Last updated: {node['last_updated']}")
                print()
        else:
            print("\n✅ No nodes have changed")
    
    elif len(sys.argv) > 1 and sys.argv[1] == "history":
        # View history of a specific node
        if len(sys.argv) < 3:
            print("Usage: python3 version_tracker.py history <node_name>")
            return
        
        node_name = sys.argv[2]
        history = tracker.get_node_version_history(node_name)
        
        print(f"📜 Version history for node {node_name}:")
        print("=" * 80)
        
        if history:
            for idx, version in enumerate(history, 1):
                print(f"\nVersion {idx}:")
                print(f"  Extracted at: {version['extracted_at']}")
                print(f"  Source hash: {version['source_hash'][:16]}...")
                print(f"  Code length: {version['source_length']} characters")
        else:
            print(f"\nNo version records found for node {node_name}")
    
    else:
        print("Node Version Tracking Tool")
        print("=" * 80)
        print("\nUsage:")
        print("  python3 version_tracker.py check           # Check changed nodes")
        print("  python3 version_tracker.py history <node_name>  # View node history")
        print("\nDatabase location:", tracker.version_db_path)
        print(f"Recorded nodes: {len(tracker.version_db['nodes'])}")
        if tracker.version_db['last_scan']:
            print(f"Last scan time: {tracker.version_db['last_scan']}")


if __name__ == "__main__":
    main()
