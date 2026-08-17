# SamplerDPMPP_3M_SDE

O nó SamplerDPMPP_3M_SDE cria um amostrador DPM++ 3M SDE para uso no processo de amostragem. Este amostrador utiliza um método de equação diferencial estocástica multietapa de terceira ordem com parâmetros de ruído configuráveis. O nó permite escolher se os cálculos de ruído são executados na GPU ou na CPU.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `eta` | Controla a estocasticidade do processo de amostragem (padrão: 1.0) | FLOAT | Sim | 0.0 - 100.0 |
| `s_noise` | Controla a quantidade de ruído adicionada durante a amostragem (padrão: 1.0) | FLOAT | Sim | 0.0 - 100.0 |
| `noise_device` | Seleciona o dispositivo para cálculos de ruído, seja GPU ou CPU (padrão: "gpu") | COMBO | Sim | "gpu"<br>"cpu" |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `sampler` | Retorna um objeto de amostrador configurado para uso em fluxos de trabalho de amostragem. | SAMPLER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_3M_SDE/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0f624398c67e50639fc41384b50b91bab93797bd785dda25f1f5fc649e46825b`
