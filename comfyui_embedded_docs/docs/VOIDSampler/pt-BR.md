# VOIDSampler

Esta documentação foi gerada por IA. Se você encontrar algum erro ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDSampler/en.md)

## Visão Geral

O nó VOIDSampler fornece um método de amostragem DDIM especializado, projetado especificamente para modelos de inpaint VOID. Ele implementa o mesmo processo de remoção de ruído utilizado durante o treinamento do modelo VOID, sem a escala de ruído que os KSamplers padrão aplicam. Este nó é destinado ao uso com nós SamplerCustom ou SamplerCustomAdvanced, e deve ser combinado com RandomNoise ou VOIDWarpedNoiseSource.

## Entradas

Este nó não possui parâmetros de entrada configuráveis. É um amostrador autocontido que aplica um algoritmo de amostragem DDIM fixo.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| *Sem entradas* | Este nó não aceita nenhum parâmetro de entrada. | - | - | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `SAMPLER` | Um objeto amostrador que implementa o algoritmo VOID DDIM, pronto para ser conectado a nós SamplerCustom ou SamplerCustomAdvanced. | SAMPLER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDSampler/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c6f1be9a90003906c54cced20e8136ab7e4f7e7118e63b67ce366eeb7f790dca`
