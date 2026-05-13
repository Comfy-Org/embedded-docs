> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ShuffleDataset/pt-BR.md)

O nó Shuffle Dataset recebe uma lista de imagens e altera aleatoriamente sua ordem. Ele usa um valor de `seed` para controlar a aleatoriedade, garantindo que a mesma ordem de embaralhamento possa ser reproduzida. Isso é útil para randomizar a sequência de imagens em um conjunto de dados antes do processamento.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `imagens` | IMAGE | Sim | - | A lista de imagens a ser embaralhada. |
| `semente` | INT | Não | 0 a 18446744073709551615 | Semente aleatória. Um valor de 0 produzirá um embaralhamento diferente a cada execução. (padrão: 0) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `imagens` | IMAGE | A mesma lista de imagens, mas em uma nova ordem aleatoriamente embaralhada. |

---
**Source fingerprint (SHA-256):** `0b8442029995bdcedf1df0cb8d27d87aa529fb1021d911ed3016a6a7e788b246`
