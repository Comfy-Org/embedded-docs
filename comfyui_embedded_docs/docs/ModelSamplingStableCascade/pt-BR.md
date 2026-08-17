# ModelSamplingStableCascade

O nó ModelSamplingStableCascade aplica amostragem em cascata estável a um modelo ajustando os parâmetros de amostragem com um valor de deslocamento. Ele cria um clone modificado do modelo de entrada com uma configuração de amostragem personalizada para a geração em cascata estável.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model` | O modelo de entrada ao qual aplicar a amostragem em cascata estável | MODEL | Sim | - |
| `shift` | O valor de deslocamento (shift) a aplicar aos parâmetros de amostragem (padrão: 2.0) | FLOAT | Sim | 0.0 - 100.0 (passo: 0.01) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model` | O modelo modificado com a amostragem em cascata estável aplicada | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingStableCascade/pt-BR.md)

---
**Source fingerprint (SHA-256):** `358681a7c698d4335cde60780d5a8b134b75df4ea40102bf51544c53bbb08c42`
