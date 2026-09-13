# ModelSamplingStableCascade

O nó ModelSamplingStableCascade aplica configurações de amostragem do stable cascade a um modelo, aplicando um valor de deslocamento aos parâmetros de amostragem. Ele retorna uma cópia corrigida do modelo de entrada com a configuração personalizada de amostragem do stable cascade, deixando o modelo original inalterado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo de entrada ao qual aplicar a amostragem do stable cascade | MODEL | Sim | - |
| `shift` | O valor de deslocamento aplicado aos parâmetros de amostragem (padrão: 2.0) | FLOAT | Sim | 0.0 - 100.0 (passo 0.01) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo modificado com a amostragem do stable cascade aplicada | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingStableCascade/pt-BR.md)

---
**Source fingerprint (SHA-256):** `358681a7c698d4335cde60780d5a8b134b75df4ea40102bf51544c53bbb08c42`
