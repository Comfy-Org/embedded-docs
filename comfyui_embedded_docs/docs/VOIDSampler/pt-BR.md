# VOIDSampler

## Visão Geral

O nó VOIDSampler fornece um método de amostragem DDIM especializado, projetado especificamente para modelos de inpaint VOID. Ele implementa o mesmo processo de remoção de ruído usado durante o treinamento do modelo VOID, sem a escala de ruído aplicada pelos KSamplers padrão. Este nó é destinado ao uso com os nós SamplerCustom ou SamplerCustomAdvanced e deve ser emparelhado com RandomNoise ou VOIDWarpedNoiseSource.

## Entradas

Este nó não possui parâmetros de entrada configuráveis. É um amostrador autocontido que aplica um algoritmo de amostragem DDIM fixo.

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| *Sem entradas* | Este nó não aceita nenhum parâmetro de entrada. | - | - | - |

Nota: Os modelos VOID foram treinados com o diffusers CogVideoXDDIMScheduler, que opera no espaço alfa onde o desvio padrão de entrada é aproximadamente 1. O KSampler padrão aplica uma escala de ruído que multiplica por cerca de 4500x, o que é incompatível com esse treinamento. O VOIDSampler ignora essa escala e implementa a regra de atualização DDIM diretamente usando a conversão sigma-alfa.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `SAMPLER` | Um objeto de amostrador que implementa o algoritmo DDIM do VOID, pronto para ser conectado aos nós SamplerCustom ou SamplerCustomAdvanced. | SAMPLER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDSampler/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b8bb6d3d7220cca4a6dd252efe9c92953b1c5c67c14365e5e0583bc9bdb133be`
