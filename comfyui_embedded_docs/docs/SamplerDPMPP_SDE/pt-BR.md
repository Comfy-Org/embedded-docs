O nó SamplerDPMPP_SDE cria um amostrador DPM++ SDE (Equação Diferencial Estocástica) para uso no processo de amostragem. Este amostrador fornece um método de amostragem estocástica com parâmetros de ruído configuráveis e seleção de dispositivo. Ele retorna um objeto amostrador que pode ser utilizado no pipeline de amostragem.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `eta` | Controla a estocasticidade do processo de amostragem (padrão: 1.0) | FLOAT | Sim | 0.0 - 100.0 |
| `s_noise` | Controla a quantidade de ruído adicionada durante a amostragem (padrão: 1.0) | FLOAT | Sim | 0.0 - 100.0 |
| `r` | Um parâmetro que influencia o comportamento da amostragem (padrão: 0.5) | FLOAT | Sim | 0.0 - 100.0 |
| `noise_device` | Seleciona o dispositivo onde os cálculos de ruído são realizados (padrão: "gpu") | COMBO | Sim | "gpu"<br>"cpu" |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `sampler` | Retorna um objeto amostrador DPM++ SDE configurado para uso em pipelines de amostragem | SAMPLER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_SDE/pt-BR.md)

---
**Source fingerprint (SHA-256):** `43b3b3c4b2756a6e7979c12418de1dba79e3e0c0fde2a06505cf0a6825e6ebbf`
