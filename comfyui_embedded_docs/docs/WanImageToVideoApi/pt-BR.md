O nó Wan Image to Video gera um vídeo a partir de uma única imagem de entrada e um prompt de texto. Ele usa a imagem fornecida como o primeiro quadro e cria uma sequência de vídeo com base na descrição, com opções de resolução, duração, áudio e outras configurações avançadas.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | Modelo a ser usado (padrão: "wan2.6-i2v") | COMBO | Sim | "wan2.5-i2v-preview"<br>"wan2.6-i2v" |
| `imagem` | Imagem de entrada que serve como o primeiro quadro para a geração do vídeo. Exatamente uma imagem é necessária. | IMAGE | Sim | - |
| `prompt` | Prompt descrevendo os elementos e características visuais. Suporta inglês e chinês (padrão: vazio). | STRING | Sim | - |
| `prompt negativo` | Prompt negativo descrevendo o que evitar (padrão: vazio). | STRING | Não | - |
| `resolução` | Qualidade da resolução do vídeo (padrão: "720P"). O modelo Wan 2.6 não suporta 480P. | COMBO | Não | "480P"<br>"720P"<br>"1080P" |
| `duração` | Duração do vídeo gerado em segundos. Uma duração de 15 segundos é suportada apenas pelo modelo Wan 2.6 (padrão: 5). | INT | Não | 5-15 (passo: 5) |
| `áudio` | O áudio deve conter uma voz clara e alta, sem ruídos estranhos ou música de fundo. Quando fornecido, a duração do áudio deve estar entre 3,0 e 29,0 segundos. | AUDIO | Não | - |
| `semente` | Semente a ser usada para a geração (padrão: 0). | INT | Não | 0-2147483647 |
| `gerar_áudio` | Se nenhuma entrada de áudio for fornecida, gera áudio automaticamente (padrão: False). | BOOLEAN | Não | - |
| `estender_prompt` | Se deve aprimorar o prompt com assistência de IA (padrão: True). | BOOLEAN | Não | - |
| `marca d'água` | Se deve adicionar uma marca d'água gerada por IA ao resultado (padrão: False). | BOOLEAN | Não | - |
| `tipo_de_tomada` | Especifica o tipo de tomada para o vídeo gerado, ou seja, se o vídeo é uma única tomada contínua ou múltiplas tomadas com cortes. Este parâmetro só tem efeito quando prompt_extend é True (padrão: "single"). | COMBO | Não | "single"<br>"multi" |

**Restrições:**

- Exatamente uma imagem de entrada é necessária para a geração do vídeo.
- O modelo Wan 2.6 (`wan2.6-i2v`) não suporta resolução 480P.
- Uma duração de 15 segundos é suportada apenas pelo modelo Wan 2.6 (`wan2.6-i2v`).
- Quando o áudio é fornecido, ele deve ter entre 3,0 e 29,0 segundos de duração.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `output` | Vídeo gerado com base na imagem de entrada e no prompt. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideoApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ad4947dbb9c12ebb97ace99cd447431ba6db88a3b74239099fcbea501cff71f0`
