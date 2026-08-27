# Editor de Curva

O nó Curve Editor fornece uma interface visual para ajustar e refinar uma curva. Você pode modificar o formato de uma curva de entrada diretamente na interface do nó e, opcionalmente, exibir um histograma ao lado dela para referência visual. O nó suporta saída intermediária durante a edição, permitindo que você veja resultados em tempo real enquanto faz alterações, e gera a curva modificada para uso em outras partes do seu fluxo de trabalho.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `curva` | A curva de entrada a ser editada. | CURVE | Sim | N/A |
| `histograma` | Um histograma opcional para exibir ao lado da curva como referência visual. | HISTOGRAM | Não | N/A |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `curva` | A curva editada após os ajustes feitos na interface do nó. | CURVE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CurveEditor/pt-BR.md)

---
**Source fingerprint (SHA-256):** `6c4459998b1a3dd3a53f84cb1c231c448c64aa55b96444bc4ac7470556a3b915`
