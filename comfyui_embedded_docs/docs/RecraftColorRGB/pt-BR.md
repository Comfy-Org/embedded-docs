> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftColorRGB/pt-BR.md)

Crie uma cor Recraft especificando valores individuais de vermelho, verde e azul. Este nó recebe valores inteiros RGB (0-255) e os converte em um formato de cor Recraft que pode ser usado em outras operações Recraft. Você também pode, opcionalmente, fornecer uma cadeia de cores Recraft existente para estendê-la com a nova cor.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `r` | INT | Sim | 0-255 | Valor vermelho da cor (padrão: 0) |
| `g` | INT | Sim | 0-255 | Valor verde da cor (padrão: 0) |
| `b` | INT | Sim | 0-255 | Valor azul da cor (padrão: 0) |
| `recraft_color` | COLOR | Não | - | Cadeia de cores Recraft existente opcional para estender com a nova cor RGB |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `recraft_color` | COLOR | O objeto de cor Recraft criado contendo os valores RGB especificados, ou a cadeia de cores estendida se uma existente foi fornecida |

---
**Source fingerprint (SHA-256):** `8c3503632d085fa4c1771f92f17008b7b051e9604d9e7d1e7d352cbbbd22dddc`
