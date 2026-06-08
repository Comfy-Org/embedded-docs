Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTemplateNode/en.md)

O nó PixVerse Template permite selecionar entre modelos disponíveis para geração de vídeo no PixVerse. Ele converte o nome do modelo selecionado no ID de modelo correspondente que a API do PixVerse exige para a criação de vídeos.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `template` | O modelo a ser usado para geração de vídeo no PixVerse. As opções disponíveis correspondem a modelos predefinidos no sistema PixVerse. | STRING | Sim | Múltiplas opções disponíveis |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `pixverse_template` | O ID do modelo correspondente ao nome do modelo selecionado, que pode ser usado por outros nós do PixVerse para geração de vídeo. | STRING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTemplateNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `d6ea1eb1cc9a7d33cf69f101990e601189726b9ef9e199fe211087f7070f35d0`
