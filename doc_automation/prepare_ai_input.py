#!/usr/bin/env python3
"""
Prepare AI input: Extract node source code and metadata
"""

import argparse
import os
import re
import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from dotenv import load_dotenv
from version_tracker import NodeVersionTracker
from node_source_extract import (
    extract_node_source_code as _extract_node_source_impl,
    extract_node_class_source,
    register_source_extract_cli_args,
    extract_config_from_parsed_args,
)


# Load environment variables
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(env_path)

# Get paths from environment variables
COMFYUI_PATH = Path(os.getenv('COMFYUI_PATH', '/Users/linmoumou/Documents/local_env/ComfyUI'))
EMBEDDED_DOCS_PATH = Path(os.getenv('EMBEDDED_DOCS_PATH', '/Users/linmoumou/Documents/local_env/embedded-docs'))
DOCS_PATH = EMBEDDED_DOCS_PATH / "comfyui_embedded_docs" / "docs"
OUTPUT_PATH = Path(__file__).parent / "ai_input"

# Initialize version tracker
version_tracker = NodeVersionTracker(OUTPUT_PATH)


def extract_node_source_code(
    file_path: Path,
    class_name: str,
    node_type: str,
    *,
    extract_config=None,
) -> Optional[str]:
    """Same-file preamble (imports/constants/helpers) + node class — see node_source_extract.py."""
    text = _extract_node_source_impl(
        file_path,
        class_name,
        node_type,
        comfy_root=COMFYUI_PATH,
        config=extract_config,
    )
    if not (text or "").strip():
        return None
    return text


def extract_basic_info(source_code: str, node_name: str) -> Dict[str, Any]:
    """Extract basic information from the source code"""
    info = {
        'node_name': node_name,
        'category': None,
        'description': None,
        'docstring': None,
    }
    
    # Extract category
    category_match = re.search(r'CATEGORY\s*=\s*["\']([^"\']+)["\']', source_code)
    if category_match:
        info['category'] = category_match.group(1)
    else:
        category_match = re.search(r'category\s*=\s*["\']([^"\']+)["\']', source_code)
        if category_match:
            info['category'] = category_match.group(1)
    
    # Extract docstring (class level documentation)
    docstring_match = re.search(r'class\s+\w+[^:]*:\s*(?:"""([^"]*?)"""|\'\'\'([^\']*?)\'\'\')', source_code, re.DOTALL)
    if docstring_match:
        info['docstring'] = (docstring_match.group(1) or docstring_match.group(2)).strip()
    
    # Extract DESCRIPTION
    desc_match = re.search(r'DESCRIPTION\s*=\s*["\']([^"\']+)["\']', source_code)
    if desc_match:
        info['description'] = desc_match.group(1)
    
    return info


