# LatentCutToBatch

O nó LatentCutToBatch divide uma representação latente ao longo de uma dimensão escolhida em várias fatias e as empilha em um novo lote. Isso permite processar diferentes partes de uma amostra latente de forma independente.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `samples` | A representação latente a ser dividida e agrupada em lote. | LATENT | Sim | - |
| `dim` | A dimensão ao longo da qual cortar as amostras latentes. `"t"` refere-se à dimensão temporal, `"x"` à largura e `"y"` à altura. | COMBO | Sim | `"t"`<br>`"x"`<br>`"y"` |
| `slice_size` | O tamanho de cada fatia a ser cortada da dimensão especificada. Se o tamanho da dimensão não for perfeitamente divisível por esse valor, o restante é descartado. (padrão: 1) | INT | Sim | 1 a 16384 (resolução máxima) |

Observação: Se a dimensão selecionada for o eixo do lote ou do canal, a entrada é retornada inalterada. Se `slice_size` for maior que o tamanho da dimensão, a dimensão inteira é usada como uma única fatia.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `samples` | O lote latente resultante, contendo as amostras fatiadas e empilhadas. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCutToBatch/pt-BR.md)

---
**Source fingerprint (SHA-256):** `873c9bc8391971887f1ab636c086cab86f5504a9c653bc80b54120ee53980bdf`
