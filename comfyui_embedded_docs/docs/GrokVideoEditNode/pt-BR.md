# Grok Video Edit

This node uses the Grok API to edit an existing video based on a text prompt. It uploads your video, sends a request to the AI model to modify it according to your description, and returns the newly generated video.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo de IA a ser usado para edição de vídeo (padrão: "grok-imagine-video"). | COMBO | Sim | "grok-imagine-video" |
| `prompt` | Descrição textual do vídeo desejado. | STRING | Sim | N/A |
| `video` | O vídeo de entrada a ser editado. A duração máxima suportada é de 8,7 segundos e o tamanho máximo do arquivo é de 50 MB. | VIDEO | Sim | N/A |
| `seed` | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente da semente (padrão: 0). | INT | Não | 0 a 2147483647 |

**Restrições:**

* O `prompt` não pode estar vazio.
* O `video` de entrada deve ter duração entre 1 e 8,7 segundos.
* O tamanho do arquivo do `video` de entrada não deve exceder 50 MB.

**Observação:** Este nó é um nó de API e requer uma conta Comfy.org e uma chave de API para ser executado. O uso é cobrado a aproximadamente US$ 0,06 por segundo de vídeo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `video` | O vídeo editado gerado pelo modelo de IA. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoEditNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7ceedff2f858bc0849b5e0d92d10ed51e7fdccd1391c6a6966561cb05999b4b1`
