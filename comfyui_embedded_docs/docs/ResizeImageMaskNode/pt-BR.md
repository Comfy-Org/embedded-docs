O nó Redimensionar Imagem/Máscara fornece múltiplos métodos para alterar as dimensões de uma imagem ou máscara de entrada. Ele pode escalar por um multiplicador, definir dimensões específicas, igualar o tamanho de outra entrada ou ajustar com base na contagem de pixels, utilizando vários métodos de interpolação para qualidade.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `entrada` | A imagem ou máscara a ser redimensionada. | IMAGE ou MASK | Sim | N/A |
| `tipo_de_redimensionamento` | O método usado para determinar o novo tamanho. Os parâmetros obrigatórios mudam conforme o tipo selecionado. | COMBO | Sim | `SCALE_BY`<br>`SCALE_DIMENSIONS`<br>`SCALE_LONGER_DIMENSION`<br>`SCALE_SHORTER_DIMENSION`<br>`SCALE_WIDTH`<br>`SCALE_HEIGHT`<br>`SCALE_TOTAL_PIXELS`<br>`MATCH_SIZE` |
| `multiplier` | O fator de escala. Obrigatório quando `tipo_de_redimensionamento` é `SCALE_BY` (padrão: 1,00). | FLOAT | Não | 0,01 a 8,0 |
| `width` | A largura alvo em pixels. Obrigatório quando `tipo_de_redimensionamento` é `SCALE_DIMENSIONS` ou `SCALE_WIDTH` (padrão: 512). | INT | Não | 0 a 8192 |
| `height` | A altura alvo em pixels. Obrigatório quando `tipo_de_redimensionamento` é `SCALE_DIMENSIONS` ou `SCALE_HEIGHT` (padrão: 512). | INT | Não | 0 a 8192 |
| `crop` | O método de corte a ser aplicado quando as dimensões não correspondem à proporção. Disponível apenas quando `tipo_de_redimensionamento` é `SCALE_DIMENSIONS` ou `MATCH_SIZE` (padrão: "center"). | COMBO | Não | `"disabled"`<br>`"center"` |
| `longer_size` | O tamanho alvo para o lado mais longo da imagem. Obrigatório quando `tipo_de_redimensionamento` é `SCALE_LONGER_DIMENSION` (padrão: 512). | INT | Não | 0 a 8192 |
| `shorter_size` | O tamanho alvo para o lado mais curto da imagem. Obrigatório quando `tipo_de_redimensionamento` é `SCALE_SHORTER_DIMENSION` (padrão: 512). | INT | Não | 0 a 8192 |
| `megapixels` | O número total alvo de megapixels. Obrigatório quando `tipo_de_redimensionamento` é `SCALE_TOTAL_PIXELS` (padrão: 1,0). | FLOAT | Não | 0,01 a 16,0 |
| `match` | Uma imagem ou máscara cujas dimensões a entrada será redimensionada para corresponder. Obrigatório quando `tipo_de_redimensionamento` é `MATCH_SIZE`. | IMAGE ou MASK | Não | N/A |
| `método_de_escala` | O algoritmo de interpolação usado para escalonamento (padrão: "area"). | COMBO | Sim | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"lanczos"` |

**Nota:** O parâmetro `crop` está disponível e é relevante apenas quando o `resize_type` está definido como `SCALE_DIMENSIONS` ou `MATCH_SIZE`. Ao usar `SCALE_WIDTH` ou `SCALE_HEIGHT`, a outra dimensão é automaticamente escalada para manter a proporção original.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `resized` | A imagem ou máscara redimensionada, correspondendo ao tipo de dados da entrada. | IMAGE ou MASK |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImageMaskNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `9ac0b153608ac971bb11d9d12ebd1f0f4d6e926604e8727a1bc3a311d95fbc03`
