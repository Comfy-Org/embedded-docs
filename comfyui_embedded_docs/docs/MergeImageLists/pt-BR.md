> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MergeImageLists/pt-BR.md)

O nó Merge Image Lists combina várias listas separadas de imagens em uma única lista contínua. Ele funciona pegando todas as imagens de cada entrada conectada e as anexando juntas na ordem em que são recebidas. Isso é útil para organizar ou agrupar imagens de diferentes fontes para processamento posterior.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Sim | - | Uma lista de imagens a ser mesclada. Esta entrada pode aceitar múltiplas conexões, e cada lista conectada será concatenada na saída final. |

**Observação:** Este nó foi projetado para receber múltiplas entradas. Você pode conectar várias listas de imagens ao único soquete de entrada `images`. O nó concatenará automaticamente todas as imagens de todas as listas conectadas em uma única lista de saída.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `images` | IMAGE | A lista única e mesclada contendo todas as imagens de cada lista de entrada conectada. |
