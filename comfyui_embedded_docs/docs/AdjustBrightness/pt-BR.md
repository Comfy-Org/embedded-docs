> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustBrightness/pt-BR.md)

O nó Ajustar Brilho modifica o brilho de uma imagem de entrada. Ele funciona multiplicando o valor de cada pixel por um fator especificado, garantindo em seguida que os valores resultantes permaneçam dentro de uma faixa válida. Um fator de 1.0 deixa a imagem inalterada, valores abaixo de 1.0 a tornam mais escura e valores acima de 1.0 a tornam mais clara.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | - | A imagem de entrada a ser ajustada. |
| `factor` | FLOAT | Não | 0.0 - 2.0 | Fator de brilho. 1.0 = sem alteração, <1.0 = mais escuro, >1.0 = mais claro. (padrão: 1.0) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `image` | IMAGE | A imagem de saída com o brilho ajustado. |
