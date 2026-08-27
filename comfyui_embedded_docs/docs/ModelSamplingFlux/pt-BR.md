# ModelSamplingFlux

O nó ModelSamplingFlux aplica a amostragem de modelo Flux a um determinado modelo, calculando um parâmetro de deslocamento com base nas dimensões da imagem. Ele cria uma configuração de amostragem especializada que ajusta o comportamento do modelo de acordo com os parâmetros de largura, altura e deslocamento especificados e, em seguida, retorna o modelo modificado com as novas configurações de amostragem aplicadas.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo ao qual aplicar a amostragem Flux | MODEL | Sim | - |
| `deslocamento_máx` | Valor máximo de deslocamento para o cálculo da amostragem (padrão: 1.15) | FLOAT | Sim | 0.0 - 100.0 (passo 0.01) |
| `deslocamento_base` | Valor base de deslocamento para o cálculo da amostragem (padrão: 0.5) | FLOAT | Sim | 0.0 - 100.0 (passo 0.01) |
| `largura` | Largura da imagem de destino em pixels (padrão: 1024) | INT | Sim | 16 - MAX_RESOLUTION (passo 8) |
| `altura` | Altura da imagem de destino em pixels (padrão: 1024) | INT | Sim | 16 - MAX_RESOLUTION (passo 8) |

`max_shift` e `base_shift` são parâmetros avançados. O deslocamento aplicado à configuração de amostragem é calculado a partir das dimensões da imagem: a resolução latente é calculada como `width × height / 256`, e o valor do deslocamento é interpolado entre `base_shift` em uma resolução latente de 256 e `max_shift` em uma resolução latente de 4096.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo modificado com a configuração de amostragem Flux aplicada | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingFlux/pt-BR.md)

---
**Source fingerprint (SHA-256):** `04065b54ace30a2b20476ed085df871ea89794650e98ae30c40f750357663834`
