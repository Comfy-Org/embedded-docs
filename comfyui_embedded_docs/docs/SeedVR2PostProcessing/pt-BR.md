# SeedVR2PostProcessing

Este nó alinha a imagem gerada com a imagem redimensionada original e aplica correção de cor opcional. Ele recebe a saída de um processo de upscaling SeedVR2 e a ajusta para corresponder às cores e dimensões da imagem de referência original.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
|-----------|-----------|--------------|-------------|-------|
| `images` | A imagem gerada a ser processada. | IMAGE | Sim | - |
| `original_resized_images` | A imagem redimensionada original antes do pré-processamento, usada como referência. | IMAGE | Sim | - |
| `color_correction_method` | Método para corresponder as cores da imagem gerada à imagem original. lab: transfere cor no espaço CIELAB, preservando detalhes (mais fiel). wavelet: transfere cor de baixa frequência, mantendo detalhes de alta frequência do upscaling. adain: corresponde média/desvio padrão por canal (mais rápido, tonalidade global). none: pula transferência de cor (apenas alinhamento geométrico). (padrão: "lab") | COMBO | Sim | `"lab"`<br>`"wavelet"`<br>`"adain"`<br>`"none"` |

**Nota:** As entradas `images` e `original_resized_images` devem ter dimensões correspondentes. Se a imagem original tiver um canal alfa (4 canais), ele será preservado e aplicado à saída.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-----------|--------------|
| `images` | A imagem processada com correção de cor aplicada e dimensões alinhadas à imagem de referência. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2PostProcessing/pt-BR.md)

---
**Source fingerprint (SHA-256):** `befbe8ccd591c8064a07ae4bb8df853c7ce10f3de83ebfa9214755c22faf28b0`
