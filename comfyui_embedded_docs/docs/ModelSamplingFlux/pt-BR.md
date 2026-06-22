# ModelSamplingFlux

O nó ModelSamplingFlux aplica a amostragem do modelo Flux a um modelo fornecido, calculando um parâmetro de deslocamento com base nas dimensões da imagem. Ele cria uma configuração de amostragem especializada que ajusta o comportamento do modelo de acordo com os parâmetros de largura, altura e deslocamento especificados, retornando o modelo modificado com as novas configurações de amostragem aplicadas.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `modelo` | O modelo ao qual aplicar a amostragem Flux | MODEL | Sim | - |
| `deslocamento_máx` | Valor máximo de deslocamento para o cálculo da amostragem (padrão: 1,15) | FLOAT | Sim | 0,0 - 100,0 |
| `deslocamento_base` | Valor base de deslocamento para o cálculo da amostragem (padrão: 0,5) | FLOAT | Sim | 0,0 - 100,0 |
| `largura` | Largura da imagem alvo em pixels (padrão: 1024) | INT | Sim | 16 - RESOLUÇÃO_MÁXIMA |
| `altura` | Altura da imagem alvo em pixels (padrão: 1024) | INT | Sim | 16 - RESOLUÇÃO_MÁXIMA |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `modelo` | O modelo modificado com a configuração de amostragem Flux aplicada | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingFlux/pt-BR.md)

---
**Source fingerprint (SHA-256):** `35733ab0cd032884ceada13715cf51e626586844e8e575471a5ba7cf8a1e5e49`
