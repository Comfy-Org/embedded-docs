# Grok Video

O nó Grok Video gera um vídeo curto a partir de uma descrição textual. Ele pode criar um vídeo do zero usando um prompt, ou gerar um vídeo a partir de uma única imagem de entrada. O nó envia a solicitação para uma API externa e retorna o vídeo gerado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo a ser usado para geração de vídeo (padrão: `"grok-imagine-video-1.5-lite"`). | COMBO | Sim | `"grok-imagine-video"`<br>`"grok-imagine-video-1.5"`<br>`"grok-imagine-video-1.5-lite"` |
| `prompt` | Descrição textual do vídeo desejado. Opcional para os modelos `grok-imagine-video-1.5` quando uma imagem de entrada é fornecida. | STRING | Sim | - |
| `resolution` | A resolução do vídeo de saída. `1080p` não está disponível para `grok-imagine-video`. | COMBO | Sim | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `aspect_ratio` | A proporção de aspecto do vídeo de saída. Ignorada quando uma imagem de entrada é fornecida; o vídeo segue a proporção de aspecto da imagem. | COMBO | Sim | `"auto"`<br>`"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` |
| `duration` | A duração do vídeo de saída em segundos (padrão: 6). | INT | Sim | 1 a 15 |
| `seed` | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente da semente (padrão: 0). | INT | Sim | 0 a 2147483647 |
| `image` | Imagem inicial opcional. Se omitida, o vídeo é gerado apenas a partir do prompt de texto. | IMAGE | Não | - |

**Nota:** Quando uma `image` é fornecida, apenas uma imagem de entrada é suportada; fornecer múltiplas imagens causará um erro. O `prompt` deve ser não vazio após remover espaços em branco quando nenhuma imagem é fornecida, ou ao usar `grok-imagine-video` mesmo com uma imagem. Para os modelos `grok-imagine-video-1.5`, o `prompt` é opcional apenas quando uma imagem de entrada é fornecida. A resolução `1080p` não está disponível para `grok-imagine-video`. Quando `aspect_ratio` é definido como `"auto"`, a proporção de aspecto é escolhida automaticamente pelo serviço; quando uma imagem de entrada é fornecida, `aspect_ratio` é ignorado e o vídeo segue a proporção de aspecto da imagem.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | O vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ed5a1c39598a319d5b350b19f39a352dedd1150471695d25f7637fc0f8735d02`
