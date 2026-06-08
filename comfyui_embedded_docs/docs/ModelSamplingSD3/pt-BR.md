O nó ModelSamplingSD3 aplica parâmetros de amostragem do Stable Diffusion 3 a um modelo. Ele modifica o comportamento de amostragem do modelo ajustando o parâmetro de deslocamento (*shift*), que controla as características da distribuição de amostragem. O nó cria uma cópia modificada do modelo de entrada com a configuração de amostragem especificada aplicada.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo de entrada para aplicar os parâmetros de amostragem do SD3 | MODEL | Sim | - |
| `deslocamento` | Controla o parâmetro de deslocamento da amostragem (padrão: 3.0) | FLOAT | Sim | 0.0 - 100.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `modelo` | O modelo modificado com os parâmetros de amostragem do SD3 aplicados | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingSD3/pt-BR.md)

---
**Source fingerprint (SHA-256):** `aa2172d578badffb0a728308b0d3aae4d048db074336963965264d5e512a0d93`
