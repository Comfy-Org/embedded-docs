# ModelSamplingSD3

Este nó aplica configurações de amostragem no estilo Stable Diffusion 3 a um modelo. Ele faz uma cópia do modelo e substitui seu método de amostragem por uma configuração de amostragem baseada em fluxo que usa o valor `shift` fornecido, o qual controla como a distribuição de amostragem é moldada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo de entrada ao qual aplicar os parâmetros de amostragem SD3 | MODEL | Sim | - |
| `deslocamento` | Controla o parâmetro de deslocamento de amostragem (padrão: 3.0) | FLOAT | Sim | 0.0 - 100.0 (passo: 0.01) |

Observação: o valor de `shift` é aplicado junto com um multiplicador interno fixo de 1000. Se o modelo original tiver uma configuração de escala de ruído, esse valor será transferido para o modelo modificado. O modelo original não é alterado; uma cópia clonada e modificada é retornada.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo modificado com parâmetros de amostragem SD3 aplicados | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingSD3/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a77e38c2cebf6f21f841a953ec5c59096eaf60ffc205c24f34f635e54c5718cb`
