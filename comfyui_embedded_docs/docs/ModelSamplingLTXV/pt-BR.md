# ModelSamplingLTXV

O nó ModelSamplingLTXV aplica parâmetros avançados de amostragem a um modelo com base na contagem de tokens. Ele calcula um valor de deslocamento (shift) usando uma interpolação linear entre os valores de deslocamento base e máximo, com o cálculo dependendo do número de tokens no latent de entrada. O nó então cria uma configuração especializada de amostragem de modelo e a aplica ao modelo de entrada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo de entrada ao qual aplicar os parâmetros de amostragem | MODEL | Sim | - |
| `max_shift` | O valor máximo de deslocamento usado no cálculo de interpolação linear. O valor de deslocamento é igual a esse máximo em 4096 tokens (padrão: 2.05) | FLOAT | Sim | 0.0 to 100.0 |
| `base_shift` | O valor base de deslocamento usado no cálculo de interpolação linear. O valor de deslocamento é igual a essa base em 1024 tokens (padrão: 0.95) | FLOAT | Sim | 0.0 to 100.0 |
| `latent` | Entrada latent opcional usada para determinar a contagem de tokens para o cálculo do deslocamento. A contagem de tokens é o produto das dimensões espaciais das amostras latentes. Se não for fornecida, uma contagem padrão de 4096 tokens é usada | LATENT | Não | - |

Nota: O valor de deslocamento é calculado por interpolação linear entre `base_shift` em 1024 tokens e `max_shift` em 4096 tokens. Quando nenhum `latent` é fornecido, a contagem padrão de 4096 tokens faz o deslocamento ser igual a `max_shift`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo modificado com os parâmetros de amostragem aplicados | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingLTXV/pt-BR.md)

---
**Source fingerprint (SHA-256):** `aba596c5478e9d6ee821eec1eca15506935bcc765a368087ccc442fc2ed6671b`
