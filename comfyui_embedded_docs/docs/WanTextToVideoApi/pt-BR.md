> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTextToVideoApi/pt-BR.md)

O nó Wan Text to Video gera conteúdo de vídeo com base em descrições textuais. Ele utiliza modelos de IA para criar vídeos a partir de prompts e suporta diversos tamanhos de vídeo, durações e entradas de áudio opcionais. O nó pode gerar áudio automaticamente quando necessário e oferece opções para aprimoramento de prompt e marca d'água.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `modelo` | COMBO | Sim | "wan2.5-t2v-preview"<br>"wan2.6-t2v" | Modelo a ser utilizado (padrão: "wan2.6-t2v") |
| `prompt` | STRING | Sim | - | Prompt descrevendo os elementos e características visuais. Suporta inglês e chinês (padrão: "") |
| `prompt_negativo` | STRING | Não | - | Prompt negativo descrevendo o que deve ser evitado (padrão: "") |
| `tamanho` | COMBO | Não | "480p: 1:1 (624x624)"<br>"480p: 16:9 (832x480)"<br>"480p: 9:16 (480x832)"<br>"720p: 1:1 (960x960)"<br>"720p: 16:9 (1280x720)"<br>"720p: 9:16 (720x1280)"<br>"720p: 4:3 (1088x832)"<br>"720p: 3:4 (832x1088)"<br>"1080p: 1:1 (1440x1440)"<br>"1080p: 16:9 (1920x1080)"<br>"1080p: 9:16 (1080x1920)"<br>"1080p: 4:3 (1632x1248)"<br>"1080p: 3:4 (1248x1632)" | Resolução e proporção do vídeo (padrão: "720p: 1:1 (960x960)") |
| `duração` | INT | Não | 5-15 (em incrementos de 5) | Duração do vídeo em segundos. A duração de 15 segundos está disponível apenas para o modelo Wan 2.6 (padrão: 5) |
| `áudio` | AUDIO | Não | - | O áudio deve conter uma voz clara e alta, sem ruídos estranhos ou música de fundo |
| `semente` | INT | Não | 0-2147483647 | Semente a ser usada para geração (padrão: 0) |
| `gerar_áudio` | BOOLEAN | Não | - | Se nenhuma entrada de áudio for fornecida, gera áudio automaticamente (padrão: False) |
| `estender_prompt` | BOOLEAN | Não | - | Se deve aprimorar o prompt com assistência de IA (padrão: True) |
| `marca_d'água` | BOOLEAN | Não | - | Se deve adicionar uma marca d'água gerada por IA ao resultado (padrão: False) |
| `tipo_de_tomada` | COMBO | Não | "single"<br>"multi" | Especifica o tipo de tomada para o vídeo gerado, ou seja, se o vídeo é uma única tomada contínua ou múltiplas tomadas com cortes. Este parâmetro só tem efeito quando prompt_extend é True (padrão: "single") |

**Observação:** O modelo Wan 2.6 não suporta resoluções 480p. A duração de 15 segundos é suportada apenas pelo modelo Wan 2.6. Ao fornecer entrada de áudio, ela deve ter entre 3,0 e 29,0 segundos de duração e conter voz clara, sem ruído de fundo ou música.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | VIDEO | O vídeo gerado com base nos parâmetros de entrada |

---
**Source fingerprint (SHA-256):** `e978f384365060a6d71899e4e2e22b2c6f4268fb0da988c8902e4876d8597a96`
