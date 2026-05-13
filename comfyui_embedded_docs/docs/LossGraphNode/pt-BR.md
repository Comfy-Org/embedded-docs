> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LossGraphNode/pt-BR.md)

O nó LossGraphNode cria um gráfico visual dos valores de perda de treinamento ao longo do tempo e o exibe como uma imagem de pré-visualização. Ele recebe dados de perda de processos de treinamento e gera um gráfico de linhas mostrando como a perda muda ao longo das etapas de treinamento. O gráfico resultante inclui rótulos nos eixos e os valores mínimo e máximo de perda.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `loss` | LOSS_MAP | Sim | - | Mapa de perda do nó de treinamento. |
| `filename_prefix` | STRING | Sim | - | Prefixo para a imagem salva do gráfico de perda. (padrão: "loss_graph") |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `ui.images` | IMAGE | A imagem do gráfico de perda gerada, exibida como pré-visualização. |

---
**Source fingerprint (SHA-256):** `9b1c844cb4babafc61102ee7bfd1039c325c6665abff1721d92a6da7d18029f9`
