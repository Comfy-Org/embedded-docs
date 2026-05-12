# ComfyUI Node Documentation Automation

Automated tool chain for generating ComfyUI node documentation using AI.

## Features

- ✅ Scan ComfyUI codebase to identify nodes missing documentation
- ✅ Extract richer same-file context (imports, helpers, constants) plus the node class; skip peer nodes in mega-files (`node_source_extract.py`)
- ✅ Generate standardized documentation using AI (DeepSeek/OpenAI/etc.)
- ✅ Version tracking with source code hash comparison
- ✅ Automatic GitHub link and disclaimer injection
- ✅ Comprehensive logging and error handling

## Quick Start

### 1. Install Dependencies

```bash
cd doc_automation
conda activate LLM_base  # or your environment
pip install -r requirements.txt
```

### 2. Configure API Key

Edit `../.env` file:

```bash
DEEPSEEK_API_KEY=your_api_key_here
```

### 3. Generate Documentation

```bash
# Scan missing nodes
python3 scan_missing_nodes.py

# Prepare AI input for test nodes
python3 prepare_ai_input.py test 5

# Generate documentation
python3 batch_generate_docs.py test --count 5
```

## Project Structure

```
doc_automation/
├── scan_missing_nodes.py       # Step 1: Scan for missing nodes
├── prepare_ai_input.py         # Step 2: Extract source code & metadata
├── batch_generate_docs.py      # Step 3: Generate docs via AI
├── batch_translate_docs.py     # Translate prepared batches
├── hash_footer.py               # Shared SHA-256 footer + strip helpers (en.md fingerprint)
├── node_source_extract.py       # Imports + preamble + node class (bounded; optional NODE_SOURCE_MAX_CONTEXT_CHARS)
├── version_tracker.py          # Track source code changes
├── doc_rules.txt               # Documentation writing rules
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── QUICK_START.md             # Detailed quick start guide
│
├── ai_input/                   # AI input files (auto-generated)
│   └── <NodeName>/
│       ├── source_code.py
│       ├── basic_info.json
│       └── ai_prompt.txt
│
├── logs/                       # Generation logs
│   └── generation_*.log
│
└── node_versions.json         # Version tracking database
```

## Key Features

### 1. Version Tracking

Every node extraction is tracked with:
- Extraction timestamp
- Source code SHA256 hash
- Code length
- File path and metadata

Check for changes:
```bash
python3 version_tracker.py check
```

View node history:
```bash
python3 version_tracker.py history <NodeName>
```

### 2. Auto-Generated Disclaimer

Every generated document automatically includes:
```markdown
> This documentation was AI-generated. If you find any errors or have 
> suggestions for improvement, please feel free to contribute! 
> [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/<NodeName>/en.md)
```

**Important:** The disclaimer and GitHub link are added by Python code, NOT by AI, ensuring correctness.

English documents (`en.md`) also get a trailing **SHA-256 source fingerprint** footer (derived from the same extracted node class body as `node_versions.json`), so reviewers can verify whether docs match upstream ComfyUI code without relying on local `doc_automation` files. Translators omit this footer; it is stripped before non-English runs.

### 3. Simplified Document Structure

Generated documents contain:
1. **Disclaimer** (auto-added by Python)
2. **Overview** (1-3 sentences about what the node does)
3. **Inputs** (complete parameter table)
4. **Outputs** (output table)

No "Usage Tips" or subjective content to avoid AI hallucinations.

## Configuration

### Node source extraction (optional shell / process env)

| Variable | Notes |
|----------|-------|
| `NODE_SOURCE_EXTRACTION_DEPTH` | Optional preset: `standard` (alias for defaults), `shallow` (no same-file preamble + no cross-file resolve + low iteration budget), `deep` (full preamble + cross-file resolve). Overridable below. |
| `NODE_SOURCE_PREAMBLE_MODE` | `slim` (default): AST-filtered prelude; `full`: entire prelude before the class; `none`: skip same-file prelude (cross-file snippets still follow `NODE_SOURCE_RESOLVE_IMPORTS`). |
| `NODE_SOURCE_IMPORT_MATCH` | `strict` (default): only keep `import a.b` lines when call chains use `a.b…` (avoids unrelated `comfy.*` imports). `broad`: legacy looser matching. |
| `NODE_SOURCE_SLIM_ITERATIONS` | How many passes slim mode uses to grow helper references (integer, 1–32, default `3`). |
| `NODE_SOURCE_RESOLVE_IMPORTS` | Set `1` to append resolved callee snippets under `COMFYUI_PATH` (e.g. `comfy.sd.load_checkpoint_guess_config`). Capped via `NODE_SOURCE_RESOLVE_MAX_CHARS_EACH` (default `6000`) and `NODE_SOURCE_RESOLVE_MAX_FUNCS` (default `8`). |
| `NODE_SOURCE_MAX_CONTEXT_CHARS` | Max total length of the assembled extract (bundle). |
| `COMFYUI_PATH` | Paths must live under here to be resolved into snippets. |

### Environment Variables (.env)

