# SamplerDPMPP_SDE

O SamplerDPMPP_SDE cria um amostrador DPM++ SDE (Equação Diferencial Estocástica) para uso no processo de amostragem. Este amostrador fornece um método de amostragem estocástica com parâmetros de ruído configuráveis e seleção de dispositivo. Ele retorna um objeto de amostrador que pode ser usado no pipeline de amostragem.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `eta` | Controla a estocasticidade do processo de amostragem (padrão: 1.0) | FLOAT | Sim | 0.0 - 100.0 |
| `s_noise` | Controla a quantidade de ruído adicionada durante a amostragem (padrão: 1.0) | FLOAT | Sim | 0.0 - 100.0 |
| `r` | Um parâmetro que influencia o comportamento da amostragem (padrão: 0.5) | FLOAT | Sim | 0.0 - 100.0 |
| `noise_device` | Seleciona o dispositivo onde os cálculos de ruído são realizados. Quando definido como "cpu", o amostrador `dpmpp_sde` é criado; quando definido como "gpu", o amostrador `dpmpp_sde_gpu` é criado (padrão: "gpu") | COMBO | Sim | "gpu"<br>"cpu" |

Nota: Todas as entradas são marcadas como parâmetros avançados. A seleção de `noise_device` altera qual variante do amostrador é criada: "cpu" corresponde a `dpmpp_sde` e "gpu" corresponde a `dpmpp_sde_gpu`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `sampler` | Retorna um objeto de amostrador DPM++ SDE configurado para uso em pipelines de amostragem | SAMPLER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_SDE/pt-BR.md)

---
**Source fingerprint (SHA-256):** `56949712f245abfcc48c09d7d14a1a7778e80ba58535e538484c382d7e0d02c6`
