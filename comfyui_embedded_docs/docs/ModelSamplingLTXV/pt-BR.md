> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingLTXV/pt-BR.md)

O nó ModelSamplingLTXV aplica parâmetros avançados de amostragem a um modelo com base na contagem de tokens. Ele calcula um valor de deslocamento usando uma interpolação linear entre os valores de deslocamento base e máximo, com o cálculo dependendo do número de tokens no latent de entrada. Em seguida, o nó cria uma configuração especializada de amostragem de modelo e a aplica ao modelo de entrada.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `model` | MODEL | Sim | - | O modelo de entrada ao qual aplicar os parâmetros de amostragem |
| `max_shift` | FLOAT | Sim | 0.0 a 100.0 | O valor máximo de deslocamento usado no cálculo da interpolação linear (padrão: 2,05) |
| `base_shift` | FLOAT | Sim | 0.0 a 100.0 | O valor base de deslocamento usado no cálculo da interpolação linear (padrão: 0,95) |
| `latent` | LATENT | Não | - | Entrada latent opcional usada para determinar a contagem de tokens para o cálculo do deslocamento. Se não for fornecida, uma contagem padrão de 4096 tokens é usada |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `model` | MODEL | O modelo modificado com os parâmetros de amostragem aplicados |

---
**Source fingerprint (SHA-256):** `2325754df1b2541a6adbdebecefde92e08535af0e179d7444093a61eb35cb24c`
