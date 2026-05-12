# ComfyUI Node Documentation Generation Workflow

## 📋 Full Workflow Overview

```
1. Scan for missing nodes → 2. Extract node information → 3. AI generates documentation → 4. Manual review → 5. Multilingual translation
```

---

## Step 1: Scan for Missing Node Documentation

**Script:** `scan_missing_nodes.py`

**Function:**
- Scan all nodes in the ComfyUI codebase
- Compare with existing documentation to find undocumented nodes
- Generate a detailed report

**How to use:**
```bash
python3 scan_missing_nodes.py
```

**Output File:**
- `missing_nodes_report.json` – Contains detailed information about all missing node docs

**Report Contents:**
- Total node count, documented count, missing documentation count
- Each missing node’s name, file path, type (new_api/classic)
- Potentially deprecated documentation list
- Documentation language completeness check

---

## Step 2: Prepare AI Input

**Script:** `prepare_ai_input.py`

**Function:**
- Extract the complete source code for each node
- Extract docstring, category, tooltip, and other metadata
- Generate structured prompts for the AI

**How to use:**
```bash
# Prepare a single node
python3 prepare_ai_input.py node <node_name>

# Prepare the first N nodes (test)
python3 prepare_ai_input.py test 10

# Prepare all missing nodes
python3 prepare_ai_input.py all
```

**Output Structure:**
```
ai_input/
├── <node_name>/
│   ├── source_code.py      # Full source code
│   ├── basic_info.json     # Extracted metadata
│   └── ai_prompt.txt       # AI prompt
└── batch_nodes.json        # Batch node list
```

**Extracted information includes:**
- ✅ Full class source code
- ✅ Class docstring
- ✅ CATEGORY (node category)
- ✅ DESCRIPTION
- ✅ All INPUT_TYPES (including tooltips)
- ✅ RETURN_TYPES and RETURN_NAMES

---

## Step 3: AI Generates Documentation

### Method A: Manual AI Generation (Recommended for important nodes)

1. Open `ai_input/<node_name>/ai_prompt.txt`
2. Copy the full prompt
3. Submit to an AI (Claude, ChatGPT, etc.)
4. AI generates the full documentation according to the source and the rules
5. Save to `comfyui_embedded_docs/docs/<node_name>/en.md`

### Method B: Batch AI Processing (Recommended for large numbers of nodes)

Use an AI API for batch processing:

```python
# Example: Generate documentation in batch using OpenAI API
import openai
import json
from pathlib import Path

ai_input = Path("ai_input")
for node_dir in ai_input.iterdir():
    if node_dir.is_dir():
        prompt_file = node_dir / "ai_prompt.txt"
        with open(prompt_file) as f:
            prompt = f.read()
        
        # Call AI API
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        
        # Save the generated documentation
        doc_content = response.choices[0].message.content
        output_file = f"comfyui_embedded_docs/docs/{node_dir.name}/en.md"
        # Save...
```

---

## Step 4: Manual Review and Optimization

**Review Checklist:**

- [ ] Is the function description accurate and concise?
- [ ] Is the working principle easy to understand?
- [ ] Is the parameter table complete (all parameters explained)?
- [ ] Are data types kept in uppercase English?
- [ ] Are usage suggestions practical?
- [ ] Is any important information missing?

**Optimization Focus:**
- Core nodes: Add more detailed working principles and usage scenarios
- API nodes: Add API configuration details and caveats
- Complex nodes: Add real examples or workflow screenshots

---

## Step 5: Multilingual Translation

**To-do Functionality:**

You can create translation scripts to generate other language versions based on en.md:
- zh.md (Chinese)
- es.md (Spanish)
- fr.md (French)
- ja.md (Japanese)
- ko.md (Korean)
- ru.md (Russian)

**Translation Rules:**
- ✅ Translate parameter names and descriptions
- ❌ Keep data types in English
- ✅ Use standardized section titles (see doc_rules.txt)

---

## 📊 Current Status

Based on the latest scan:
- **Total nodes:** 494
- **Documented:** 145 (29.4%)
- **Missing docs:** 401 (81.2%)
- **Need update:** 121 (missing language version)

---

## 🎯 Recommended Processing Order

### Priority 1: High-frequency Core Nodes (~30 nodes)
Manual review with AI assistance to ensure high-quality documentation
- CheckpointLoader
- KSampler
- VAEEncode/Decode
- CLIPTextEncode
- And other commonly used nodes

### Priority 2: API Integration Nodes (~100 nodes)
Batch AI generation with manual spot checks
- OpenAI series
- Flux series
- Various API nodes

### Priority 3: Utility & Helper Nodes (~270 nodes)
Batch AI generates basic versions
- String operations
- Math operations
- Tool-type nodes

---

## 🛠️ Quick Command Reference

```bash
# 1. Scan for missing nodes
python3 scan_missing_nodes.py

# 2. Prepare AI input for a single node
python3 prepare_ai_input.py node OpenAIDalle2

# 3. Batch prepare the first 50 nodes
python3 prepare_ai_input.py test 50

# 4. Prepare all missing nodes (401)
python3 prepare_ai_input.py all

# 5. List generated files
ls -R ai_input/
```

---

## 📝 File Descriptions

| File | Purpose |
|------|---------|
| `scan_missing_nodes.py` | Scans and reports missing node documentation |
| `prepare_ai_input.py`  | Extracts node source code and metadata, prepares AI input |
| `generate_docs.py`     | Auto-generates basic doc frameworks (limited details) |
| `doc_rules.txt`        | Documentation writing rules and format requirements |
| `missing_nodes_report.json` | Detailed missing nodes report |
| `ai_input/`            | Directory for AI input files |
| `WORKFLOW.md`          | This workflow explanation file |

---

## ✅ Next Steps

1. **Immediate actions:**
   - Use `prepare_ai_input.py test 10` to prep 10 nodes
   - Manually submit `ai_prompt.txt` to the AI to generate documentation
   - Review documentation quality

2. **Short-term goals:**
   - Complete high-quality docs for 30 core nodes
   - Validate AI generation quality
   - Optimize prompt template

3. **Long-term goals:**
   - Build AI API batch workflow
   - Complete basic docs for all 401 nodes
   - Add all language versions

