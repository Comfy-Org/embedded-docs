Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoReferenceNode/en.md)

O nó Grok Referência-para-Vídeo gera um vídeo com base em um prompt de texto, usando até sete imagens de referência para orientar o estilo e o conteúdo da saída. Ele se conecta a uma API externa para criar o vídeo, que é então baixado e retornado.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `prompt` | Descrição textual do vídeo desejado. | STRING | Sim | N/A |
| `modelo` | O modelo a ser usado para a geração do vídeo. | COMBO | Sim | `"grok-imagine-video"` |
| `model.reference_images` | Até 7 imagens de referência para orientar a geração do vídeo. | IMAGE | Sim | 1 a 7 imagens |
| `model.resolution` | A resolução do vídeo de saída. | COMBO | Sim | `"480p"`<br>`"720p"` |
| `model.aspect_ratio` | A proporção de aspecto do vídeo de saída. | COMBO | Sim | `"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` |
| `model.duration` | A duração do vídeo de saída em segundos (padrão: 6). | INT | Sim | 2 a 10 |
| `semente` | Semente para determinar se o nó deve ser reexecutado; os resultados reais são não determinísticos, independentemente da semente (padrão: 0). | INT | Não | 0 a 2147483647 |

**Nota:** O parâmetro `model` é um grupo que contém `reference_images`, `resolution`, `aspect_ratio` e `duration`. Você deve fornecer pelo menos uma imagem de referência e pode fornecer até sete.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `video` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoReferenceNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e368769b869b7a0d0be8e6fdcc2b82774c11805483b2e83a448b6985a6dd9f96`
