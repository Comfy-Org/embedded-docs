# SamplerDPMPP_3M_SDE

O nó SamplerDPMPP_3M_SDE cria um amostrador DPM++ 3M SDE para uso no processo de amostragem. Este amostrador utiliza um método de equação diferencial estocástica multietapa de terceira ordem com parâmetros de ruído configuráveis. O nó permite escolher se os cálculos de ruído são realizados na GPU ou CPU.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `eta` | Controla a estocasticidade do processo de amostragem (padrão: 1.0) | FLOAT | Sim | 0.0 - 100.0 |
| `s_noise` | Controla a quantidade de ruído adicionada durante a amostragem (padrão: 1.0) | FLOAT | Sim | 0.0 - 100.0 |
| `noise_device` | Seleciona o dispositivo para cálculos de ruído, GPU ou CPU (padrão: "gpu") | COMBO | Sim | "gpu"<br>"cpu" |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `sampler` | Retorna um objeto amostrador configurado para uso em fluxos de trabalho de amostragem | SAMPLER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_3M_SDE/pt-BR.md)

---
**Source fingerprint (SHA-256):** `817ce8c12245063e5f2f3421f57dd55801aae96dfd8fe1bf3f88f814799b830a`
