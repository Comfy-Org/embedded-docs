# ModelSamplingLTXV

O nó ModelSamplingLTXV aplica parâmetros avançados de amostragem a um modelo com base na contagem de tokens. Ele calcula um valor de shift interpolando linearmente entre `base_shift` e `max_shift` em um intervalo de tokens e, em seguida, aplica um patch ao modelo de entrada com uma configuração de amostragem especializada. Se um `latent` for fornecido, suas dimensões determinam a contagem de tokens; caso contrário, são usados 4096 tokens.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo de entrada ao qual aplicar os parâmetros de amostragem. | MODEL | Sim | - |
| `max_shift` | O valor máximo de shift usado no cálculo de interpolação linear (padrão: 2.05). | FLOAT | Sim | 0.0 a 100.0 (passo: 0.01) |
| `base_shift` | O valor base de shift usado no cálculo de interpolação linear (padrão: 0.95). | FLOAT | Sim | 0.0 a 100.0 (passo: 0.01) |
| `latent` | Entrada latent opcional usada para determinar a contagem de tokens para o cálculo do shift. Se não for fornecida, uma contagem padrão de 4096 tokens será usada. | LATENT | Não | - |

O valor de shift é calculado por interpolação entre `base_shift` em 1024 tokens e `max_shift` em 4096 tokens. Quando `latent` é fornecido, a contagem de tokens é o produto de todas as dimensões após as duas primeiras nas amostras de latent (as dimensões espaciais/temporais). Se nenhum `latent` for fornecido, a contagem de tokens usa 4096 como padrão.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo modificado com os parâmetros de amostragem aplicados. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingLTXV/pt-BR.md)

---
**Source fingerprint (SHA-256):** `aba596c5478e9d6ee821eec1eca15506935bcc765a368087ccc442fc2ed6671b`
