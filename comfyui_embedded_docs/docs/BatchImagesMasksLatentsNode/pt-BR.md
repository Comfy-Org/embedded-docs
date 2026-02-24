> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchImagesMasksLatentsNode/pt-BR.md)

O nó Batch Images/Masks/Latents combina múltiplas entradas do mesmo tipo em um único lote (batch). Ele detecta automaticamente se as entradas são imagens, máscaras ou representações latentes e usa o método de agrupamento apropriado. Isso é útil para preparar vários itens para processamento por nós que aceitam entradas em lote.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `inputs` | IMAGE, MASK ou LATENT | Sim | 1 a 50 entradas | Uma lista dinâmica de entradas a serem combinadas em um lote. Você pode adicionar entre 1 e 50 itens. Todos os itens devem ser do mesmo tipo (todas imagens, todas máscaras ou todos latentes). |

**Observação:** O nó determina automaticamente o tipo de dado (IMAGE, MASK ou LATENT) com base no primeiro item da lista `inputs`. Todos os itens subsequentes devem corresponder a esse tipo. O nó falhará se você tentar misturar tipos de dados diferentes.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `output` | IMAGE, MASK ou LATENT | Uma única saída em lote. O tipo de dado corresponde ao tipo de entrada (IMAGE em lote, MASK em lote ou LATENT em lote). |
