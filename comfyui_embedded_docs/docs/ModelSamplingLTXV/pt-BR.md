# ModelSamplingLTXV

O nó ModelSamplingLTXV aplica parâmetros avançados de amostragem a um modelo com base na contagem de tokens. Ele calcula um valor de deslocamento (shift) usando interpolação linear entre os valores de deslocamento base e máximo, com o cálculo dependendo do número de tokens presentes no latente de entrada. Em seguida, o nó cria uma configuração especializada de amostragem de modelo e a aplica ao modelo de entrada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo de entrada para aplicar os parâmetros de amostragem | MODEL | Sim | - |
| `deslocamento_máx` | O valor máximo de deslocamento usado no cálculo de interpolação linear (padrão: 2.05) | FLOAT | Sim | 0.0 a 100.0 (passo: 0.01) |
| `deslocamento_base` | O valor base de deslocamento usado no cálculo de interpolação linear (padrão: 0.95) | FLOAT | Sim | 0.0 a 100.0 (passo: 0.01) |
| `latente` | Entrada latente opcional usada para determinar a contagem de tokens para o cálculo do deslocamento. Se não for fornecida, uma contagem de tokens padrão de 4096 é usada | LATENT | Não | - |

O valor de deslocamento é calculado interpolando entre `base_shift` e `max_shift` em uma faixa de tokens de 1024 a 4096. Quando um `latent` é fornecido, a contagem de tokens é calculada a partir do produto de suas dimensões espaciais (como altura e largura). Se nenhum `latent` for fornecido, a contagem de tokens assume o valor padrão de 4096.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo modificado com os parâmetros de amostragem aplicados | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingLTXV/pt-BR.md)

---
**Source fingerprint (SHA-256):** `aba596c5478e9d6ee821eec1eca15506935bcc765a368087ccc442fc2ed6671b`
