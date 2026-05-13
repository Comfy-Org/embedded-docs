> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseImageToVideoApi/pt-BR.md)

# Visão Geral

Este nó gera um vídeo curto a partir de uma única imagem inicial usando o modelo HappyHorse. Você fornece uma imagem de primeiro quadro e um prompt de texto descrevendo o movimento desejado e a cena, e o nó cria um vídeo que continua a partir dessa imagem.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `model` | COMBO | Sim | `"happyhorse-1.0-i2v"` | O modelo HappyHorse a ser usado para geração de vídeo. |
| `model.prompt` | STRING | Não | N/A | Prompt descrevendo os elementos e características visuais. Suporta inglês e chinês. (padrão: "") |
| `model.resolution` | COMBO | Sim | `"720P"`<br>`"1080P"` | A resolução do vídeo de saída. (padrão: "720P") |
| `model.duration` | INT | Sim | 3 a 15 | A duração do vídeo gerado em segundos. (padrão: 5) |
| `first_frame` | IMAGE | Sim | N/A | Imagem do primeiro quadro. A proporção de aspecto da saída é derivada desta imagem. |
| `seed` | INT | Não | 0 a 2147483647 | Semente a ser usada para geração. (padrão: 0) |
| `watermark` | BOOLEAN | Não | Verdadeiro / Falso | Se deve adicionar uma marca d'água de IA ao resultado. (padrão: Falso) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `video` | VIDEO | O arquivo de vídeo gerado. |

---
**Source fingerprint (SHA-256):** `e10ad61abd92df7ad6dd3ac70cc6af35faf0413798f4cff32c81194695bb0bed`
