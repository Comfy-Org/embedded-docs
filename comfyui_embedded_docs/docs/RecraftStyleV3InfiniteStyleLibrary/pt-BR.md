> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3InfiniteStyleLibrary/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3InfiniteStyleLibrary/en.md)

Este nó permite selecionar um estilo da Biblioteca Infinita de Estilos do Recraft usando um UUID preexistente. Ele recupera as informações do estilo com base no identificador fornecido e o retorna para uso em outros nós do Recraft.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|---------------|-------------|-----------|-----------|
| `style_id` | STRING | Sim | Qualquer UUID válido | UUID do estilo da Biblioteca Infinita de Estilos. |

**Observação:** A entrada `style_id` não pode estar vazia. Se uma string vazia for fornecida, o nó lançará uma exceção.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `recraft_style` | STYLEV3 | O objeto de estilo selecionado da Biblioteca Infinita de Estilos do Recraft |

---
**Source fingerprint (SHA-256):** `37d7d9eff1232cc17912c6fca908dc5b8c404c0b6cf0a36e8fecc837ff2a1eea`
