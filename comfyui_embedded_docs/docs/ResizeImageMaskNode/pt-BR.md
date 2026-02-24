> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImageMaskNode/pt-BR.md)

O nó Redimensionar Imagem/Máscara fornece múltiplos métodos para alterar as dimensões de uma imagem ou máscara de entrada. Ele pode dimensionar por um multiplicador, definir dimensões específicas, corresponder ao tamanho de outra entrada ou ajustar com base na contagem de pixels, utilizando vários métodos de interpolação para qualidade.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `input` | IMAGE ou MASK | Sim | N/A | A imagem ou máscara a ser redimensionada. |
| `resize_type` | COMBO | Sim | `SCALE_BY`<br>`SCALE_DIMENSIONS`<br>`SCALE_LONGER_DIMENSION`<br>`SCALE_SHORTER_DIMENSION`<br>`SCALE_WIDTH`<br>`SCALE_HEIGHT`<br>`SCALE_TOTAL_PIXELS`<br>`MATCH_SIZE` | O método usado para determinar o novo tamanho. Os parâmetros necessários mudam com base no tipo selecionado. |
| `multiplier` | FLOAT | Não | 0.01 a 8.0 | O fator de escala. Obrigatório quando `resize_type` é `SCALE_BY` (padrão: 1.00). |
| `width` | INT | Não | 0 a 8192 | A largura alvo em pixels. Obrigatório quando `resize_type` é `SCALE_DIMENSIONS` ou `SCALE_WIDTH` (padrão: 512). |
| `height` | INT | Não | 0 a 8192 | A altura alvo em pixels. Obrigatório quando `resize_type` é `SCALE_DIMENSIONS` ou `SCALE_HEIGHT` (padrão: 512). |
| `crop` | COMBO | Não | `"disabled"`<br>`"center"` | O método de corte a ser aplicado quando as dimensões não correspondem à proporção. Disponível apenas quando `resize_type` é `SCALE_DIMENSIONS` ou `MATCH_SIZE` (padrão: "center"). |
| `longer_size` | INT | Não | 0 a 8192 | O tamanho alvo para o lado mais longo da imagem. Obrigatório quando `resize_type` é `SCALE_LONGER_DIMENSION` (padrão: 512). |
| `shorter_size` | INT | Não | 0 a 8192 | O tamanho alvo para o lado mais curto da imagem. Obrigatório quando `resize_type` é `SCALE_SHORTER_DIMENSION` (padrão: 512). |
| `megapixels` | FLOAT | Não | 0.01 a 16.0 | O número total alvo de megapixels. Obrigatório quando `resize_type` é `SCALE_TOTAL_PIXELS` (padrão: 1.0). |
| `match` | IMAGE ou MASK | Não | N/A | Uma imagem ou máscara cujas dimensões a entrada será redimensionada para corresponder. Obrigatório quando `resize_type` é `MATCH_SIZE`. |
| `scale_method` | COMBO | Sim | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"lanczos"` | O algoritmo de interpolação usado para o dimensionamento (padrão: "area"). |

**Observação:** O parâmetro `crop` está disponível e é relevante apenas quando o `resize_type` está definido como `SCALE_DIMENSIONS` ou `MATCH_SIZE`. Ao usar `SCALE_WIDTH` ou `SCALE_HEIGHT`, a outra dimensão é automaticamente escalonada para manter a proporção original.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `resized` | IMAGE ou MASK | A imagem ou máscara redimensionada, correspondendo ao tipo de dados da entrada. |
