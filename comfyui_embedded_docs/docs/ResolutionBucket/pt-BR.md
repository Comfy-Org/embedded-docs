# Bucket de Resolução

Este nó organiza uma lista de imagens latentes e seus dados de condicionamento correspondentes por resolução. Ele agrupa itens que compartilham a mesma altura e largura, criando lotes separados para cada resolução única. Esse processo é útil para preparar dados para treinamento eficiente, pois permite que os modelos processem vários itens do mesmo tamanho juntos.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `latentes` | Lista de dicionários latentes para agrupar por resolução. | LATENT | Sim | N/A |
| `condicionamento` | Lista de listas de condicionamento (deve corresponder ao comprimento dos latentes). | CONDITIONING | Sim | N/A |

**Nota:** O número de itens na lista `latents` deve corresponder exatamente ao número de itens na lista `conditioning`. Cada dicionário latente pode conter um lote de amostras, e a lista de condicionamento correspondente deve conter um número correspondente de itens de condicionamento para esse lote.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `latentes` | Lista de dicionários latentes em lote, um por grupo de resolução. | LATENT |
| `condicionamento` | Lista de listas de condicionamento, uma por grupo de resolução. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionBucket/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2858de5f0827812002ca72ba5d7ce56411d1ef97e9a12a65fc4bea193a1a0ec0`
