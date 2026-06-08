O nó LTXVLatentUpsampler aumenta a resolução espacial de uma representação latente de vídeo por um fator de dois. Ele utiliza um modelo de upscale especializado para processar os dados latentes, que são primeiro desnormalizados e depois renormalizados usando as estatísticas de canal do VAE fornecido. Este nó é projetado para fluxos de trabalho de vídeo no espaço latente.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `samples` | A representação latente de entrada do vídeo a ser ampliada. | LATENT | Sim |  |
| `upscale_model` | O modelo carregado usado para realizar o upscale de 2x nos dados latentes. | LATENT_UPSCALE_MODEL | Sim |  |
| `vae` | O modelo VAE usado para desnormalizar os latentes de entrada antes do upscale e para normalizar os latentes de saída após o processo. | VAE | Sim |  |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `LATENT` | A representação latente ampliada, com dimensões espaciais duplicadas em comparação com a entrada. O latente de saída mantém o mesmo tamanho de lote, número de canais e duração temporal da entrada. O `noise_mask` da entrada, se presente, é removido da saída. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVLatentUpsampler/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b2c726d3a3e4881eee7e1d3bae8c478adf01cd87a9652be882579f4e26c1536f`
