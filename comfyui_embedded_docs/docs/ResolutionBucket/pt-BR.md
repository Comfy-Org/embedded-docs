# Bucket de Resolução

Este nó organiza uma lista de imagens latentes e seus dados de condicionamento correspondentes por resolução. Ele agrupa itens que compartilham a mesma altura e largura, criando lotes separados para cada resolução única. Esse processo é útil para preparar dados para treinamento eficiente, pois permite que os modelos processem vários itens do mesmo tamanho juntos.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `latentes` | Lista de dicionários latentes a serem agrupados por resolução. | LATENT | Sim | N/A |
| `condicionamento` | Lista de listas de condicionamento (deve corresponder ao comprimento de `latents`). | CONDITIONING | Sim | N/A |

**Nota:** Ambas as entradas são do tipo lista, o que significa que o nó recebe uma lista de itens para cada uma. O número de itens na lista `latents` deve corresponder exatamente ao número de itens na lista `conditioning`; se as contagens não corresponderem, o nó gera um erro. Cada dicionário latente pode conter um lote de amostras, e a lista de condicionamento correspondente deve conter um número correspondente de itens de condicionamento para esse lote, pois cada amostra no lote é pareada com sua própria entrada de condicionamento. Amostras latentes podem ter um formato de (B, C, H, W) para imagens ou (B, T, C, H, W) para vídeos; o nó as agrupa apenas por altura e largura.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `latents` | Lista de dicionários latentes em lote, um por grupo de resolução. | LATENT |
| `conditioning` | Lista de listas de condicionamento, uma por grupo de resolução. | CONDITIONING |

**Nota:** Ambas as saídas são do tipo lista. Cada lista de saída contém uma entrada por resolução única (altura e largura) encontrada na entrada, na ordem em que as resoluções foram encontradas pela primeira vez. Os latentes dentro de cada grupo são empilhados ao longo de uma nova dimensão de lote.

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionBucket/pt-BR.md)

---
**Source fingerprint (SHA-256):** `11687f9916895136c7c5b8146cd7519cbf6c296720e453bac52fe4da237403cd`
