#!/bin/bash
cd /Users/linmoumou/Documents/embedded-docs/comfyui_embedded_docs/docs/OpenAIGPTImageNodeV2
for f in *.md; do
  lang="${f%.md}"
  echo "$lang: $(grep -c 'transparent' "$f")"
done
