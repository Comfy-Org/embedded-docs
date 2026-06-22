# BatchImagesMasksLatentsNode

O nó Batch Images/Masks/Latents combina múltiplas entradas do mesmo tipo em um único lote. Ele detecta automaticamente se as entradas são imagens, máscaras ou representações latentes e utiliza o método de agrupamento apropriado. Isso é útil para preparar vários itens para processamento por nós que aceitam entradas em lote.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `inputs` | Uma lista dinâmica de entradas a serem combinadas em um lote. Você pode adicionar entre 1 e 50 itens. Todos os itens devem ser do mesmo tipo (todas imagens, todas máscaras ou todos latentes). | IMAGE, MASK ou LATENT | Sim | 1 a 50 entradas |

**Nota:** O nó determina automaticamente o tipo de dado (IMAGE, MASK ou LATENT) com base no primeiro item da lista `inputs`. Todos os itens subsequentes devem corresponder a esse tipo. O nó falhará se você tentar misturar tipos de dados diferentes.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `output` | Uma única saída em lote. O tipo de dado corresponde ao tipo de entrada (IMAGE em lote, MASK em lote ou LATENT em lote). | IMAGE, MASK ou LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchImagesMasksLatentsNode/pt-BR.md)

---
**Source fingerprint (SHA-256):** `6f3037bc00fd8526f42ad2d79a0f27434f58bd6dd0338a585cc707a771ac0989`
