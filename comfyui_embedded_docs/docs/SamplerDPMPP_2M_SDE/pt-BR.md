# SamplerDPMPP_2M_SDE

O nó SamplerDPMPP_2M_SDE cria um sampler DPM++ 2M SDE para modelos de difusão. Este sampler combina um solucionador multietapa de segunda ordem com ruído de equação diferencial estocástica (SDE) para gerar amostras. Ele fornece diferentes tipos de solucionador e opções de manipulação de ruído para controlar o processo de amostragem.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `solver_type` | O tipo de solucionador de equação diferencial a ser usado durante a amostragem: "midpoint" ou "heun" (padrão: "midpoint") | COMBO | Sim | "midpoint"<br>"heun" |
| `eta` | Controla a quantidade de estocasticidade (aleatoriedade) no processo de amostragem (padrão: 1.0) | FLOAT | Sim | 0.0 - 100.0 |
| `s_noise` | Controla a quantidade de ruído adicionada durante a amostragem (padrão: 1.0) | FLOAT | Sim | 0.0 - 100.0 |
| `noise_device` | O dispositivo usado para cálculos de ruído. "gpu" realiza a geração de ruído na GPU para um desempenho potencialmente mais rápido; "cpu" usa a CPU (padrão: "gpu") | COMBO | Sim | "gpu"<br>"cpu" |

Nota: Quando `noise_device` está definido como "cpu", o nó cria o sampler `dpmpp_2m_sde`. Quando definido como "gpu", ele cria a variante `dpmpp_2m_sde_gpu`, que realiza os cálculos relacionados ao ruído na GPU.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `sampler` | Um objeto de sampler configurado pronto para uso no pipeline de amostragem | SAMPLER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2M_SDE/pt-BR.md)

---
**Source fingerprint (SHA-256):** `42f5f098fa7573ca8a1a6085b72675ee6cb0ae8e7865c5793a815a6ef2495f82`
