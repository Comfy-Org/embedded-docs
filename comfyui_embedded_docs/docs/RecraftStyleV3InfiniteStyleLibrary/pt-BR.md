> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3InfiniteStyleLibrary/pt-BR.md)

Este nó permite que você selecione um estilo da Biblioteca de Estilos Infinitos da Recraft usando um UUID preexistente. Ele recupera as informações do estilo com base no identificador fornecido e as retorna para uso em outros nós da Recraft.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `style_id` | STRING | Sim | Qualquer UUID válido | UUID do estilo da Biblioteca de Estilos Infinitos. |

**Observação:** A entrada `style_id` não pode estar vazia. Se uma string vazia for fornecida, o nó lançará uma exceção.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `recraft_style` | STYLEV3 | O objeto de estilo selecionado da Biblioteca de Estilos Infinitos da Recraft |
