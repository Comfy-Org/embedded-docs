> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HitPawGeneralImageEnhance/pt-BR.md)

Este nó melhora imagens de baixa resolução, aumentando-as para super-resolução, removendo artefatos e ruídos. Ele utiliza uma API externa para processar a imagem e pode ajustar automaticamente o tamanho da entrada para permanecer dentro dos limites de processamento. O tamanho máximo permitido para a saída é de 4 megapixels.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `modelo` | STRING | Sim | `"generative_portrait"`<br>`"generative"` | O modelo de aprimoramento a ser usado. O modelo `generative_portrait` é otimizado para retratos, enquanto `generative` é um modelo de uso geral. |
| `imagem` | IMAGE | Sim | - | A imagem de entrada a ser aprimorada. |
| `fator_de_upscale` | INT | Sim | `1`<br>`2`<br>`4` | O fator pelo qual aumentar as dimensões da imagem. Um fator de 1 significa sem aumento, 2 dobra as dimensões e 4 quadruplica. |
| `auto_redimensionar` | BOOLEAN | Não | - | Redimensionar automaticamente a imagem de entrada se a saída exceder o limite. Quando ativado, o nó tentará reduzir o tamanho da imagem de entrada para caber no limite de saída de 4 megapixels antes de aplicar o fator de aumento solicitado. (padrão: `False`) |

**Nota:** O nó gerará um erro se o tamanho de saída calculado (altura da entrada × fator de aumento × largura da entrada × fator de aumento) exceder 4.000.000 pixels (4MP) e `auto_downscale` estiver desativado. Quando `auto_downscale` estiver ativado, o nó tentará reduzir a imagem de entrada para caber no limite antes de aplicar o fator de aumento solicitado. Se for necessário reduzir em mais de 2x, o nó reduzirá o fator de aumento.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `imagem` | IMAGE | A imagem de saída aprimorada e ampliada. |

---
**Source fingerprint (SHA-256):** `29f927d39777acdfba2aad107027672d281c202ec78e04942e405c2cc64fcee4`
