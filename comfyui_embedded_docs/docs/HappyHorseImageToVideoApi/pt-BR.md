# HappyHorse Imagem para Vídeo

Este nó gera um vídeo curto a partir de uma única imagem inicial usando o modelo HappyHorse. Você fornece uma imagem de primeiro quadro e um prompt de texto descrevendo o movimento e a cena desejados, e o nó cria um vídeo que continua a partir dessa imagem.

## Entradas

### Entradas Comuns

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model` | O modelo HappyHorse a ser usado para a geração de vídeos. | COMBO | Sim | `"happyhorse-1.1-i2v"`<br>`"happyhorse-1.0-i2v"` |
| `first_frame` | Imagem do primeiro quadro. A proporção de aspecto da saída é derivada desta imagem. | IMAGE | Sim | mín. 300×300 px; proporção 1:2.5 a 2.5:1 |
| `seed` | Semente a ser usada para a geração. (padrão: 0) | INT | Não | 0 a 2147483647 |
| `watermark` | Indica se deve adicionar uma marca d'água gerada por IA ao resultado. (opção avançada; padrão: False) | BOOLEAN | Não | True / False |

### Entradas de happyhorse-1.1-i2v e happyhorse-1.0-i2v

Ambas as versões do modelo compartilham o mesmo conjunto de parâmetros.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt que descreve os elementos e as características visuais. Suporta inglês e chinês. (padrão: "") | STRING | Não | N/A |
| `resolution` | A resolução do vídeo de saída. (padrão: "720P") | COMBO | Sim | `"720P"`<br>`"1080P"` |
| `duration` | A duração do vídeo gerado em segundos. (padrão: 5) | INT | Sim | 3 a 15 |

Nota: a imagem `first_frame` deve ter pelo menos 300x300 pixels, e sua proporção de aspecto deve estar entre 1:2.5 e 2.5:1.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `video` | O arquivo de vídeo gerado. | VIDEO |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseImageToVideoApi/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4bf6eece0d1b4104ce2d84e29b2c918a0a6ba782da1dd801b66cbfa1666d150b`
