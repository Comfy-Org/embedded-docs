# LTXVLatentUpsampler

O nó LTXVLatentUpsampler aumenta a resolução espacial de uma representação latente de vídeo por um fator de dois. Ele usa um modelo de ampliação especializado para processar os dados latentes, que são primeiro desnormalizados e depois renormalizados usando as estatísticas de canais do VAE fornecido. Este nó é projetado para fluxos de trabalho de vídeo no espaço latente.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `samples` | A representação latente de entrada do vídeo a ser ampliado. | LATENT | Sim |  |
| `upscale_model` | O modelo carregado usado para realizar a ampliação 2x nos dados latentes. | LATENT_UPSCALE_MODEL | Sim |  |
| `vae` | O modelo VAE usado para desnormalizar os latentes de entrada antes da ampliação e para normalizar os latentes de saída depois. | VAE | Sim |  |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `LATENT` | A representação latente ampliada, com dimensões espaciais duplicadas em relação à entrada. O latente de saída tem o mesmo tamanho de lote, número de canais e comprimento temporal que a entrada, e é convertido de volta para o mesmo tipo de dados dos latentes de entrada. O `noise_mask` da entrada, se presente, é removido da saída. | LATENT |

Nota: Este nó é marcado como experimental.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVLatentUpsampler/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7d7f0b733cb3758e9ec985cac30134d719b130b5b86c35bfdd14576a5b4575db`
