# Normalizar Imagens

Este nó normaliza uma imagem de entrada subtraindo um valor médio especificado de cada pixel e depois dividindo o resultado por um desvio padrão especificado. Esta é uma etapa comum de pré-processamento para padronizar os valores dos pixels e preparar os dados da imagem para processamento adicional.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `image` | A imagem de entrada a ser normalizada. | IMAGE | Sim | - |
| `mean` | Valor médio para normalização (padrão: 0.5). | FLOAT | Não | 0.0 - 1.0 |
| `std` | Desvio padrão para normalização (padrão: 0.5). | FLOAT | Não | 0.001 - 1.0 |

Nota: A normalização é aplicada a todo o lote de imagens de uma só vez, e qualquer tamanho de lote é suportado.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `image` | A imagem resultante após o processo de normalização ter sido aplicado. | IMAGE |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeImages/pt-BR.md)

---
**Source fingerprint (SHA-256):** `927451ed275254d87e42b52919143ee2f3d9833a2aa5b43c7315d798871f9a2d`
