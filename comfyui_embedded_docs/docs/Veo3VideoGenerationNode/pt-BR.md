Gera vídeos a partir de descrições textuais usando a API Veo 3 do Google. Este nó suporta múltiplos modelos Veo 3, incluindo variantes rápidas e leves, e permite especificar resolução, duração e geração de áudio do vídeo.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `prompt` | Descrição textual do vídeo (padrão: "") | STRING | Sim | - |
| `aspect_ratio` | Proporção de tela do vídeo de saída (padrão: "16:9") | COMBO | Sim | "16:9"<br>"9:16" |
| `resolução` | Resolução do vídeo de saída. 4K não está disponível para os modelos veo-3.1-lite e veo-3.0. (padrão: "720p") | COMBO | Não | "720p"<br>"1080p"<br>"4k" |
| `negative_prompt` | Prompt textual negativo para orientar o que evitar no vídeo (padrão: "") | STRING | Não | - |
| `duration_seconds` | Duração do vídeo de saída em segundos, em intervalos de 2 (padrão: 8) | INT | Não | 4-8 |
| `enhance_prompt` | Este parâmetro está obsoleto e é ignorado. (padrão: True) | BOOLEAN | Não | - |
| `person_generation` | Permite ou bloqueia a geração de pessoas no vídeo (padrão: "ALLOW") | COMBO | Não | "ALLOW"<br>"BLOCK" |
| `seed` | Semente para geração do vídeo (0 para aleatório) (padrão: 0) | INT | Não | 0-4294967295 |
| `image` | Imagem de referência opcional para orientar a geração do vídeo | IMAGE | Não | - |
| `model` | Modelo Veo 3 a ser usado para geração do vídeo (padrão: "veo-3.0-generate-001") | COMBO | Não | "veo-3.1-generate"<br>"veo-3.1-fast-generate"<br>"veo-3.1-lite"<br>"veo-3.0-generate-001"<br>"veo-3.0-fast-generate-001" |
| `generate_audio` | Gera áudio para o vídeo. Suportado por todos os modelos Veo 3. (padrão: False) | BOOLEAN | Não | - |

**Observação:** O parâmetro `enhance_prompt` está obsoleto e seu valor é ignorado. O nó sempre aprimora o prompt internamente. Além disso, o parâmetro `resolution` só é aplicado ao usar um modelo veo-3.1; ele é ignorado para modelos veo-3.0.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | O arquivo de vídeo gerado | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Veo3VideoGenerationNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `36ea9d3f0ea717eb7b8146ca35dfdfbe538fbbf164541ee1d1b19b660543e375`
