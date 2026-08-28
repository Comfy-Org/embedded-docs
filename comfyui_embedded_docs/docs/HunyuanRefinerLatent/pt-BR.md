# HunyuanRefinerLatent

O nó HunyuanRefinerLatent prepara dados de conditioning e latent para o processo de refinamento de vídeo Hunyuan. Ele anexa os dados da imagem latent de entrada ao conditioning positivo e ao negativo, aplica um valor de aumento de ruído a eles e cria um novo latent preenchido com zeros, com 32 canais, para processamento adicional.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positivo` | A entrada de conditioning positivo a ser processada | CONDITIONING | Sim | - |
| `negativo` | A entrada de conditioning negativo a ser processada | CONDITIONING | Sim | - |
| `latente` | A entrada de representação latent, usada como dados de imagem latent para o conditioning e para definir as dimensões do latent de saída | LATENT | Sim | - |
| `aumento_de_ruído` | A quantidade de aumento de ruído a ser aplicada (padrão: 0,10). Este parâmetro é exibido na seção avançada do nó. | FLOAT | Sim | 0.0 - 1.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positivo` | O conditioning positivo processado, com os dados da imagem latent anexados e o aumento de ruído aplicado | CONDITIONING |
| `negativo` | O conditioning negativo processado, com os dados da imagem latent anexados e o aumento de ruído aplicado | CONDITIONING |
| `latente` | Um novo latent preenchido com zeros, com o mesmo tamanho de lote e as mesmas três últimas dimensões do latent de entrada, e 32 canais | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanRefinerLatent/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4c5669cf2ad5ba00e176876741b7d8d3f092cc58d2163871a10fd769ee4ff84c`
