> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScaleToMaxDimension/pt-BR.md)

O nó ImageScaleToMaxDimension redimensiona imagens para caberem dentro de uma dimensão máxima especificada, mantendo a proporção original. Ele calcula se a imagem está orientada no modo retrato ou paisagem e, em seguida, dimensiona a dimensão maior para corresponder ao tamanho alvo, ajustando proporcionalmente a dimensão menor. O nó suporta vários métodos de ampliação para diferentes requisitos de qualidade e desempenho.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | - | A imagem de entrada a ser dimensionada |
| `upscale_method` | STRING | Sim | "area"<br>"lanczos"<br>"bilinear"<br>"nearest-exact"<br>"bicubic" | O método de interpolação usado para dimensionar a imagem |
| `largest_size` | INT | Sim | 0 a 16384 | A dimensão máxima para a imagem redimensionada (padrão: 512) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `image` | IMAGE | A imagem redimensionada com a maior dimensão correspondendo ao tamanho especificado |
