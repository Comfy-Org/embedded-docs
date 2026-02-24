> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftColorRGB/pt-BR.md)

Crie uma Cor Recraft escolhendo valores RGB específicos. Este nó permite definir uma cor especificando valores individuais de vermelho, verde e azul, que são então convertidos em um formato de cor Recraft que pode ser usado em outras operações Recraft.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `r` | INT | Sim | 0-255 | Valor de vermelho da cor (padrão: 0) |
| `g` | INT | Sim | 0-255 | Valor de verde da cor (padrão: 0) |
| `b` | INT | Sim | 0-255 | Valor de azul da cor (padrão: 0) |
| `recraft_color` | COLOR | Não | - | Cor Recraft existente opcional para estender |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `recraft_color` | COLOR | O objeto de cor Recraft criado contendo os valores RGB especificados |
