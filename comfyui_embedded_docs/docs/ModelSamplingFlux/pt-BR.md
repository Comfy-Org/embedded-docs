# ModelSamplingFlux

O nó ModelSamplingFlux aplica a amostragem do modelo Flux a um modelo fornecido, calculando um parâmetro de deslocamento (shift) com base nas dimensões da imagem. Ele cria uma configuração de amostragem especializada que ajusta o comportamento do modelo de acordo com os parâmetros de largura, altura e deslocamento especificados e, em seguida, retorna o modelo modificado com as novas configurações de amostragem aplicadas.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model` | O modelo ao qual aplicar a amostragem Flux | MODEL | Sim | - |
| `max_shift` | Valor máximo de deslocamento para o cálculo da amostragem (padrão: 1,15) | FLOAT | Sim | 0.0 - 100.0 |
| `base_shift` | Valor base de deslocamento para o cálculo da amostragem (padrão: 0,5) | FLOAT | Sim | 0.0 - 100.0 |
| `width` | Largura da imagem de destino em pixels (padrão: 1024) | INT | Sim | 16 - MAX_RESOLUTION |
| `height` | Altura da imagem de destino em pixels (padrão: 1024) | INT | Sim | 16 - MAX_RESOLUTION |

O valor efetivo de deslocamento é interpolado entre `base_shift` e `max_shift` com base no tamanho latente derivado de `width` e `height`. O valor de `step` é 0,01 para `max_shift` e `base_shift`, e 8 para `width` e `height`. Os parâmetros `max_shift` e `base_shift` são marcados como opções avançadas na interface do usuário.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model` | O modelo modificado com a configuração de amostragem Flux aplicada | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingFlux/pt-BR.md)

---
**Source fingerprint (SHA-256):** `04065b54ace30a2b20476ed085df871ea89794650e98ae30c40f750357663834`
