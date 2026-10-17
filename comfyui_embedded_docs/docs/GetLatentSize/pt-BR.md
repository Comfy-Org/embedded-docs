# Get Image/Video Latent Size

Lê um latent de imagem ou vídeo e retorna sua largura, altura, contagem de quadros e tamanho do lote, para que a geometria possa ser reutilizada sem decodificar o latent. Use-o para dimensionar máscaras de ruído, alinhar resoluções ou calcular sobreposições ao fazer tiling de um sampler. Os valores medidos também são impressos no próprio nó.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `latent` | O latent de imagem ou vídeo a inspecionar. Quando o latent contém vários fluxos, o primeiro é medido. | LATENT | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `width` | A largura do latent, em células latentes em vez de pixels. | INT |
| `height` | A altura do latent, em células latentes em vez de pixels. | INT |
| `frames` | O número de quadros no latent. Latents de imagem têm um único quadro. | INT |
| `batch_size` | O número de latents no lote. | INT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetLatentSize/pt-BR.md)

---
**Source fingerprint (SHA-256):** `f75b3347cb1853b035b0bb283d5487ab1532d561d66d3cae3c67f54bf693d31a`
