O nó Runway Text to Image gera imagens a partir de prompts de texto usando o modelo Gen 4 da Runway. Você pode fornecer uma descrição textual e, opcionalmente, incluir uma imagem de referência para orientar o processo de geração de imagem. O nó gerencia a comunicação com a API e retorna a imagem gerada.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt de texto para a geração (padrão: "") | STRING | Sim | - |
| `proporção` | Proporção de aspecto para a imagem gerada | COMBO | Sim | "16:9"<br>"1:1"<br>"21:9"<br>"2:3"<br>"3:2"<br>"4:5"<br>"5:4"<br>"9:16"<br>"9:21" |
| `imagem_de_referência` | Imagem de referência opcional para orientar a geração | IMAGE | Não | - |

**Observação:** A imagem de referência deve ter dimensões que não excedam 7999x7999 pixels e uma proporção de aspecto entre 0,5 e 2,0. Quando uma imagem de referência é fornecida, ela orienta o processo de geração de imagem.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | A imagem gerada com base no prompt de texto e na imagem de referência opcional | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayTextToImageNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `140f8e6b07216892d84f2d7fbc3afaf1c390e98ddedf27d4926032066a783f67`