| Variable | Description | Default |
|----------|-------------|---------|
| `DEEPSEEK_API_KEY` | DeepSeek API key | Required |
| `API_BASE_URL` | API base URL | `https://api.deepseek.com` |
| `API_MODEL` | Model to use | `deepseek-chat` |
| `BATCH_SIZE` | Batch size | `5` |
| `MAX_RETRIES` | Max retries on error | `3` |
| `DELAY_BETWEEN_REQUESTS` | Delay in seconds | `2` |

## Commands

### scan_missing_nodes.py

```bash
python3 scan_missing_nodes.py
```

Scans ComfyUI codebase and generates `missing_nodes_report.json`.

**Output:**
- Total nodes: 494
- Documented: 145
- Missing: 401

### prepare_ai_input.py

```bash
# Single node
python3 prepare_ai_input.py node <NodeName>

# First N nodes (test)
python3 prepare_ai_input.py test 10

# All missing nodes
python3 prepare_ai_input.py all
```

**For each node, creates:**
- `ai_input/<NodeName>/source_code.py` - Complete source code
- `ai_input/<NodeName>/basic_info.json` - Metadata + version info
- `ai_input/<NodeName>/ai_prompt.txt` - AI prompt

**Version tracking:**
- Records extraction timestamp
- Calculates source hash
- Detects code changes on re-extraction

### batch_generate_docs.py

```bash
# Test mode (5 nodes)
python3 batch_generate_docs.py test --count 5

# All prepared nodes
python3 batch_generate_docs.py all

# Single node
python3 batch_generate_docs.py node --node <NodeName>

# Resume (only missing docs)
python3 batch_generate_docs.py resume

# Force regenerate
python3 batch_generate_docs.py all --force
```

**Features:**
- Auto-adds disclaimer with correct GitHub link
- Removes AI-generated disclaimer if present (prevents duplication)
- Validates generated content (length, required sections)
- Retry logic with exponential backoff
- Comprehensive logging

### version_tracker.py

```bash
# Check for changed nodes
python3 version_tracker.py check

# View node history
python3 version_tracker.py history <NodeName>

# Show stats
python3 version_tracker.py
```

## Document Quality Standards

### Required:
- ✅ Use tooltip text exactly as provided for parameter descriptions
- ✅ Keep data types in ENGLISH (IMAGE, STRING, INT, FLOAT, etc.)
- ✅ Use backticks for parameter names: `parameter_name`
- ✅ Base descriptions on source code facts
- ✅ Extract docstring for overview

### Prohibited:
- ❌ No "Usage Tips" or best practices sections
- ❌ No emojis
- ❌ No code examples
- ❌ No translated data type names
- ❌ No speculative content

## Workflow

### Phase 1: Test (5-10 nodes)
```bash
python3 prepare_ai_input.py test 10
python3 batch_generate_docs.py test --count 10
# Review quality
```

### Phase 2: Batch Process (100 nodes)
```bash
python3 prepare_ai_input.py test 100
python3 batch_generate_docs.py all
```

### Phase 3: Complete (remaining ~300 nodes)
```bash
python3 prepare_ai_input.py all
python3 batch_generate_docs.py resume
```

## Cost Estimation

Using DeepSeek API:
- ~¥0.001/1K tokens
- Each node: ~3K tokens (2K prompt + 1K response)
- 401 nodes total: ~1.2M tokens ≈ ¥1.2

## Logs

View generation logs:
```bash
tail -f logs/generation_*.log
```

Log format:
```
[2025-10-09 23:21:18] [INFO] 🤖 正在生成文档: AddNoise
[2025-10-09 23:21:34] [SUCCESS] ✅ 成功生成: AddNoise
```

## Troubleshooting

### API Key Error
```
❌ 未找到 DEEPSEEK_API_KEY
```
**Solution:** Check `../.env` file exists and contains valid API key.

### Rate Limiting (429 Error)
**Solution:** Increase delay in `.env`:
```bash
DELAY_BETWEEN_REQUESTS=5
BATCH_SIZE=3
```

### Incomplete Documentation
**Solution:** Check logs for errors:
```bash
grep "ERROR" logs/generation_*.log
```

## Version Tracking Details

### Database Structure (`node_versions.json`)

```json
{
  "nodes": {
    "NodeName": {
      "versions": [
        {
          "node_name": "NodeName",
          "extracted_at": "2025-10-09T23:00:00",
          "source_hash": "abc123...",
          "source_length": 1234,
          "metadata": {
            "file_path": "comfy_extras/nodes_x.py",
            "node_type": "new_api",
            "class_name": "NodeClass"
          }
        }
      ],
      "current_hash": "abc123...",
      "last_updated": "2025-10-09T23:00:00"
    }
  },
  "last_scan": "2025-10-09T23:00:00"
}
```

### Use Cases

1. **Detect Updates:** Run periodic scans to find nodes with changed source code
2. **Audit Trail:** View complete history of when nodes were extracted
3. **Selective Regeneration:** Only regenerate docs for changed nodes

## Next Steps

1. ✅ Test with 5-10 nodes
2. ✅ Verify quality
3. ⏳ Batch generate all 401 nodes
4. ⏳ Manual review of critical nodes
5. ⏳ Multi-language translation (future)

## Contributing

All code uses English comments for collaboration. If you find any Chinese comments, feel free to translate them.

## License

Same as main project.
