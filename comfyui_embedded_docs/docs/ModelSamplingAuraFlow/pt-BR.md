# ModelSamplingAuraFlow

O nó ModelSamplingAuraFlow aplica uma configuração de amostragem especializada a modelos de difusão, projetada especificamente para arquiteturas de modelo AuraFlow. Ele modifica o comportamento de amostragem do modelo ao aplicar um parâmetro `shift` que ajusta a distribuição de amostragem. Este nó herda do framework de amostragem de modelos SD3 e fornece controle refinado sobre o processo de amostragem.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-----------|---------------|-------------|-------|
| `model` | O modelo de difusão no qual aplicar a configuração de amostragem AuraFlow. | MODEL | Sim | - |
| `shift` | O valor de shift a ser aplicado à distribuição de amostragem. Padrão: 1.73. Passo: 0.01. | FLOAT | Sim | 0.0 - 100.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-----------|---------------|
| `model` | O modelo modificado com a configuração de amostragem AuraFlow aplicada. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingAuraFlow/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7ca35632ae73517c78aa31a528492427c9af37862322ff7335f895c597ee1709`
