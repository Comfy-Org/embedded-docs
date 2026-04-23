> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKVCache/pt-BR.md)

O nó Flux KV Cache aplica uma otimização de Cache de Chave-Valor (KV) em modelos da família Flux. Essa otimização é projetada especificamente para melhorar o desempenho ao usar imagens de referência, armazenando em cache determinados cálculos, o que pode acelerar o processo de geração.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|--------------|-------------|-------|-----------|
| `model` | MODEL | Sim | | O modelo no qual aplicar o Cache KV. |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `model` | MODEL | O modelo modificado com o Cache KV ativado. |