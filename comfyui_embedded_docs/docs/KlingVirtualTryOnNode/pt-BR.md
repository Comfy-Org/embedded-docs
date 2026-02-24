> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVirtualTryOnNode/pt-BR.md)

Kling Virtual Try On Node. Insira uma imagem de uma pessoa e uma imagem de uma peça de roupa para experimentar a roupa na pessoa. Você pode combinar várias imagens de itens de vestuário em uma única imagem com um fundo branco.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `human_image` | IMAGE | Sim | - | A imagem da pessoa em quem experimentar as roupas |
| `cloth_image` | IMAGE | Sim | - | A imagem da peça de roupa para experimentar na pessoa |
| `model_name` | STRING | Sim | `"kolors-virtual-try-on-v1"` | O modelo de experimentação virtual a ser usado (padrão: "kolors-virtual-try-on-v1") |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `output` | IMAGE | A imagem resultante mostrando a pessoa com o item de vestuário experimentado |
