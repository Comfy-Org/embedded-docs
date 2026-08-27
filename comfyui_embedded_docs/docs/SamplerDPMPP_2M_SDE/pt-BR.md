# SamplerDPMPP_2M_SDE

O nó SamplerDPMPP_2M_SDE cria um amostrador DPM++ 2M SDE para modelos de difusão. Este amostrador usa solucionadores de equações diferenciais de segunda ordem com equações diferenciais estocásticas para gerar amostras. Ele fornece diferentes tipos de solucionadores e opções de manipulação de ruído para controlar o processo de amostragem.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `tipo_de_solvedor` | O tipo de solucionador de equações diferenciais a ser usado no processo de amostragem (padrão: "midpoint") | COMBO | Sim | `"midpoint"`<br>`"heun"` |
| `eta` | Controla a estocasticidade do processo de amostragem (padrão: 1.0) | FLOAT | Sim | 0.0 - 100.0 |
| `s_ruído` | Controla a quantidade de ruído adicionada durante a amostragem (padrão: 1.0) | FLOAT | Sim | 0.0 - 100.0 |
| `dispositivo_de_ruído` | O dispositivo onde os cálculos de ruído são realizados. Quando definido como "cpu", o amostrador usa geração de ruído baseada na CPU; quando definido como "gpu", usa geração de ruído baseada na GPU para um desempenho potencialmente mais rápido (padrão: "gpu") | COMBO | Sim | `"gpu"`<br>`"cpu"` |

Nota: `eta`, `s_noise` e `noise_device` são marcados como parâmetros avançados e aparecem na seção avançada da interface do nó.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `sampler` | Um objeto de amostrador configurado, pronto para uso no pipeline de amostragem. | SAMPLER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2M_SDE/pt-BR.md)

---
**Source fingerprint (SHA-256):** `42f5f098fa7573ca8a1a6085b72675ee6cb0ae8e7865c5793a815a6ef2495f82`
