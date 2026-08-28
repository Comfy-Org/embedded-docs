# Normalizar Imagens

Este nó ajusta os valores de pixel de uma imagem de entrada usando um processo matemático de normalização. Ele subtrai um valor médio especificado de cada pixel e depois divide o resultado por um desvio padrão especificado. Esta é uma etapa comum de pré-processamento para preparar dados de imagem para outros modelos de aprendizado de máquina.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `image` | A imagem de entrada a ser normalizada. | IMAGE | Sim | - |
| `mean` | Valor médio para normalização (padrão: 0.5). | FLOAT | Não | 0.0 - 1.0 |
| `std` | Desvio padrão para normalização (padrão: 0.5). | FLOAT | Não | 0.001 - 1.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `images` | A imagem resultante após o processo de normalização ter sido aplicado. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeImages/pt-BR.md)

---
**Source fingerprint (SHA-256):** `927451ed275254d87e42b52919143ee2f3d9833a2aa5b43c7315d798871f9a2d`
