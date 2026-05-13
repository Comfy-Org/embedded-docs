> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionBucket/pt-BR.md)

Este nó organiza uma lista de imagens latentes e seus dados de condicionamento correspondentes por resolução. Ele agrupa itens que compartilham a mesma altura e largura, criando lotes separados para cada resolução única. Esse processo é útil para preparar dados para treinamento eficiente, pois permite que os modelos processem vários itens do mesmo tamanho juntos.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|-----------|----------|-------|-------------|
| `latents` | LATENT | Sim | N/A | Lista de dicionários latentes para agrupar por resolução. |
| `conditioning` | CONDITIONING | Sim | N/A | Lista de listas de condicionamento (deve corresponder ao comprimento dos latentes). |

**Nota:** O número de itens na lista `latents` deve corresponder exatamente ao número de itens na lista `conditioning`. Cada dicionário latente pode conter um lote de amostras, e a lista de condicionamento correspondente deve conter um número correspondente de itens de condicionamento para esse lote.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `latents` | LATENT | Lista de dicionários latentes em lote, um por grupo de resolução. |
| `conditioning` | CONDITIONING | Lista de listas de condicionamento, uma por grupo de resolução. |

---
**Source fingerprint (SHA-256):** `2858de5f0827812002ca72ba5d7ce56411d1ef97e9a12a65fc4bea193a1a0ec0`
