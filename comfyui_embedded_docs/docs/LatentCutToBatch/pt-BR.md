> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCutToBatch/pt-BR.md)

O nó LatentCutToBatch divide uma representação latente ao longo de uma dimensão escolhida em múltiplos segmentos e os empilha em um novo lote. Isso permite processar diferentes partes de uma amostra latente de forma independente.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|--------------|-------------|-----------|-----------|
| `amostras` | LATENT | Sim | - | A representação latente a ser dividida e agrupada em lote. |
| `dimensão` | COMBO | Sim | `"t"`<br>`"x"`<br>`"y"` | A dimensão ao longo da qual cortar as amostras latentes. `"t"` refere-se à dimensão temporal, `"x"` à largura e `"y"` à altura. |
| `tamanho_do_fatiamento` | INT | Sim | 1 a 16384 | O tamanho de cada segmento a ser cortado da dimensão especificada. Se o tamanho da dimensão não for perfeitamente divisível por este valor, o restante é descartado. (padrão: 1) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|---------------|--------------|-----------|
| `amostras` | LATENT | O lote latente resultante, contendo as amostras fatiadas e empilhadas. |

---
**Source fingerprint (SHA-256):** `38d0ace3ef91e47e3f047aa7057c61e09b6534702526b34691b4bc239c933cd3`
