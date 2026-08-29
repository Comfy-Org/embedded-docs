# Google Veo 3 Geração de Vídeo

Gera vídeos a partir de prompts de texto usando a API Google Veo 3. Este nó suporta múltiplos modelos Veo 3, incluindo variantes rápidas e leves, e permite especificar resolução de vídeo, duração e geração de áudio.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
|-----------|-------------|--------------|-------------|-----------|
| `prompt` | Descrição textual do vídeo (padrão: "") | STRING | Sim | - |
| `aspect_ratio` | Proporção de aspecto do vídeo de saída (padrão: "16:9") | COMBO | Sim | "16:9"<br>"9:16" |
| `resolução` | Resolução do vídeo de saída. 4K não está disponível para o modelo veo-3.1-lite. (padrão: "720p") | COMBO | Não | "720p"<br>"1080p"<br>"4k" |
| `negative_prompt` | Prompt de texto negativo para orientar o que evitar no vídeo (padrão: "") | STRING | Não | - |
| `duration_seconds` | Duração do vídeo de saída em segundos (padrão: 8) | INT | Não | 4 - 8 (passo 2) |
| `enhance_prompt` | Este parâmetro está obsoleto e é ignorado. (padrão: True) | BOOLEAN | Não | - |
| `person_generation` | Se permite a geração de pessoas no vídeo (padrão: "ALLOW") | COMBO | Não | "ALLOW"<br>"BLOCK" |
| `seed` | Semente para geração de vídeo (0 para aleatório) (padrão: 0) | INT | Não | 0 - 4294967295 |
| `image` | Imagem de referência opcional para orientar a geração de vídeo | IMAGE | Não | - |
| `model` | Modelo Veo 3 a ser usado para geração de vídeo (padrão: "veo-3.1-generate") | COMBO | Não | "veo-3.1-generate"<br>"veo-3.1-fast-generate"<br>"veo-3.1-lite" |
| `generate_audio` | Gera áudio para o vídeo. Suportado por todos os modelos Veo 3. (padrão: False) | BOOLEAN | Não | - |

**Nota:** O parâmetro `enhance_prompt` está obsoleto e seu valor é ignorado. O nó sempre aprimora o prompt internamente. Se você selecionar a resolução "4k" com o modelo veo-3.1-lite, o nó gera um erro.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
|---------------|-------------|-------------|
| `output` | O arquivo de vídeo gerado | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Veo3VideoGenerationNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5320736448ad854e2f93e08ccaa870e977e06497666cb305f314bc76ff917740`
