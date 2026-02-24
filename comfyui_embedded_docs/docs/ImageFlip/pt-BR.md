> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageFlip/pt-BR.md)

O nó ImageFlip inverte imagens ao longo de diferentes eixos. Ele pode inverter imagens verticalmente ao longo do eixo x ou horizontalmente ao longo do eixo y. O nó utiliza operações torch.flip para realizar a inversão com base no método selecionado.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | - | A imagem de entrada a ser invertida |
| `flip_method` | STRING | Sim | "x-axis: vertically"<br>"y-axis: horizontally" | A direção de inversão a ser aplicada |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `image` | IMAGE | A imagem de saída invertida |
