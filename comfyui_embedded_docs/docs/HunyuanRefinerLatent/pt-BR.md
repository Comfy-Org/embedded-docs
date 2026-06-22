# HunyuanRefinerLatent

O nó HunyuanRefinerLatent processa entradas de condicionamento e latentes para operações de refinamento. Ele aplica aumento de ruído tanto no condicionamento positivo quanto no negativo, incorporando dados de imagem latente, e gera uma nova saída latente com dimensões específicas para processamento adicional.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `positivo` | A entrada de condicionamento positivo a ser processada | CONDITIONING | Sim | - |
| `negativo` | A entrada de condicionamento negativo a ser processada | CONDITIONING | Sim | - |
| `latente` | A representação latente de entrada | LATENT | Sim | - |
| `aumento_de_ruído` | A quantidade de aumento de ruído a ser aplicada (padrão: 0.10) | FLOAT | Sim | 0.0 - 1.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `positivo` | O condicionamento positivo processado com aumento de ruído aplicado e concatenação de imagem latente | CONDITIONING |
| `negativo` | O condicionamento negativo processado com aumento de ruído aplicado e concatenação de imagem latente | CONDITIONING |
| `latente` | Uma nova saída latente com dimensões [batch_size, 32, altura, largura, canais] | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanRefinerLatent/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f097b58f1948e5c0801f81b51a5189619695a6afa189368aff4c64b126fc5ce5`
