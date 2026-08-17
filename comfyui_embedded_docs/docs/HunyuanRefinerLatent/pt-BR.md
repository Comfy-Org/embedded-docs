# HunyuanRefinerLatent

O nó HunyuanRefinerLatent processa entradas de condicionamento e latente para operações de refinamento. Ele aplica aumento de ruído tanto ao condicionamento positivo quanto ao negativo, incorporando dados de imagem latente, e gera uma nova saída latente com dimensões específicas para processamento adicional.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `positive` | A entrada de condicionamento positivo a ser processada | CONDITIONING | Sim | - |
| `negative` | A entrada de condicionamento negativo a ser processada | CONDITIONING | Sim | - |
| `latent` | A entrada de representação latente | LATENT | Sim | - |
| `noise_augmentation` | A quantidade de aumento de ruído a ser aplicada (padrão: 0.10, passo: 0.01, parâmetro avançado) | FLOAT | Sim | 0.0 - 1.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | O condicionamento positivo processado, com aumento de ruído aplicado e concatenação de imagem latente | CONDITIONING |
| `negative` | O condicionamento negativo processado, com aumento de ruído aplicado e concatenação de imagem latente | CONDITIONING |
| `latent` | Um novo latente preenchido com zeros, com o mesmo tamanho de lote e os mesmos tamanhos das três últimas dimensões do `latent` de entrada, mas com 32 canais | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanRefinerLatent/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4c5669cf2ad5ba00e176876741b7d8d3f092cc58d2163871a10fd769ee4ff84c`
