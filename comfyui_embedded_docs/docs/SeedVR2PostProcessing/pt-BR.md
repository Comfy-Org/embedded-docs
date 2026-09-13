# Pós-processar saída SeedVR2

Este nó alinha a imagem gerada com a imagem redimensionada original e aplica correção de cor opcional. Ele recebe a saída de um processo de upscaling do SeedVR2 e a ajusta para corresponder às cores e dimensões da imagem de referência original.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `images` | A imagem gerada a ser processada. | IMAGE | Sim | - |
| `original_resized_images` | A imagem redimensionada original antes do pré-processamento, usada como referência. | IMAGE | Sim | - |
| `color_correction_method` | Método para corresponder as cores da imagem gerada às da imagem original. lab: transfere a cor no espaço CIELAB, preservando detalhes (mais fiel). wavelet: transfere a cor de baixa frequência, mantendo os detalhes de alta frequência do upscaling. adain: corresponde à média/desvio padrão por canal (mais rápido, tonalidade global). none: ignora a transferência de cor (apenas alinhamento geométrico). (padrão: "lab") | COMBO | Sim | `"lab"`<br>`"wavelet"`<br>`"adain"`<br>`"none"` |

**Observação:** Ambas as entradas podem ser tensores 4-D (batch, height, width, channels) ou 5-D (batch, frames, height, width, channels). O nó recorta ambas para o menor batch, contagem de frames, altura e largura, então elas não precisam corresponder exatamente. Quando um método de correção de cor diferente de `none` é usado, a imagem de referência é redimensionada primeiro para o tamanho da saída. A correção de cor é processada em blocos que levam a memória em consideração, reduzindo para um tamanho de bloco menor se a memória se esgotar. A altura e a largura da saída são arredondadas para baixo para números pares. Se a imagem de referência tiver um canal alfa (4 canais), esse canal alfa é preservado e aplicado à saída.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `images` | A imagem alinhada e com correção de cor. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2PostProcessing/pt-BR.md)

---
**Source fingerprint (SHA-256):** `00a3a3ef06edc7e0eca8f67a96095920a3e0e885dac3fb676d081e4c4c30bec5`
