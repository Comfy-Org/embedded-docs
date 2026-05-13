> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideoApi/pt-BR.md)

O nó Wan Image to Video gera um vídeo a partir de uma única imagem de entrada e um prompt de texto. Ele usa a imagem fornecida como o primeiro quadro e cria uma sequência de vídeo com base na descrição, com opções de resolução, duração, áudio e outras configurações avançadas.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|---------------|-------------|-----------|-----------|
| `model` | COMBO | Sim | "wan2.5-i2v-preview"<br>"wan2.6-i2v" | Modelo a ser usado (padrão: "wan2.6-i2v") |
| `image` | IMAGE | Sim | - | Imagem de entrada que serve como o primeiro quadro para a geração do vídeo. Exatamente uma imagem é necessária. |
| `prompt` | STRING | Sim | - | Prompt descrevendo os elementos e características visuais. Suporta inglês e chinês (padrão: vazio). |
| `negative_prompt` | STRING | Não | - | Prompt negativo descrevendo o que evitar (padrão: vazio). |
| `resolution` | COMBO | Não | "480P"<br>"720P"<br>"1080P" | Qualidade da resolução do vídeo (padrão: "720P"). O modelo Wan 2.6 não suporta 480P. |
| `duration` | INT | Não | 5-15 (passo: 5) | Duração do vídeo gerado em segundos. Uma duração de 15 segundos é suportada apenas pelo modelo Wan 2.6 (padrão: 5). |
| `audio` | AUDIO | Não | - | O áudio deve conter uma voz clara e alta, sem ruídos estranhos ou música de fundo. Quando fornecido, a duração do áudio deve estar entre 3,0 e 29,0 segundos. |
| `seed` | INT | Não | 0-2147483647 | Semente a ser usada para a geração (padrão: 0). |
| `generate_audio` | BOOLEAN | Não | - | Se nenhuma entrada de áudio for fornecida, gera áudio automaticamente (padrão: False). |
| `prompt_extend` | BOOLEAN | Não | - | Se deve aprimorar o prompt com assistência de IA (padrão: True). |
| `watermark` | BOOLEAN | Não | - | Se deve adicionar uma marca d'água gerada por IA ao resultado (padrão: False). |
| `shot_type` | COMBO | Não | "single"<br>"multi" | Especifica o tipo de tomada para o vídeo gerado, ou seja, se o vídeo é uma única tomada contínua ou múltiplas tomadas com cortes. Este parâmetro só tem efeito quando prompt_extend é True (padrão: "single"). |

**Restrições:**

- Exatamente uma imagem de entrada é necessária para a geração do vídeo.
- O modelo Wan 2.6 (`wan2.6-i2v`) não suporta resolução 480P.
- Uma duração de 15 segundos é suportada apenas pelo modelo Wan 2.6 (`wan2.6-i2v`).
- Quando o áudio é fornecido, ele deve ter entre 3,0 e 29,0 segundos de duração.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `output` | VIDEO | Vídeo gerado com base na imagem de entrada e no prompt. |

---
**Source fingerprint (SHA-256):** `ad4947dbb9c12ebb97ace99cd447431ba6db88a3b74239099fcbea501cff71f0`
