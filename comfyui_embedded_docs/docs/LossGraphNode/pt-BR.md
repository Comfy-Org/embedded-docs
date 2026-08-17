# Plotar Gráfico de Loss

O LossGraphNode cria um gráfico visual dos valores de loss de treinamento ao longo do tempo e o exibe como uma imagem de pré-visualização. Ele recebe dados de loss de processos de treinamento e gera um gráfico de linha mostrando como o loss muda ao longo das etapas de treinamento. O gráfico resultante inclui rótulos de eixos e valores de loss mínimo/máximo.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `loss` | Mapa de loss do nó de treinamento. Deve conter uma chave `loss` com uma lista de valores de loss usados para plotar o gráfico. | LOSS_MAP | Sim | - |
| `filename_prefix` | Prefixo para a imagem do gráfico de loss salvo. (padrão: "loss_graph") | STRING | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `ui.images` | A imagem do gráfico de loss gerado, exibida como pré-visualização. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LossGraphNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b1f0b72a03d4ce2d9461fc6e312bd1e847455f7dd5227667876a945494ea8cdb`
