> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustContrast/pt-BR.md)

O nó Adjust Contrast modifica o nível de contraste de uma imagem de entrada. Ele funciona ajustando a diferença entre as áreas claras e escuras da imagem. Um fator de 1.0 deixa a imagem inalterada, valores abaixo de 1.0 reduzem o contraste e valores acima de 1.0 o aumentam.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | - | A imagem de entrada que terá seu contraste ajustado. |
| `factor` | FLOAT | Não | 0.0 - 2.0 | Fator de contraste. 1.0 = sem alteração, <1.0 = menos contraste, >1.0 = mais contraste. (padrão: 1.0) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `image` | IMAGE | A imagem resultante com o contraste ajustado. |
