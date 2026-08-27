# ModelSamplingAuraFlow

O nó ModelSamplingAuraFlow aplica uma configuração de amostragem especializada a modelos de difusão, projetada especificamente para arquiteturas de modelo AuraFlow. Ele modifica o comportamento de amostragem do modelo ao aplicar um valor de deslocamento que ajusta a distribuição de amostragem. Este nó herda do framework de amostragem de modelo SD3 e oferece controle fino sobre o processo de amostragem.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo de difusão ao qual será aplicada a configuração de amostragem AuraFlow | MODEL | Sim | - |
| `deslocamento` | O valor de deslocamento a ser aplicado à distribuição de amostragem (padrão: 1.73, passo: 0.01) | FLOAT | Sim | 0.0 - 100.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo modificado com a configuração de amostragem AuraFlow aplicada | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingAuraFlow/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7ca35632ae73517c78aa31a528492427c9af37862322ff7335f895c597ee1709`