def create_ai_prompt(node_name: str, source_code: str, basic_info: Dict, doc_rules: str) -> str:
    """Generate complete AI prompt for documentation"""
    
    github_link = f"https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/{node_name}/en.md"
    
    prompt = f"""# Task: Generate ComfyUI Node Documentation

## Node Information

**Node Name:** {node_name}
**Category:** {basic_info.get('category', 'Unknown')}

## Node Source Code

```python
{source_code}
```

## Extracted Information

- **Docstring:** {basic_info.get('docstring', 'None')}
- **Description:** {basic_info.get('description', 'None')}

## Documentation Requirements

{doc_rules}

## Your Task

Please generate a complete English documentation (en.md) for this node following the structure:

Generate the documentation with:

1. **Overview** - A concise 1-3 sentence explanation of what this node does and how it works (extract from docstring if available)
2. **Inputs** - Complete parameter table with all input parameters
3. **Outputs** - Output table with return values

### Table Format:

**Inputs table:**
| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|

- Required column: Use "Yes" for required parameters, "No" for optional parameters
- Check the source code: parameters in "required" section are "Yes", in "optional" section are "No"
- For new API: check if `optional=True` in parameter definition

**Outputs table:**
| Output Name | Data Type | Description |
|-------------|-----------|-------------|

### Important Guidelines:

- Keep data types in ENGLISH (IMAGE, STRING, INT, FLOAT, MODEL, CONDITIONING, etc.)
- Use backticks (`) for parameter names in tables
- Write in clear, non-technical language for general users
- Extract all information from the source code, including tooltips
- Use tooltip text EXACTLY as provided for parameter descriptions
- If a parameter has a default value, mention it in the Description column (e.g., "default: 1.0")
- If the node has a docstring or description, use it as foundation for your explanation
- Keep descriptions FACTUAL - avoid speculation or assumptions
- Do NOT add usage tips or best practices sections
- Focus on objective functionality based on the source code

### CRITICAL: Parameter Constraints and Limitations

**Carefully analyze the source code for parameter constraints:**

1. **Numeric Limits**: Check for max/min values, batch limits (e.g., `max=8` → "maximum 8 items")
2. **Parameter Dependencies**: Look for if/else logic showing:
   - Required combinations (e.g., "both image AND mask required")
   - Conditional requirements (e.g., "when mode=X, param Y is needed")
   - Mutual exclusions (e.g., "cannot use A and B together")
3. **Validation Logic**: Look for exceptions/errors in the code showing constraints
4. **Size Matching**: Note any dimension/shape matching requirements

**Document constraints in:**
- Parameter descriptions (for individual constraints)
- A note after the Inputs table (for complex multi-parameter constraints)

**Special Formatting for COMBO Parameters:**
- For parameters with multiple options, use `<br>` tags in the Range column to separate options
- Example Range column: `"option1"<br>"option2"<br>"option3"`
- In Description column, explain what each option does if they have different meanings
- Use `<br>` in Description too if needed for clarity

Example: If code shows `if image is not None and mask is not None: path = "/edit"` 
→ Document: "When both `image` and `mask` are provided, the node switches to editing mode"

Please provide the complete markdown content for en.md.
"""
    
    return prompt


def prepare_node_for_ai(
    node_name: str,
    file_path: Path,
    node_type: str,
    class_name: str,
    *,
    extract_config=None,
) -> bool:
    """Prepare AI input for a single node."""
    print(f"📝 Preparing node: {node_name}")

    # 1. Extract source code
    source_code = extract_node_source_code(
        file_path,
        class_name,
        node_type,
        extract_config=extract_config,
    )
    if not source_code:
        print(f"   ⚠️  Failed to extract source code")
        return False

    # Fingerprint only the node class body so preamble / cross-file context does not perturb hashes.
    class_fingerprint_src = extract_node_class_source(file_path, class_name)
    if not (class_fingerprint_src or "").strip():
        print(f"   ⚠️  Failed to extract node class body for versioning hash")
        return False

    # 2. Check for version changes (class body only — same as ai_input/source_code bundle context differs)
    is_changed, old_hash = version_tracker.check_node_changed(node_name, class_fingerprint_src)
    if is_changed and old_hash:
        print(f"   🔄 Source code changed (old hash: {old_hash[:16]}...)")
    
    # 3. Record version information
    version_info = version_tracker.record_node_version(
        node_name,
        class_fingerprint_src,
        metadata={
            "file_path": str(file_path.relative_to(COMFYUI_PATH)),
            "node_type": node_type,
            "class_name": class_name
        }
    )
    
    # 4. Extract basic info
    basic_info = extract_basic_info(source_code, node_name)
    
    # 5. Add version info to basic_info
    basic_info["version_info"] = {
        "extracted_at": version_info["extracted_at"],
        "source_hash": version_info["source_hash"],
        "source_length": version_info["source_length"],
        "hash_scope": "node_class_body",
    }
    
    # 6. Read documentation rules
    rules_file = Path(__file__).parent / "doc_rules.txt"
    if rules_file.exists():
        with open(rules_file, 'r', encoding='utf-8') as f:
            doc_rules = f.read()
    else:
        doc_rules = "Follow standard documentation practices."
    
    # 7. Create AI prompt
    ai_prompt = create_ai_prompt(node_name, source_code, basic_info, doc_rules)
    
    # 8. Save to output directory
    output_dir = OUTPUT_PATH / node_name
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Save source code
    with open(output_dir / "source_code.py", 'w', encoding='utf-8') as f:
        f.write(source_code)
    
    # Save basic info
    with open(output_dir / "basic_info.json", 'w', encoding='utf-8') as f:
        json.dump(basic_info, f, indent=2, ensure_ascii=False)
    
    # Save AI prompt
    with open(output_dir / "ai_prompt.txt", 'w', encoding='utf-8') as f:
        f.write(ai_prompt)
    
    print(f"   ✅ Prepared: {output_dir}")
    return True


