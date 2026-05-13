> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ImageToVideoApi/pt-BR.md)

Este documento foi gerado por IA. Se encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ImageToVideoApi/en.md)

O nó Wan 2.7 Imagem para Vídeo gera um vídeo a partir de uma imagem de primeiro quadro. Opcionalmente, você pode fornecer uma imagem de último quadro para criar uma transição entre os dois, ou fornecer um arquivo de áudio para guiar o movimento e o ritmo do vídeo. O nó utiliza um modelo de IA para animar a cena com base na sua descrição textual.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `model` | COMBO | Sim | `"wan2.7-i2v"` | O modelo de IA a ser usado para geração de vídeo. |
| `model.prompt` | STRING | Sim | - | Uma descrição textual dos elementos e características visuais desejados no vídeo. Suporta inglês e chinês. |
| `model.negative_prompt` | STRING | Sim | - | Uma descrição textual de elementos ou características que o modelo deve evitar. |
| `model.resolution` | COMBO | Sim | `"720P"`<br>`"1080P"` | A resolução do vídeo de saída. |
| `model.duration` | INT | Sim | 2 a 15 | A duração do vídeo gerado em segundos (padrão: 5). |
| `first_frame` | IMAGE | Sim | - | A imagem a ser usada como primeiro quadro do vídeo. A proporção de aspecto do vídeo de saída é derivada desta imagem. |
| `last_frame` | IMAGE | Não | - | Uma imagem opcional para usar como último quadro. Quando fornecida, o modelo gera um vídeo que faz a transição do primeiro para este último quadro. |
| `audio` | AUDIO | Não | - | Um arquivo de áudio opcional para guiar a geração do vídeo, útil para sincronização labial ou movimentos sincronizados com batidas. A duração deve estar entre 2 e 30 segundos. Se não for fornecido, o modelo gerará música de fundo ou efeitos sonoros correspondentes. |
| `seed` | INT | Sim | 0 a 2147483647 | Um valor de semente para controlar a aleatoriedade da geração (padrão: 0). |
| `prompt_extend` | BOOLEAN | Sim | - | Quando ativado, o nó usará assistência de IA para aprimorar seu prompt de texto (padrão: Verdadeiro). Esta é uma configuração avançada. |
| `watermark` | BOOLEAN | Sim | - | Quando ativado, uma marca d'água gerada por IA será adicionada ao vídeo final (padrão: Falso). Esta é uma configuração avançada. |

**Nota:** A entrada `audio` possui uma restrição de duração. Se fornecida, o arquivo de áudio deve ter entre 2 e 30 segundos de duração.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `output` | VIDEO | O arquivo de vídeo gerado. |

---
**Source fingerprint (SHA-256):** `ccd18dca3b191f2cbe64b6c2b941a7efcf281e4f327329d932cec27fd8234133`
