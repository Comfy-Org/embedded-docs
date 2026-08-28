# ModelSamplingSD3

O nó ModelSamplingSD3 aplica parâmetros de amostragem do Stable Diffusion 3 a um modelo. Ele modifica o comportamento de amostragem do modelo ajustando o parâmetro shift, que controla as características da distribuição de amostragem. O nó cria uma cópia modificada do modelo de entrada com a configuração de amostragem especificada aplicada.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo de entrada para aplicar os parâmetros de amostragem do SD3 | MODEL | Sim | - |
| `deslocamento` | Controla o parâmetro shift da amostragem (padrão: 3.0) | FLOAT | Sim | 0.0 - 100.0 (step: 0.01) |

Nota: O nó aplica o valor de `shift` com um multiplicador interno fixo de 1000. Se o modelo original tiver uma configuração de escala de ruído, ela será preservada no modelo modificado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model` | O modelo modificado com os parâmetros de amostragem do SD3 aplicados | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingSD3/pt-BR.md)

---
**Source fingerprint (SHA-256):** `46d44786422c2efea78c1fe7e1183cebc9bf51d4f13861da04d5a974b5b6da7d`
