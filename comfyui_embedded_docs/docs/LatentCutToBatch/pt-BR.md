# LatentCutToBatch

O nó LatentCutToBatch divide uma representação latente ao longo de uma dimensão escolhida (tempo, largura ou altura) em fatias de um tamanho especificado e as empilha em um novo lote. Cada fatia torna-se um item separado no lote, para que diferentes partes de uma amostra latente possam ser processadas independentemente.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `amostras` | A representação latente a ser dividida e agrupada em lote. | LATENT | Sim | - |
| `dimensão` | A dimensão ao longo da qual cortar as amostras latentes. `"t"` refere-se à dimensão temporal (quadros), `"x"` à largura e `"y"` à altura. | COMBO | Sim | `"t"`<br>`"x"`<br>`"y"` |
| `tamanho_do_fatiamento` | O tamanho de cada fatia a ser cortada da dimensão especificada. Se o tamanho da dimensão não for perfeitamente divisível por esse valor, o restante é descartado. (padrão: 1) | INT | Sim | 1 a 16384 (resolução máxima) |

Nota: A opção `"t"` só tem efeito quando o latente inclui uma dimensão temporal. Se a dimensão escolhida corresponder à posição do lote ou do canal, ou não existir (por exemplo, selecionar `"t"` em um latente sem quadros), o nó retorna a entrada inalterada. Se `slice_size` for maior que o tamanho da dimensão escolhida, a dimensão inteira é usada como uma única fatia. Quando o tamanho da dimensão não é uniformemente divisível por `slice_size`, a parte restante no final é descartada. O tamanho do lote de saída é o tamanho do lote de entrada multiplicado pelo número de fatias, e a própria dimensão fatiada é reduzida para `slice_size`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `samples` | O lote latente resultante, contendo as amostras fatiadas e empilhadas. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCutToBatch/pt-BR.md)

---
**Source fingerprint (SHA-256):** `873c9bc8391971887f1ab636c086cab86f5504a9c653bc80b54120ee53980bdf`
