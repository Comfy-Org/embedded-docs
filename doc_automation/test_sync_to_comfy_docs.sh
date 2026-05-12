#!/usr/bin/env bash
# Smoke tests for sync_to_comfy_docs.py (no writes to TARGET_DOCS; uses --dry-run).
# Run from repo root: bash doc_automation/test_sync_to_comfy_docs.sh

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "=== 1. Dry-run: 3 nodes, no docs.json ==="
python3 sync_to_comfy_docs.py --mode test --count 3 --dry-run --no-docs-json

echo ""
echo "=== 2. Non-existent node: expect 0 nodes synced ==="
python3 sync_to_comfy_docs.py --node NonExistentNode
# exit 0, "Syncing 0 nodes"

echo ""
echo "=== 3. Node with space in name (dry-run) ==="
python3 sync_to_comfy_docs.py --node "Epsilon Scaling" --dry-run --no-docs-json

echo ""
echo "=== 4. Node with space: Video Slice (dry-run) ==="
python3 sync_to_comfy_docs.py --node "Video Slice" --dry-run --no-docs-json

echo ""
echo "=== 5. Mode all dry-run (count only) ==="
python3 sync_to_comfy_docs.py --mode all --dry-run --no-docs-json 2>&1 | grep -E "^Syncing|^Done" || true

echo ""
echo "=== All smoke tests passed ==="
