# Grok Video

O nó Grok Video gera um vídeo curto a partir de uma descrição textual. Ele pode criar um vídeo do zero usando um prompt, ou gerar um vídeo a partir de uma única imagem de entrada. O nó envia a solicitação para uma API externa e retorna o vídeo gerado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo a ser usado para geração de vídeo. | COMBO | Sim | `"grok-imagine-video"`<br>`"grok-imagine-video-1.5"` |
| `prompt` | Descrição textual do vídeo desejado. Opcional para grok-imagine-video-1.5 quando uma imagem de entrada é fornecida. | STRING | Sim | - |
| `resolution` | A resolução do vídeo de saída. 1080p está disponível apenas para grok-imagine-video-1.5. | COMBO | Sim | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `aspect_ratio` | A proporção de aspecto do vídeo de saída. | COMBO | Sim | `"auto"`<br>`"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` |
| `duration` | A duração do vídeo de saída em segundos (padrão: 6). | INT | Sim | 1 a 15 |
| `seed` | Semente para determinar se o nó deve ser executado novamente; os resultados reais são não determinísticos independentemente da semente (padrão: 0). | INT | Sim | 0 a 2147483647 |
| `image` | Imagem inicial opcional. Se omitida, o vídeo é gerado apenas a partir do prompt de texto. | IMAGE | Não | - |

**Observação:** Quando uma `image` é fornecida, apenas uma imagem de entrada é suportada; fornecer várias imagens causará um erro. O `prompt` deve ser não vazio após remover espaços em branco quando nenhuma imagem é fornecida, ou ao usar `grok-imagine-video` mesmo com uma imagem. Para `grok-imagine-video-1.5`, o `prompt` é opcional somente quando uma imagem de entrada é fornecida. A resolução `1080p` está disponível apenas para `grok-imagine-video-1.5`. Quando `aspect_ratio` é definido como `"auto"`, a proporção de aspecto é escolhida automaticamente pelo serviço.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `output` | O vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c7d07b7bf9a776892873698abb97c7d936c7770aab397d031a287b7ecfad0b71`
