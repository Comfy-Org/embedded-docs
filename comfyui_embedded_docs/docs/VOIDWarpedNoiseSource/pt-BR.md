# VOIDWarpedNoiseSource

Este nó converte um LATENT (como a saída do nó VOIDWarpedNoise) em uma fonte de NOISE. Isso permite alimentar ruído distorcido pré-calculado em nós que esperam uma fonte de ruído, como o SamplerCustomAdvanced.

## Entradas

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `warped_noise` | Latent de ruído distorcido do VOIDWarpedNoise | LATENT | Sim | N/A |

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `NOISE` | Uma fonte de ruído que envolve o latent fornecido, utilizável com SamplerCustomAdvanced | NOISE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoiseSource/pt-BR.md)

---
**Source fingerprint (SHA-256):** `61d7c82cb8a2acba28f980c4c42c6d4be12788b27676a5d30885799cf9c36185`
