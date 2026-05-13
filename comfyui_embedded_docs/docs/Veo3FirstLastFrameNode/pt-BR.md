> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Veo3FirstLastFrameNode/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Veo3FirstLastFrameNode/en.md)

O nó Veo3FirstLastFrameNode usa o modelo Veo 3 do Google para gerar um vídeo baseado em um prompt de texto, com um primeiro e último quadro fornecidos que definem o início e o fim da sequência de vídeo.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `prompt` | STRING | Sim | N/A | Descrição textual do vídeo (padrão: string vazia). |
| `negative_prompt` | STRING | Não | N/A | Prompt de texto negativo para orientar o que evitar no vídeo (padrão: string vazia). |
| `resolution` | COMBO | Sim | `"720p"`<br>`"1080p"`<br>`"4k"` | A resolução do vídeo de saída. |
| `aspect_ratio` | COMBO | Não | `"16:9"`<br>`"9:16"` | Proporção de aspecto do vídeo de saída (padrão: "16:9"). |
| `duration` | INT | Não | 4 a 8 | Duração do vídeo de saída em segundos (padrão: 8). |
| `seed` | INT | Não | 0 a 4294967295 | Semente para geração do vídeo (padrão: 0). |
| `first_frame` | IMAGE | Sim | N/A | O quadro inicial do vídeo. |
| `last_frame` | IMAGE | Sim | N/A | O quadro final do vídeo. |
| `model` | COMBO | Não | `"veo-3.1-generate"`<br>`"veo-3.1-fast-generate"`<br>`"veo-3.1-lite"` | O modelo Veo 3 específico a ser usado para geração (padrão: "veo-3.1-generate"). |
| `generate_audio` | BOOLEAN | Não | N/A | Gerar áudio para o vídeo (padrão: Verdadeiro). |

**Nota:** O modelo `veo-3.1-lite` não suporta resolução 4K. Se você selecionar `veo-3.1-lite` e resolução `4k`, ocorrerá um erro.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | VIDEO | O arquivo de vídeo gerado. |

---
**Source fingerprint (SHA-256):** `b486b22e71a305172700760bb3eff256b0e571bba75e68f27e23a1e1a1319b5a`
