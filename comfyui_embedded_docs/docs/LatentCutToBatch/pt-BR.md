> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCutToBatch/pt-BR.md)

O nó LatentCutToBatch recebe uma representação latente e a divide ao longo de uma dimensão especificada em múltiplas fatias. Essas fatias são então empilhadas em uma nova dimensão de lote, convertendo efetivamente uma única amostra latente em um lote de amostras latentes menores. Isso é útil para processar diferentes partes de um espaço latente de forma independente.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `samples` | LATENT | Sim | - | A representação latente a ser dividida e processada em lote. |
| `dim` | COMBO | Sim | `"t"`<br>`"x"`<br>`"y"` | A dimensão ao longo da qual as amostras latentes serão cortadas. `"t"` refere-se à dimensão temporal, `"x"` à largura e `"y"` à altura. |
| `slice_size` | INT | Sim | 1 a 16384 | O tamanho de cada fatia a ser cortada da dimensão especificada. Se o tamanho da dimensão não for perfeitamente divisível por este valor, o restante será descartado. (padrão: 1) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `samples` | LATENT | O lote latente resultante, contendo as amostras fatiadas e empilhadas. |
