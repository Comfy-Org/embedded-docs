# Escalar ROPE

O nó ScaleROPE permite modificar a Incorporação Posicional Rotativa (ROPE) de um modelo aplicando fatores separados de escala e deslocamento aos seus componentes X, Y e T (tempo). É um nó avançado e experimental usado para ajustar o comportamento da codificação posicional do modelo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo cujos parâmetros ROPE serão modificados. | MODEL | Sim | - |
| `escala_x` | O fator de escala a ser aplicado ao componente X do ROPE (padrão: 1.0). | FLOAT | Sim | 0.0 - 100.0 (step 0.1) |
| `deslocamento_x` | O valor de deslocamento a ser aplicado ao componente X do ROPE (padrão: 0.0). | FLOAT | Sim | -256.0 - 256.0 (step 0.1) |
| `escala_y` | O fator de escala a ser aplicado ao componente Y do ROPE (padrão: 1.0). | FLOAT | Sim | 0.0 - 100.0 (step 0.1) |
| `deslocamento_y` | O valor de deslocamento a ser aplicado ao componente Y do ROPE (padrão: 0.0). | FLOAT | Sim | -256.0 - 256.0 (step 0.1) |
| `escala_t` | O fator de escala a ser aplicado ao componente T (tempo) do ROPE (padrão: 1.0). | FLOAT | Sim | 0.0 - 100.0 (step 0.1) |
| `deslocamento_t` | O valor de deslocamento a ser aplicado ao componente T (tempo) do ROPE (padrão: 0.0). | FLOAT | Sim | -256.0 - 256.0 (step 0.1) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo com os novos parâmetros de escala e deslocamento ROPE aplicados. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ScaleROPE/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5d5ab0182b78c8c12ceaf44685a91e666ce15fa099fd194e3605bbdb9cc3c961`
