> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageOutput/pt-BR.md)

O nó LoadImageOutput carrega imagens da pasta de saída. Ao clicar no botão de atualizar, ele atualiza a lista de imagens disponíveis e seleciona automaticamente a primeira, facilitando a iteração entre suas imagens geradas.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `imagem` | COMBO | Sim | Múltiplas opções disponíveis | Carrega uma imagem da pasta de saída. Inclui uma opção de upload e um botão de atualizar para renovar a lista de imagens. Quando o botão de atualizar é clicado, o nó atualiza a lista de imagens e seleciona automaticamente a primeira, permitindo uma iteração fácil. |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `imagem` | IMAGE | A imagem carregada da pasta de saída |
| `mask` | MASK | A máscara associada à imagem carregada |

---
**Source fingerprint (SHA-256):** `d1de0140765c9d5dd393715faa84dc5c3f0e49117391b8823a51b176bcb568d8`
