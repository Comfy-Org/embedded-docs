# SD_4XUpscale_Conditioning

O nó SD_4XUpscale_Conditioning prepara dados de condicionamento para ampliar imagens usando modelos de difusão. Ele recebe imagens de entrada e dados de condicionamento e, em seguida, aplica escala e aumento de ruído para criar um condicionamento modificado que orienta o processo de ampliação. O nó gera tanto condicionamento positivo quanto negativo, juntamente com representações latentes para as dimensões ampliadas.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `images` | Imagens de entrada a serem ampliadas | IMAGE | Sim | - |
| `positive` | Dados de condicionamento positivo que orientam a geração em direção ao conteúdo desejado | CONDITIONING | Sim | - |
| `negative` | Dados de condicionamento negativo que afastam a geração de conteúdo indesejado | CONDITIONING | Sim | - |
| `scale_ratio` | Fator de escala aplicado às imagens de entrada (padrão: 4.0) | FLOAT | Sim | 0.0 - 10.0 |
| `noise_augmentation` | Quantidade de ruído a ser adicionada durante o processo de ampliação (padrão: 0.0) | FLOAT | Sim | 0.0 - 1.0 |

As dimensões alvo da ampliação são calculadas multiplicando as dimensões das imagens de entrada por `scale_ratio`. A imagem incorporada ao condicionamento e a latente de saída são criadas a um quarto dessas dimensões alvo.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `positive` | Condicionamento positivo modificado com informações de ampliação aplicadas | CONDITIONING |
| `negative` | Condicionamento negativo modificado com informações de ampliação aplicadas | CONDITIONING |
| `latent` | Representação latente vazia correspondente às dimensões ampliadas | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SD_4XUpscale_Conditioning/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f215e890bd86f42d4da9c6f575fc92e65844e2e2056c5610310d8089e5d61902`
