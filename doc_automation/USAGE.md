# Quick Usage Guide

## ✅ System Ready!

Your documentation automation system is fully configured and tested.

### Current Status
- Total nodes: 494
- Documented: 168
- Missing: 378
- API: DeepSeek (configured ✅)

## Generate Documentation

### Single Command - Generate N Nodes

```bash
cd doc_automation
conda activate LLM_base
python3 main.py --count <N>
```

**Example:**
```bash
# Generate 10 nodes
python3 main.py --count 10

# Generate 50 nodes
python3 main.py --count 50

# Generate all remaining nodes
python3 main.py --mode all
```

### What It Does Automatically

1. **Scans** ComfyUI for missing documentation
2. **Prepares** AI input (source code + metadata)
3. **Generates** documentation with AI
4. **Updates** all reports (missing_nodes_report.json, node_versions.json)

### Features

✅ **Smart Skip:** Only generates missing docs (no duplicates)  
✅ **Version Tracking:** Records source code hash & timestamp  
✅ **Auto-Links:** Adds GitHub link automatically  
✅ **Constraint Detection:** AI analyzes code for parameter limits  
✅ **Progress Logs:** Detailed logs in `logs/` directory

## View Results

```bash
# Check generated docs
ls -lt ../comfyui_embedded_docs/docs/ | head -20

# View specific doc
cat ../comfyui_embedded_docs/docs/ByteDanceTextToVideoNode/en.md

# Check latest log
tail -f logs/generation_*.log
```

## Status Commands

```bash
# Check configuration
python3 check_config.py

# View missing nodes count
grep "缺失文档的节点数" missing_nodes_report.json

# View version database
python3 version_tracker.py
```

## Advanced Usage

### Force Regenerate Specific Node
```bash
python3 main.py --mode node --node AudioEncoderLoader --force
```

### Continue from Where You Left Off
```bash
python3 main.py --mode resume
```

### Only Scan (No Generation)
```bash
python3 main.py --scan-only
```

## Documentation Quality

Each generated document includes:
1. AI-generated disclaimer with GitHub link (auto-added by Python)
2. Overview (what the node does)
3. Inputs table (with parameter constraints if applicable)
4. Outputs table

**Example Constraint Documentation:**
```markdown
**Parameter Constraints:**
- The `image` parameter accepts 1-10 images maximum
- When `image` and `mask` are both provided, switches to editing mode
- The `duration` parameter is limited to 3-12 seconds
```

## Next Steps

### Generate All Remaining Docs (~378 nodes)

```bash
# Estimate: ~40 minutes, cost ~¥1.2

# Option 1: All at once
python3 main.py --mode all

# Option 2: In batches
python3 main.py --count 100  # First batch
python3 main.py --count 100  # Second batch
python3 main.py --mode resume  # Remaining

# Option 3: Resume anytime
python3 main.py --mode resume
```

### Cost & Time Estimate
- Per node: ~3K tokens, ~3 seconds
- 378 nodes: ~1.2M tokens, ~20 minutes
- DeepSeek cost: ~¥1.2

## Troubleshooting

### Rate Limit Error
Edit `../.env`:
```bash
DELAY_BETWEEN_REQUESTS=5
BATCH_SIZE=3
```

### Check API Connection
```bash
python3 check_config.py
```

### View Errors
```bash
grep "ERROR" logs/generation_*.log
```

---

**Ready to generate all 378 remaining docs?**  
Just run: `python3 main.py --mode all`