def create_batch_file(nodes_data: List[Dict]) -> None:
    """Create batch file containing information of all processed nodes"""
    batch_file = OUTPUT_PATH / "batch_nodes.json"
    
    with open(batch_file, 'w', encoding='utf-8') as f:
        json.dump(nodes_data, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Batch file created: {batch_file}")


def main():
    """Main function"""
    import argparse

    pre = argparse.ArgumentParser(
        description=(
            "Prepare ai_input from ComfyUI sources. "
            "Positional arguments: test [count] | all | node <name> | changed "
            "(omit for default: first 5 missing)."
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Tip: put all options before positional words, e.g.\n"
        "  python3 prepare_ai_input.py --source-preamble slim --source-resolve 0 node CheckpointLoaderSimple",
    )
    register_source_extract_cli_args(pre)
    known, rest = pre.parse_known_args()
    extract_cfg = extract_config_from_parsed_args(known)

    print("=" * 80)
    print("ComfyUI Node AI Input Preparation Tool")
    print("=" * 80)
    print()

    # Create output directory
    OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

    # Read missing nodes report
    report_file = Path(__file__).parent / "missing_nodes_report.json"
    if not report_file.exists():
        print("❌ missing_nodes_report.json not found. Please run scan_missing_nodes.py first")
        return

    with open(report_file, "r", encoding="utf-8") as f:
        report = json.load(f)

    missing_nodes = report["missing_nodes"]
    changed_nodes = report.get("changed_nodes", [])

    # Also load all_nodes_info.json for forced single-node updates on nodes that
    # already have documentation (not present in missing_nodes).
    all_nodes_info_file = Path(__file__).parent / "all_nodes_info.json"
    all_nodes_info = {}
    if all_nodes_info_file.exists():
        with open(all_nodes_info_file, "r", encoding="utf-8") as f:
            raw = json.load(f)
        # Normalise: the file is {"total": N, "nodes": {...}} or a flat dict
        nodes_dict = raw.get("nodes", raw)
        for nid, meta in nodes_dict.items():
            all_nodes_info[nid] = {
                "name": nid,
                "file": meta["file"],
                "type": meta["type"],
                "class_name": meta.get("class_name", nid),
            }

    # Filter nodes that don't have documentation yet
    nodes_without_docs = []
    for node in missing_nodes:
        node_name = node["name"]
        doc_file = DOCS_PATH / node_name / "en.md"
        if not doc_file.exists():
            nodes_without_docs.append(node)

    print(f"📊 Total missing nodes: {len(missing_nodes)}")
    print(f"📝 Nodes definitely missing documentation: {len(nodes_without_docs)}")
    print(f"🔄 Nodes with changed source code: {len(changed_nodes)}\n")

    # Select nodes to process based on command arguments
    nodes_to_process = []

    if len(rest) > 0:
        mode = rest[0]
        if mode == "all":
            nodes_to_process = nodes_without_docs
        elif mode == "test":
            count = int(rest[1]) if len(rest) > 1 else 10
            nodes_to_process = nodes_without_docs[:count]
        elif mode == "node":
            if len(rest) < 2:
                print("❌ Please specify node name: python3 prepare_ai_input.py node <node_name>")
                return
            node_name = rest[1]
            # First look in missing_nodes; if not found, fall back to all_nodes_info so
            # that nodes with existing docs can also be force-refreshed from source.
            nodes_to_process = [n for n in missing_nodes if n["name"] == node_name]
            if not nodes_to_process:
                if node_name in all_nodes_info:
                    nodes_to_process = [all_nodes_info[node_name]]
                    print(f"   ℹ️  Node already has docs — re-preparing from latest source code: {node_name}")
                else:
                    print(f"❌ Node not found in missing_nodes_report.json or all_nodes_info.json: {node_name}")
                    return
        elif mode == "changed":
            if not changed_nodes:
                print("✅ No changed nodes to prepare.")
                return
            nodes_to_process = changed_nodes
            print(f"🔄 Changed mode: will re-prepare {len(nodes_to_process)} node(s) with updated source code\n")
        elif mode in ("regenerate-all", "everything"):
            if not all_nodes_info:
                print("❌ all_nodes_info.json missing or empty. Run scan_missing_nodes.py first.")
                return
            items = sorted(all_nodes_info.values(), key=lambda x: x["name"])
            if len(rest) > 1:
                try:
                    lim = int(rest[1])
                    if lim <= 0:
                        print("❌ Limit must be a positive integer.")
                        return
                    items = items[:lim]
                    print(f"   ℹ️  Limit active: first {lim} nodes only\n")
                except ValueError:
                    print(f"❌ Invalid limit (expected integer): {rest[1]!r}")
                    return
            nodes_to_process = items
            print(
                "⚙️  regenerate-all: preparing AI input for every node in all_nodes_info.json "
                f"({len(nodes_to_process)} node(s))\n"
            )
        else:
            print("❌ Invalid argument")
            print("Usage:")
            print("  python3 prepare_ai_input.py [OPTIONS] test [count]    # Prepare first N nodes (default 10)")
            print("  python3 prepare_ai_input.py [OPTIONS] all           # Prepare all missing nodes")
            print("  python3 prepare_ai_input.py [OPTIONS] node <name>   # Prepare specified node")
            print("  python3 prepare_ai_input.py [OPTIONS] changed       # Re-prepare nodes with changed source")
            print("  python3 prepare_ai_input.py [OPTIONS] regenerate-all [limit]   # Prepare ALL scanned nodes")
            print("  Options: --help  (see --source-* flags)")
            return
    else:
        # Default: prepare first 5 nodes without documentation
        print("💡 Default test mode: preparing first 5 nodes without documentation")
        print("   Use: [OPTIONS] test [count] | all | node <name> | changed | regenerate-all [limit]")
        print()
        nodes_to_process = nodes_without_docs[:5]

    print(f"🚀 Starting to prepare AI input for {len(nodes_to_process)} nodes...\n")

    # Prepare nodes
    success_count = 0
    failed_count = 0
    prepared_nodes = []

    for node in nodes_to_process:
        node_name = node["name"]
        file_path = COMFYUI_PATH / node["file"]
        node_type = node["type"]
        class_name = node.get("class_name", node_name)

        try:
            if prepare_node_for_ai(
                node_name,
                file_path,
                node_type,
                class_name,
                extract_config=extract_cfg,
            ):
                success_count += 1
                prepared_nodes.append(
                    {
                        "node_name": node_name,
                        "file": node["file"],
                        "type": node_type,
                        "ai_input_dir": str(OUTPUT_PATH / node_name),
                    }
                )
            else:
                failed_count += 1
        except Exception as e:
            print(f"   ❌ Preparation failed: {e}")
            failed_count += 1

    # Create batch file
    if prepared_nodes:
        create_batch_file(prepared_nodes)

    # Summary
    print("\n" + "=" * 80)
    print("📊 Preparation complete")
    print("=" * 80)
    print(f"✅ Success: {success_count}")
    print(f"❌ Failed: {failed_count}")
    print(f"\n📁 Output directory: {OUTPUT_PATH}")
    print("\n💡 Next step: use the files in the ai_input directory to generate documentation")
    print()


if __name__ == "__main__":
    main()

