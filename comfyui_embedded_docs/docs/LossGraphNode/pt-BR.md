# Plotar Gráfico de Loss

O `LossGraphNode` cria um gráfico de linhas dos valores de perda de treinamento ao longo das etapas de treinamento e o exibe como uma imagem de pré-visualização. Ele lê os valores de perda de um nó de treinamento, plota-os em um gráfico com eixos rotulados e valores mínimo e máximo de perda, e retorna o gráfico como uma pré-visualização de imagem na interface.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `loss` | Mapa de perda do nó de treinamento. Deve conter uma chave `loss` com uma lista de valores numéricos de perda. | LOSS_MAP | Sim | - |
| `filename_prefix` | Prefixo para a imagem do gráfico de perda salvo. (padrão: "loss_graph") | STRING | Sim | - |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `ui.images` | A imagem do gráfico de perda gerada exibida como pré-visualização. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LossGraphNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b1f0b72a03d4ce2d9461fc6e312bd1e847455f7dd5227667876a945494ea8cdb`
