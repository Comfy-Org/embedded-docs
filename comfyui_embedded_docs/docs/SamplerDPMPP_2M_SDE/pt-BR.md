# SamplerDPMPP_2M_SDE

O nó SamplerDPMPP_2M_SDE cria um amostrador DPM++ 2M SDE para modelos de difusão. Este amostrador utiliza solucionadores de equações diferenciais de segunda ordem com equações diferenciais estocásticas para gerar amostras. Ele oferece diferentes tipos de solucionadores e opções de tratamento de ruído para controlar o processo de amostragem.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `tipo_de_solvedor` | O tipo de solucionador de equação diferencial a ser usado no processo de amostragem | STRING | Sim | `"midpoint"`<br>`"heun"` |
| `eta` | Controla a estocasticidade do processo de amostragem (padrão: 1.0) | FLOAT | Sim | 0.0 - 100.0 |
| `s_ruído` | Controla a quantidade de ruído adicionada durante a amostragem (padrão: 1.0) | FLOAT | Sim | 0.0 - 100.0 |
| `dispositivo_de_ruído` | O dispositivo onde os cálculos de ruído são realizados. Quando definido como "cpu", o amostrador usa geração de ruído baseada em CPU; quando definido como "gpu", usa geração de ruído baseada em GPU para desempenho potencialmente mais rápido | STRING | Sim | `"gpu"`<br>`"cpu"` |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `sampler` | Um objeto amostrador configurado pronto para uso no pipeline de amostragem | SAMPLER |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2M_SDE/pt-BR.md)

---
**Source fingerprint (SHA-256):** `4a6a16e3494e8270f3707e172f252e7fc4e1b65efbecd3dd086b1a1edc5ba23a`
