# Recraft Cor RGB

Crie uma cor Recraft especificando valores individuais de vermelho, verde e azul. Este nó recebe valores inteiros RGB (0-255) e os converte em um formato de cor Recraft que pode ser usado em outras operações Recraft. Você também pode, opcionalmente, fornecer uma cadeia de cores Recraft existente para estendê-la com a nova cor.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `r` | Valor vermelho da cor (padrão: 0) | INT | Sim | 0-255 |
| `g` | Valor verde da cor (padrão: 0) | INT | Sim | 0-255 |
| `b` | Valor azul da cor (padrão: 0) | INT | Sim | 0-255 |
| `recraft_color` | Cadeia de cores Recraft existente opcional para estender com a nova cor RGB | COLOR | Não | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `recraft_color` | O objeto de cor Recraft criado contendo os valores RGB especificados, ou a cadeia de cores estendida se uma existente foi fornecida | COLOR |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftColorRGB/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8c3503632d085fa4c1771f92f17008b7b051e9604d9e7d1e7d352cbbbd22dddc`
