> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftCreativeUpscaleNode/pt-BR.md)

## Visão Geral

O nó Recraft Creative Upscale Image aprimora uma imagem raster aumentando sua resolução. Ele utiliza um processo de "upscale criativo" que se concentra em melhorar pequenos detalhes e rostos dentro da imagem. Esta operação é realizada de forma síncrona através de uma API externa.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | | A imagem de entrada a ser aprimorada em resolução. |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `image` | IMAGE | A imagem resultante com resolução aumentada e detalhes aprimorados. |
