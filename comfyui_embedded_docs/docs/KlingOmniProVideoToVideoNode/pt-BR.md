> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProVideoToVideoNode/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProVideoToVideoNode/en.md)

Este nó utiliza o modelo Kling AI para gerar um novo vídeo com base em um vídeo de entrada e imagens de referência opcionais. Você fornece um prompt de texto descrevendo o conteúdo desejado, e o nó transforma o vídeo de referência de acordo. Ele também pode incorporar até quatro imagens de referência adicionais para orientar o estilo e o conteúdo da saída.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `model_name` | COMBO | Sim | `"kling-v3-omni"`<br>`"kling-video-o1"` | O modelo Kling específico a ser usado para geração de vídeo (padrão: "kling-v3-omni"). |
| `prompt` | STRING | Sim | N/A | Um prompt de texto descrevendo o conteúdo do vídeo. Pode incluir descrições positivas e negativas. |
| `aspect_ratio` | COMBO | Sim | `"16:9"`<br>`"9:16"`<br>`"1:1"` | A proporção de aspecto desejada para o vídeo gerado. |
| `duration` | INT | Sim | 3 a 10 | A duração do vídeo gerado em segundos (padrão: 3). |
| `reference_video` | VIDEO | Sim | N/A | Vídeo a ser usado como referência. |
| `keep_original_sound` | BOOLEAN | Sim | N/A | Determina se o áudio do vídeo de referência é mantido na saída (padrão: True). |
| `reference_images` | IMAGE | Não | N/A | Até 4 imagens de referência adicionais. |
| `resolution` | COMBO | Não | `"1080p"`<br>`"720p"` | A resolução para o vídeo gerado (padrão: "1080p"). |
| `seed` | INT | Não | 0 a 2147483647 | A semente controla se o nó deve ser executado novamente; os resultados são não determinísticos independentemente da semente (padrão: 0). |

**Restrições dos Parâmetros:**

* O `prompt` deve ter entre 1 e 2500 caracteres.
* O `reference_video` deve ter duração entre 3,0 e 10,05 segundos.
* O `reference_video` deve ter dimensões entre 720x720 e 2160x2160 pixels.
* No máximo 4 `reference_images` podem ser fornecidas. Cada imagem deve ter pelo menos 300x300 pixels e uma proporção de aspecto entre 1:2,5 e 2,5:1.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | VIDEO | O novo vídeo gerado. |

---
**Source fingerprint (SHA-256):** `1bed976530603bcf7db67048e89ad6adac218fba8597744f8ece3e16a2ee4993`
