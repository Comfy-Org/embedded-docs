# HitPaw General Image Enhance

Este nó aprimora imagens de baixa resolução ao aumentá-las para super-resolução, removendo artefatos e ruído. Ele envia a imagem para uma API externa para processamento e pode ajustar automaticamente o tamanho da entrada para permanecer dentro do limite de saída permitido. O tamanho máximo de saída permitido é 32 megapixels.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo de aprimoramento a ser usado. O modelo `generative_portrait` é otimizado para retratos, enquanto `generative` é um modelo de uso geral. | COMBO | Sim | `"generative_portrait"`<br>`"generative"` |
| `image` | A imagem de entrada a ser aprimorada. | IMAGE | Sim | - |
| `upscale_factor` | O fator pelo qual aumentar as dimensões da imagem. Um fator de 1 significa sem aumento, 2 dobra as dimensões e 4 as quadruplica. | COMBO | Sim | `1`<br>`2`<br>`4` |
| `auto_downscale` | Reduz automaticamente a escala da imagem de entrada se a saída exceder o limite. (padrão: `False`) | BOOLEAN | Não | - |

**Observação:** O nó gera um erro se o tamanho de saída calculado (largura de entrada × upscale_factor × altura de entrada × upscale_factor) exceder 32.000.000 pixels (32MP) e `auto_downscale` estiver desabilitado. Quando `auto_downscale` está habilitado, o nó reduz automaticamente o tamanho da imagem de entrada ou o fator de upscale (ou ambos) para que a saída caiba dentro do limite de 32MP. O `model` e o `upscale_factor` selecionados são combinados no nome do modelo enviado ao serviço.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `image` | A imagem de saída aprimorada e ampliada. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HitPawGeneralImageEnhance/pt-BR.md)

---
**Source fingerprint (SHA-256):** `eb9adc1ac94c5fb943e3dd8f6617b21c5d3203f0d9ddb93ba1c9d4b4e63bd421`
