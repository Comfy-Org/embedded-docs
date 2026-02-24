> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmos7B/pt-BR.md)

O nó ModelMergeCosmos7B mescla dois modelos de IA usando uma combinação ponderada de componentes específicos. Ele permite um controle refinado sobre como diferentes partes dos modelos são combinadas, ajustando pesos individuais para embeddings de posição, blocos do transformador e camadas finais.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Sim | - | Primeiro modelo a ser mesclado |
| `model2` | MODEL | Sim | - | Segundo modelo a ser mesclado |
| `pos_embedder.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o componente de incorporação de posição (padrão: 1.0) |
| `extra_pos_embedder.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o componente de incorporação de posição extra (padrão: 1.0) |
| `x_embedder.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o componente de incorporação X (padrão: 1.0) |
| `t_embedder.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o componente de incorporação T (padrão: 1.0) |
| `affline_norm.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o componente de normalização afim (padrão: 1.0) |
| `blocks.block0.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco do transformador 0 (padrão: 1.0) |
| `blocks.block1.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco do transformador 1 (padrão: 1.0) |
| `blocks.block2.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco do transformador 2 (padrão: 1.0) |
| `blocks.block3.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco do transformador 3 (padrão: 1.0) |
| `blocks.block4.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco do transformador 4 (padrão: 1.0) |
| `blocks.block5.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco do transformador 5 (padrão: 1.0) |
| `blocks.block6.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco do transformador 6 (padrão: 1.0) |
| `blocks.block7.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco do transformador 7 (padrão: 1.0) |
| `blocks.block8.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco do transformador 8 (padrão: 1.0) |
| `blocks.block9.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco do transformador 9 (padrão: 1.0) |
| `blocks.block10.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco do transformador 10 (padrão: 1.0) |
| `blocks.block11.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco do transformador 11 (padrão: 1.0) |
| `blocks.block12.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco do transformador 12 (padrão: 1.0) |
| `blocks.block13.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco do transformador 13 (padrão: 1.0) |
| `blocks.block14.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco do transformador 14 (padrão: 1.0) |
| `blocks.block15.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco do transformador 15 (padrão: 1.0) |
| `blocks.block16.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco do transformador 16 (padrão: 1.0) |
| `blocks.block17.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco do transformador 17 (padrão: 1.0) |
| `blocks.block18.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco do transformador 18 (padrão: 1.0) |
| `blocks.block19.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco do transformador 19 (padrão: 1.0) |
| `blocks.block20.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco do transformador 20 (padrão: 1.0) |
| `blocks.block21.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco do transformador 21 (padrão: 1.0) |
| `blocks.block22.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco do transformador 22 (padrão: 1.0) |
| `blocks.block23.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco do transformador 23 (padrão: 1.0) |
| `blocks.block24.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco do transformador 24 (padrão: 1.0) |
| `blocks.block25.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco do transformador 25 (padrão: 1.0) |
| `blocks.block26.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco do transformador 26 (padrão: 1.0) |
| `blocks.block27.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco do transformador 27 (padrão: 1.0) |
| `final_layer.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o componente da camada final (padrão: 1.0) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo mesclado, combinando características de ambos os modelos de entrada |
