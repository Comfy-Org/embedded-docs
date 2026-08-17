# VOIDWarpedNoiseSource

## Visão Geral

Este nó converte um LATENT (como a saída do nó VOIDWarpedNoise) em uma fonte de NOISE. Isso permite usar o ruído distorcido com o nó SamplerCustomAdvanced para uma geração de imagens mais controlada.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `warped_noise` | Ruído distorcido latente do VOIDWarpedNoise | LATENT | Sim | N/A |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `NOISE` | Uma fonte de ruído que pode ser usada com o SamplerCustomAdvanced | NOISE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoiseSource/pt-BR.md)

---
**Source fingerprint (SHA-256):** `61d7c82cb8a2acba28f980c4c42c6d4be12788b27676a5d30885799cf9c36185`
