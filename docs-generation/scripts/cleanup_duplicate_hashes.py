#!/usr/bin/env python3
"""
Clean up duplicate hash records in node_versions.json

This script removes duplicate version records that have the same hash,
keeping only the first occurrence of each unique hash.
"""

import json
from collections import OrderedDict

import runtime  # noqa: F401
from lib.paths import NODE_VERSIONS


def cleanup_duplicate_hashes():
    """Remove duplicate hash records from node_versions.json"""
    version_db_path = NODE_VERSIONS
    
    if not version_db_path.exists():
        print("❌ node_versions.json not found")
        return
    
    print("📖 Loading node_versions.json...")
    with open(version_db_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    nodes = data.get("nodes", {})
    total_removed = 0
    nodes_cleaned = []
    
    print(f"🔍 Processing {len(nodes)} nodes...")
    print("=" * 80)
    
    for node_name, node_data in nodes.items():
        versions = node_data.get("versions", [])
        if not versions:
            continue
        
        # Track seen hashes, keep only first occurrence
        seen_hashes = {}
        unique_versions = []
        removed_count = 0
        
        for version in versions:
            hash_val = version.get("source_hash", "")
            if hash_val in seen_hashes:
                # Duplicate hash, skip it
                removed_count += 1
                total_removed += 1
            else:
                # First occurrence of this hash, keep it
                seen_hashes[hash_val] = True
                unique_versions.append(version)
        
        if removed_count > 0:
            nodes_cleaned.append(node_name)
            print(f"  ✅ {node_name}: removed {removed_count} duplicate records (kept {len(unique_versions)})")
            node_data["versions"] = unique_versions
            
            # Update current_hash to match the last version (most recent)
            if unique_versions:
                node_data["current_hash"] = unique_versions[-1]["source_hash"]
                node_data["last_updated"] = unique_versions[-1]["extracted_at"]
    
    if total_removed > 0:
        print("=" * 80)
        print(f"\n📊 Cleanup finished:")
        print(f"  - cleaned {len(nodes_cleaned)} nodes")
        print(f"  - removed {total_removed} duplicate hash records")
        
        # Backup original file
        backup_path = version_db_path.with_suffix('.json.backup')
        print(f"\n💾 Backup of original file at: {backup_path}")
        with open(backup_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        # Save cleaned data
        print(f"💾 Saving cleaned data...")
        with open(version_db_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"\n✅ Cleanup complete!")
    else:
        print("\n✅ No duplicate records found; nothing to clean")


if __name__ == "__main__":
    cleanup_duplicate_hashes()
