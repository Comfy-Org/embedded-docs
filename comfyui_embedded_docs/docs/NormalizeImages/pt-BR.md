> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeImages/pt-BR.md)

Este nó ajusta os valores dos pixels de uma imagem de entrada usando um processo matemático de normalização. Ele subtrai um valor médio especificado de cada pixel e, em seguida, divide o resultado por um desvio padrão especificado. Esta é uma etapa comum de pré-processamento para preparar dados de imagem para outros modelos de aprendizado de máquina.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `image` | IMAGE | Sim | - | A imagem de entrada a ser normalizada. |
| `mean` | FLOAT | Não | 0.0 - 1.0 | Valor médio para normalização (padrão: 0.5). |
| `std` | FLOAT | Não | 0.001 - 1.0 | Desvio padrão para normalização (padrão: 0.5). |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `image` | IMAGE | A imagem resultante após o processo de normalização ter sido aplicado. |

---
**Source fingerprint (SHA-256):** `9d08c8dba7d13c6f255ed786d3d2d3005bce425dc04b14b7199d868c3fc81fd9`
