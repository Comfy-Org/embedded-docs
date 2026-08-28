# LTXVLatentUpsampler

O nó LTXVLatentUpsampler aumenta a resolução espacial de uma representação latente de vídeo por um fator de dois. Ele utiliza um modelo de upscale especializado para processar os dados latentes, que são primeiro desnormalizados e depois renormalizados usando as estatísticas de canal do VAE fornecido. Este nó é projetado para fluxos de trabalho de vídeo no espaço latente.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `samples` | A representação latente de entrada do vídeo a ser ampliada. | LATENT | Sim |  |
| `upscale_model` | O modelo carregado usado para realizar o upscale 2x nos dados latentes. | LATENT_UPSCALE_MODEL | Sim |  |
| `vae` | O modelo VAE usado para desnormalizar os latentes de entrada antes do upscale e normalizar os latentes de saída depois. | VAE | Sim |  |

Nota: Este nó é marcado como experimental no ComfyUI.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `LATENT` | A representação latente ampliada, com as dimensões espaciais dobradas em comparação com a entrada. O latente de saída tem o mesmo tamanho de lote, o mesmo número de canais e o mesmo comprimento temporal que a entrada. O `noise_mask` da entrada, se presente, é removido da saída. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVLatentUpsampler/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7d7f0b733cb3758e9ec985cac30134d719b130b5b86c35bfdd14576a5b4575db`
