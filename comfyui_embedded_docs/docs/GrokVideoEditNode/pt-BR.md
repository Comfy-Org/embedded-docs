> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoEditNode/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoEditNode/en.md)

Este nó utiliza a API Grok para editar um vídeo existente com base em um prompt de texto. Ele faz o upload do seu vídeo, envia uma solicitação ao modelo de IA para modificá-lo de acordo com sua descrição e retorna o novo vídeo gerado.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `model` | COMBO | Sim | `"grok-imagine-video"`<br>`"grok-imagine-video-beta"` | O modelo de IA a ser usado para edição de vídeo (padrão: `"grok-imagine-video"`). |
| `prompt` | STRING | Sim | N/A | Descrição textual do vídeo desejado. |
| `video` | VIDEO | Sim | N/A | O vídeo de entrada a ser editado. A duração máxima suportada é de 8,7 segundos e o tamanho máximo do arquivo é de 50MB. |
| `seed` | INT | Não | 0 a 2147483647 | Um valor de semente para determinar se o nó deve ser executado novamente. Os resultados reais são não determinísticos, independentemente do valor da semente (padrão: 0). |

**Restrições:**

* O `video` de entrada deve ter duração entre 1 e 8,7 segundos.
* O tamanho do arquivo do `video` de entrada não deve exceder 50MB.
* O `prompt` não pode estar vazio.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `video` | VIDEO | O vídeo editado gerado pelo modelo de IA. |

---
**Source fingerprint (SHA-256):** `dfe52a089f7bfe7abc7f40ef113c44aef2dded828221d9d1acf0ddb6a167c33f`
