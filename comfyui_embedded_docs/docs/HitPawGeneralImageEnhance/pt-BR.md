# HitPaw General Image Enhance

Este nó melhora imagens de baixa resolução, ampliando-as para super-resolução, removendo artefatos e ruído. Ele utiliza uma API externa para processar a imagem e pode ajustar automaticamente o tamanho da entrada para permanecer dentro dos limites de processamento. O tamanho máximo permitido para a saída é de 32 megapixels.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `modelo` | O modelo de aprimoramento a ser usado. O modelo `generative_portrait` é otimizado para retratos, enquanto `generative` é um modelo de uso geral. | COMBO | Sim | `"generative_portrait"`<br>`"generative"` |
| `imagem` | A imagem de entrada a ser aprimorada. | IMAGE | Sim | - |
| `fator_de_upscale` | O fator pelo qual as dimensões da imagem serão ampliadas. Um fator de 1 significa nenhuma ampliação, 2 dobra as dimensões e 4 quadruplica. | COMBO | Sim | `1`<br>`2`<br>`4` |
| `auto_redimensionar` | Reduzir automaticamente a escala da imagem de entrada se a saída exceder o limite. (padrão: `False`) | BOOLEAN | Não | - |

**Nota:** O nó gera um erro se o tamanho de saída calculado (largura da entrada × fator de ampliação × altura da entrada × fator de ampliação) exceder 32.000.000 pixels (32MP) e `auto_downscale` estiver desabilitado. Quando `auto_downscale` está habilitado, o nó reduz automaticamente o tamanho da imagem de entrada ou o fator de ampliação (ou ambos) para que a saída caiba dentro do limite de 32MP.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `image` | A imagem de saída aprimorada e ampliada. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HitPawGeneralImageEnhance/pt-BR.md)

---
**Source fingerprint (SHA-256):** `eb9adc1ac94c5fb943e3dd8f6617b21c5d3203f0d9ddb93ba1c9d4b4e63bd421`
