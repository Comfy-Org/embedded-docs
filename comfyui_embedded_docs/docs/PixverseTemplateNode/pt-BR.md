> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTemplateNode/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTemplateNode/en.md)

O nó PixVerse Template permite selecionar entre modelos disponíveis para geração de vídeo no PixVerse. Ele converte o nome do modelo selecionado no ID de modelo correspondente que a API do PixVerse exige para a criação de vídeos.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `template` | STRING | Sim | Múltiplas opções disponíveis | O modelo a ser usado para geração de vídeo no PixVerse. As opções disponíveis correspondem a modelos predefinidos no sistema PixVerse. |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `pixverse_template` | STRING | O ID do modelo correspondente ao nome do modelo selecionado, que pode ser usado por outros nós do PixVerse para geração de vídeo. |

---
**Source fingerprint (SHA-256):** `d6ea1eb1cc9a7d33cf69f101990e601189726b9ef9e199fe211087f7070f35d0`
