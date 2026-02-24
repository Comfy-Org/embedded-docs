> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageRGBToYUV/pt-BR.md)

O nó ImageRGBToYUV converte imagens coloridas RGB para o espaço de cores YUV. Ele recebe uma imagem RGB como entrada e a separa em três canais distintos: Y (luminância), U (projeção azul) e V (projeção vermelha). Cada canal de saída é retornado como uma imagem em tons de cinza separada, representando o componente YUV correspondente.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sim | - | A imagem RGB de entrada a ser convertida para o espaço de cores YUV |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `Y` | IMAGE | O componente de luminância (brilho) do espaço de cores YUV |
| `U` | IMAGE | O componente de projeção azul do espaço de cores YUV |
| `V` | IMAGE | O componente de projeção vermelha do espaço de cores YUV |
