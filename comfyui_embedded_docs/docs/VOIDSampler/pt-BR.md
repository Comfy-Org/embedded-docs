# VOIDSampler

VOIDSampler é um sampler DDIM especializado para modelos de inpaint VOID. Ele implementa o mesmo processo de denoising com o qual o VOID foi treinado, sem a escala de ruído que os KSamplers padrão aplicam. Use este nó com SamplerCustom ou SamplerCustomAdvanced, em conjunto com RandomNoise ou VOIDWarpedNoiseSource.

## Entradas

Este nó não possui parâmetros de entrada configuráveis. É um sampler autocontido que aplica um algoritmo de amostragem DDIM fixo.

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| *Sem entradas* | Este nó não aceita nenhum parâmetro de entrada. | - | - | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `SAMPLER` | Um objeto de sampler que implementa o algoritmo DDIM do VOID, pronto para ser conectado aos nós SamplerCustom ou SamplerCustomAdvanced. | SAMPLER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDSampler/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b8bb6d3d7220cca4a6dd252efe9c92953b1c5c67c14365e5e0583bc9bdb133be`
