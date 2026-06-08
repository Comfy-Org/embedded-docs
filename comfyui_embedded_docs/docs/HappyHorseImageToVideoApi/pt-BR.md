# Visão Geral

Este nó gera um vídeo curto a partir de uma única imagem inicial usando o modelo HappyHorse. Você fornece uma imagem de primeiro quadro e um prompt de texto descrevendo o movimento desejado e a cena, e o nó cria um vídeo que continua a partir dessa imagem.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model` | O modelo HappyHorse a ser usado para geração de vídeo. | COMBO | Sim | `"happyhorse-1.0-i2v"` |
| `model.prompt` | Prompt descrevendo os elementos e características visuais. Suporta inglês e chinês. (padrão: "") | STRING | Não | N/A |
| `model.resolution` | A resolução do vídeo de saída. (padrão: "720P") | COMBO | Sim | `"720P"`<br>`"1080P"` |
| `model.duration` | A duração do vídeo gerado em segundos. (padrão: 5) | INT | Sim | 3 a 15 |
| `first_frame` | Imagem do primeiro quadro. A proporção de aspecto da saída é derivada desta imagem. | IMAGE | Sim | N/A |
| `seed` | Semente a ser usada para geração. (padrão: 0) | INT | Não | 0 a 2147483647 |
| `watermark` | Se deve adicionar uma marca d'água de IA ao resultado. (padrão: Falso) | BOOLEAN | Não | Verdadeiro / Falso |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `video` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseImageToVideoApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `e10ad61abd92df7ad6dd3ac70cc6af35faf0413798f4cff32c81194695bb0bed`
