#!/bin/bash
cd /Users/linmoumou/Documents/embedded-docs
D=comfyui_embedded_docs/docs
echo "--- a. markdown fences:"; grep -rl '```markdown' $D/OpenAIGPTImage1/ $D/OpenAIGPTImageNodeV2/ | wc -l
echo "--- b. translated type names:"; grep -rEn '\| (MODELO|CADENA|IMAGEN|IMAGEM|МОДЕЛЬ|СТРОКА|ИЗОБРАЖЕНИЕ|CHAÎNE|FLOTTANT|ENTIER|モデル|画像|模型|图像|文字列) \|' $D/OpenAIGPTImage1/ $D/OpenAIGPTImageNodeV2/ | wc -l
echo "--- c. Required yes residue:"; grep -rn '| Yes |' $D/OpenAIGPTImage1/*.md $D/OpenAIGPTImageNodeV2/*.md | grep -v en.md | wc -l
echo "--- c2. Range 'to N' residue:"; grep -rn ' to [0-9]' $D/OpenAIGPTImage1/*.md $D/OpenAIGPTImageNodeV2/*.md | grep -v en.md | wc -l
echo "--- e. double H1:"; grep -rn '^## ##' $D/OpenAIGPTImage1/*.md $D/OpenAIGPTImageNodeV2/*.md | wc -l
echo "--- H1 count per file:"
for f in $D/OpenAIGPTImage1/*.md $D/OpenAIGPTImageNodeV2/*.md; do echo "$(grep -c '^# ' $f) $f"; done
