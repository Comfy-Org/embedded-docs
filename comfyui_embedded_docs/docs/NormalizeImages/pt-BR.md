> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeImages/pt-BR.md)

Este nó ajusta os valores de pixel de uma imagem de entrada usando um processo matemático de normalização. Ele subtrai um valor médio especificado de cada pixel e, em seguida, divide o resultado por um desvio padrão especificado. Esta é uma etapa comum de pré-processamento para preparar dados de imagem para outros modelos de aprendizado de máquina.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | - | A imagem de entrada a ser normalizada. |
| `mean` | FLOAT | Não | 0.0 - 1.0 | O valor médio a ser subtraído dos pixels da imagem (padrão: 0.5). |
| `std` | FLOAT | Não | 0.001 - 1.0 | O valor do desvio padrão pelo qual os pixels da imagem serão divididos (padrão: 0.5). |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `image` | IMAGE | A imagem resultante após a aplicação do processo de normalização. |
