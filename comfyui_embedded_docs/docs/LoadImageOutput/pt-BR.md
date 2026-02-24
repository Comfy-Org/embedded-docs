> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageOutput/pt-BR.md)

O nó LoadImageOutput carrega imagens da pasta de saída. Quando você clica no botão de atualizar, ele atualiza a lista de imagens disponíveis e seleciona automaticamente a primeira, facilitando a iteração pelas suas imagens geradas.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `image` | COMBO | Sim | Múltiplas opções disponíveis | Carrega uma imagem da pasta de saída. Inclui uma opção de upload e um botão de atualizar para renovar a lista de imagens. |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `image` | IMAGE | A imagem carregada da pasta de saída |
| `mask` | MASK | A máscara associada à imagem carregada |
