# Pad Image

Adiciona preenchimento a uma imagem com uma cor sólida ou uma cópia espelhada de suas bordas. O preenchimento pode ser definido como pixels exatos em cada lado, como um multiplicador de tamanho ou como a menor quantidade que torna a largura e a altura divisíveis por um número, o que é útil antes de salvar ou criar mosaicos. A imagem original mantém seu lugar: o preenchimento de `left` e `top` é adicionado antes dela, e o de `right` e `bottom`, depois dela.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `image` | A imagem à qual adicionar preenchimento. | IMAGE | Sim | - |
| `padding_type` | Quanto preenchimento adicionar: `"pad dimensions"` para quantidades exatas por lado, `"pad by multiplier"` para um tamanho de saída relativo à entrada, ou `"pad to multiple"` para alcançar o próximo múltiplo. Selecionar uma opção revela seus parâmetros. | DYNAMIC_COMBO | Sim | `"pad dimensions"`<br>`"pad by multiplier"`<br>`"pad to multiple"` |
| `left` | Pixels a adicionar à esquerda. Disponível quando `padding_type` é `"pad dimensions"` (padrão: 0). | INT | Sim | 0 a 16384 |
| `top` | Pixels a adicionar no topo. Disponível quando `padding_type` é `"pad dimensions"` (padrão: 0). | INT | Sim | 0 a 16384 |
| `right` | Pixels a adicionar à direita. Disponível quando `padding_type` é `"pad dimensions"` (padrão: 0). | INT | Sim | 0 a 16384 |
| `bottom` | Pixels a adicionar na parte inferior. Disponível quando `padding_type` é `"pad dimensions"` (padrão: 0). | INT | Sim | 0 a 16384 |
| `multiplier` | Tamanho de saída relativo à entrada; por exemplo, 1.5 adiciona 25% em cada lado. O preenchimento é dividido igualmente entre lados opostos. Disponível quando `padding_type` é `"pad by multiplier"` (padrão: 1.0). | FLOAT | Sim | 1.0 a 8.0 (passo: 0.01) |
| `multiple` | Adiciona preenchimento para que a largura e a altura sejam divisíveis por este número. O preenchimento é dividido igualmente entre lados opostos, com o pixel extra indo para a direita e para a parte inferior. Disponível quando `padding_type` é `"pad to multiple"` (padrão: 32). | INT | Sim | 1 a 16384 |
| `padding_style` | Com o que preencher a área de preenchimento: `"color"` ou `"mirror image"`. Selecionar uma opção revela seus parâmetros. | DYNAMIC_COMBO | Sim | `"color"`<br>`"mirror image"` |
| `color` | Cor de preenchimento da área preenchida; alfa é ignorado. Disponível quando `padding_style` é `"color"` (padrão: `"#000000"`). | COLOR | Sim | - |
| `feathering` | Mistura esta quantidade de pixels da borda da imagem à cor de preenchimento nos lados preenchidos. 0 deixa uma borda dura. Disponível quando `padding_style` é `"color"` (padrão: 0). | INT | Sim | 0 a 16384 |

`"mirror image"` reflete as bordas da imagem em vez de preenchê-las com uma cor. O pixel da borda não é repetido e, quando o preenchimento é mais largo ou mais alto que a própria imagem, a imagem espelhada se repete para cobrir o restante. Quando todos os valores de preenchimento resultam em 0, a imagem de entrada é retornada inalterada.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `image` | A imagem com preenchimento, com a dimensão de lote e o número de canais da entrada. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PadImageNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `9373cd6aa287befba74374b9b2a6c38b20344b5715e9aaa4cf49282ae930c91d`
