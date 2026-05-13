> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoiseSource/pt-BR.md)

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoiseSource/en.md)

## Visão Geral

Este nó converte um LATENT (como a saída do nó VOIDWarpedNoise) em uma fonte de NOISE. Isso permite que você use o ruído distorcido com o nó SamplerCustomAdvanced para uma geração de imagem mais controlada.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `warped_noise` | LATENT | Sim | N/A | Ruído distorcido latente do VOIDWarpedNoise |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `NOISE` | NOISE | Uma fonte de ruído que pode ser usada com o SamplerCustomAdvanced |

---
**Source fingerprint (SHA-256):** `ff798d223da5cf705a40ad1f36cc403030105331d0cc4173e9553cd3718c5d93`
