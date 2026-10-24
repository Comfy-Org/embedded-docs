# Ideogram Vector Image to SVG

Este nó converte uma imagem em um SVG editável com o Ideogram Vector. O resultado é marcação vetorial em vez de uma imagem raster, portanto, as formas traçadas permanecem editáveis em um editor vetorial. Áreas transparentes de uma imagem com alpha permanecem transparentes.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modelo a ser usado. Padrão: `"ideogram-vector-1"`. | DYNAMIC_COMBO | Sim | `"ideogram-vector-1"` |
| `image` | A imagem a ser convertida. Uma entrada em lote é convertida imagem por imagem e os SVGs resultantes são retornados juntos. | IMAGE | Sim | - |
| `mode` | `"simple"` traça menos formas e maiores; `"default"` mantém detalhes mais finos. Padrão: `"default"`. | COMBO | Sim | `"simple"`<br>`"default"` |

**Restrições:**

* Imagens cujo lado mais longo tenha mais de 2048 pixels são reduzidas antes do upload.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `SVG` | A imagem convertida como marcação vetorial editável. | SVG |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramVectorImageToSVGApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `6553291e9d887b31485b9cbf8f6ced4186470eb47e8621ebb0f4e5df6542123e`
