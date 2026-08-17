# Pós-processar saída SeedVR2

Este nó alinha a imagem gerada com a imagem redimensionada original e aplica correção de cor opcional. Ele recebe a saída de um processo de upscaling SeedVR2 e a ajusta para corresponder às cores e dimensões da imagem de referência original.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `images` | A imagem gerada a ser processada. | IMAGE | Sim | - |
| `original_resized_images` | A imagem redimensionada original antes do pré-processamento, usada como referência. | IMAGE | Sim | - |
| `color_correction_method` | Método para fazer as cores da imagem gerada corresponderem às da imagem original. lab: transferir cor no espaço CIELAB, preservando detalhes (mais fiel). wavelet: transferir cor de baixa frequência, mantendo detalhes de alta frequência do upscaling. adain: corresponder média/desvio padrão por canal (mais rápido, tom global). none: pular transferência de cor (somente alinhamento geométrico). (padrão: "lab") | COMBO | Sim | `"lab"`<br>`"wavelet"`<br>`"adain"`<br>`"none"` |

**Observação:** A saída é cortada para a menor altura e largura entre as imagens gerada e de referência, e as dimensões finais são arredondadas para baixo até números pares. Se a imagem de referência tiver um canal alfa (4 canais), ele é preservado e aplicado à saída. Ambas as entradas podem ser tensores de imagem 4D ou 5D, e a saída usa a mesma dimensionalidade da entrada da imagem gerada.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `images` | A imagem alinhada e com correção de cor. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2PostProcessing/pt-BR.md)

---
**Source fingerprint (SHA-256):** `00a3a3ef06edc7e0eca8f67a96095920a3e0e885dac3fb676d081e4c4c30bec5`
