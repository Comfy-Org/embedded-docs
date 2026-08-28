# Bucket de Resolução

Este nó organiza uma lista de imagens latentes e seus dados de condicionamento correspondentes por resolução. Ele agrupa itens que compartilham a mesma altura e largura, criando lotes separados para cada resolução exclusiva. Esse processo é útil para preparar dados para treinamento eficiente, pois permite que os modelos processem vários itens do mesmo tamanho juntos.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `latentes` | Lista de dicionários de latentes para agrupar por resolução. | LATENT | Sim | N/A |
| `condicionamento` | Lista de listas de condicionamento (deve corresponder ao comprimento de latents). | CONDITIONING | Sim | N/A |

**Nota:** O número de itens na lista `latents` deve corresponder exatamente ao número de itens na lista `conditioning`. Se as contagens não corresponderem, o nó gera um erro. Cada dicionário de latentes pode conter um lote de amostras, e a lista de condicionamento correspondente deve conter um número correspondente de itens de condicionamento para esse lote. As amostras latentes podem ter a forma (B, C, H, W) para imagens ou (B, T, C, H, W) para vídeos; o nó as agrupa apenas por altura e largura.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `latentes` | Lista de dicionários de latentes em lote, um por grupo de resolução. | LATENT |
| `condicionamento` | Lista de listas de condicionamento, uma por grupo de resolução. | CONDITIONING |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionBucket/pt-BR.md)

---
**Source fingerprint (SHA-256):** `11687f9916895136c7c5b8146cd7519cbf6c296720e453bac52fe4da237403cd`
