# ModelSamplingStableCascade

O nó ModelSamplingStableCascade aplica amostragem em cascata estável a um modelo, ajustando os parâmetros de amostragem com um valor de deslocamento. Ele cria uma versão modificada do modelo de entrada com uma configuração de amostragem personalizada para geração em cascata estável.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo de entrada para aplicar a amostragem em cascata estável | MODEL | Sim | - |
| `deslocamento` | O valor de deslocamento a ser aplicado aos parâmetros de amostragem (padrão: 2.0) | FLOAT | Sim | 0.0 - 100.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `modelo` | O modelo modificado com amostragem em cascata estável aplicada | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingStableCascade/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2d0a342fff05434c8fe78999187bd31dbee7deb6f4447759a489102a8ce277de`
