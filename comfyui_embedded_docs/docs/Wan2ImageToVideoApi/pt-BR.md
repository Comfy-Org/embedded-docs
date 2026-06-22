# Wan 2.7 Imagem para Vídeo

Este documento foi gerado por IA. Se encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ImageToVideoApi/en.md)

O nó Wan 2.7 Imagem para Vídeo gera um vídeo a partir de uma imagem de primeiro quadro. Opcionalmente, você pode fornecer uma imagem de último quadro para criar uma transição entre os dois, ou fornecer um arquivo de áudio para guiar o movimento e o ritmo do vídeo. O nó utiliza um modelo de IA para animar a cena com base na sua descrição textual.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model` | O modelo de IA a ser usado para geração de vídeo. | COMBO | Sim | `"wan2.7-i2v"` |
| `model.prompt` | Uma descrição textual dos elementos e características visuais desejados no vídeo. Suporta inglês e chinês. | STRING | Sim | - |
| `model.negative_prompt` | Uma descrição textual de elementos ou características que o modelo deve evitar. | STRING | Sim | - |
| `model.resolution` | A resolução do vídeo de saída. | COMBO | Sim | `"720P"`<br>`"1080P"` |
| `model.duration` | A duração do vídeo gerado em segundos (padrão: 5). | INT | Sim | 2 a 15 |
| `first_frame` | A imagem a ser usada como primeiro quadro do vídeo. A proporção de aspecto do vídeo de saída é derivada desta imagem. | IMAGE | Sim | - |
| `last_frame` | Uma imagem opcional para usar como último quadro. Quando fornecida, o modelo gera um vídeo que faz a transição do primeiro para este último quadro. | IMAGE | Não | - |
| `audio` | Um arquivo de áudio opcional para guiar a geração do vídeo, útil para sincronização labial ou movimentos sincronizados com batidas. A duração deve estar entre 2 e 30 segundos. Se não for fornecido, o modelo gerará música de fundo ou efeitos sonoros correspondentes. | AUDIO | Não | - |
| `seed` | Um valor de semente para controlar a aleatoriedade da geração (padrão: 0). | INT | Sim | 0 a 2147483647 |
| `prompt_extend` | Quando ativado, o nó usará assistência de IA para aprimorar seu prompt de texto (padrão: Verdadeiro). Esta é uma configuração avançada. | BOOLEAN | Sim | - |
| `watermark` | Quando ativado, uma marca d'água gerada por IA será adicionada ao vídeo final (padrão: Falso). Esta é uma configuração avançada. | BOOLEAN | Sim | - |

**Nota:** A entrada `audio` possui uma restrição de duração. Se fornecida, o arquivo de áudio deve ter entre 2 e 30 segundos de duração.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ImageToVideoApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ccd18dca3b191f2cbe64b6c2b941a7efcf281e4f327329d932cec27fd8234133`
