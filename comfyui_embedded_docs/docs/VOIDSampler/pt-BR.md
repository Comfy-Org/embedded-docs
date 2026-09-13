# VOIDSampler

VOIDSampler é um amostrador DDIM especializado, projetado para modelos de inpainting VOID. Ele reproduz o processo exato de remoção de ruído com o qual o VOID foi treinado, ignorando o escalonamento de ruído que os KSamplers padrão aplicam. Use este nó em conjunto com SamplerCustom ou SamplerCustomAdvanced, emparelhado com RandomNoise ou VOIDWarpedNoiseSource.

## Entradas

Este nó não possui parâmetros de entrada configuráveis. É um amostrador autocontido que aplica um algoritmo fixo de amostragem DDIM.

| Parâmetro | Descrição | Tipo de dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| *Nenhuma entrada* | Este nó não aceita parâmetros de entrada. | - | - | - |

## Saídas

| Nome da saída | Descrição | Tipo de dados |
| --- | --- | --- |
| `SAMPLER` | Um objeto amostrador que implementa o algoritmo DDIM do VOID, pronto para ser conectado aos nós SamplerCustom ou SamplerCustomAdvanced. | SAMPLER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDSampler/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b8bb6d3d7220cca4a6dd252efe9c92953b1c5c67c14365e5e0583bc9bdb133be`
