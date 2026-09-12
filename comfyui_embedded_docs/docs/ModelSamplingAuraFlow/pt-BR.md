# ModelSamplingAuraFlow

O nó ModelSamplingAuraFlow aplica uma configuração de amostragem especializada a modelos de difusão, projetada especificamente para arquiteturas de modelo AuraFlow. Ele modifica o comportamento de amostragem do modelo aplicando um valor de deslocamento que ajusta a distribuição de amostragem. Este nó herda da estrutura de amostragem do modelo SD3 e fornece controle refinado sobre o processo de amostragem.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo de difusão ao qual aplicar a configuração de amostragem do AuraFlow | MODEL | Sim | - |
| `deslocamento` | O valor de deslocamento a aplicar à distribuição de amostragem (padrão: 1.73, passo: 0.01) | FLOAT | Sim | 0.0 - 100.0 |
| `sampling` | O modo de amostragem usado ao aplicar patch ao modelo (padrão: "flow"). Marcado como uma opção avançada. | COMBO | Não | "flow"<br>"img_to_img_velocity" |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo modificado com a configuração de amostragem do AuraFlow aplicada | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingAuraFlow/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5c1381d2dec9ac84a7ee6cd134de444ab50f657eafd960263c63a055d0a139d6`
