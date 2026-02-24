> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmos14B/pt-BR.md)

O nó ModelMergeCosmos14B mescla dois modelos de IA usando uma abordagem baseada em blocos projetada especificamente para a arquitetura do modelo Cosmos 14B. Ele permite combinar diferentes componentes dos modelos ajustando valores de peso entre 0.0 e 1.0 para cada bloco do modelo e camada de incorporação (embedding).

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Sim | - | Primeiro modelo a ser mesclado |
| `model2` | MODEL | Sim | - | Segundo modelo a ser mesclado |
| `pos_embedder.` | FLOAT | Sim | 0.0 - 1.0 | Peso do incorporador de posição (padrão: 1.0) |
| `extra_pos_embedder.` | FLOAT | Sim | 0.0 - 1.0 | Peso do incorporador de posição extra (padrão: 1.0) |
| `x_embedder.` | FLOAT | Sim | 0.0 - 1.0 | Peso do incorporador X (padrão: 1.0) |
| `t_embedder.` | FLOAT | Sim | 0.0 - 1.0 | Peso do incorporador T (padrão: 1.0) |
| `affline_norm.` | FLOAT | Sim | 0.0 - 1.0 | Peso da normalização afim (padrão: 1.0) |
| `blocks.block0.` | FLOAT | Sim | 0.0 - 1.0 | Peso do Bloco 0 (padrão: 1.0) |
| `blocks.block1.` | FLOAT | Sim | 0.0 - 1.0 | Peso do Bloco 1 (padrão: 1.0) |
| `blocks.block2.` | FLOAT | Sim | 0.0 - 1.0 | Peso do Bloco 2 (padrão: 1.0) |
| `blocks.block3.` | FLOAT | Sim | 0.0 - 1.0 | Peso do Bloco 3 (padrão: 1.0) |
| `blocks.block4.` | FLOAT | Sim | 0.0 - 1.0 | Peso do Bloco 4 (padrão: 1.0) |
| `blocks.block5.` | FLOAT | Sim | 0.0 - 1.0 | Peso do Bloco 5 (padrão: 1.0) |
| `blocks.block6.` | FLOAT | Sim | 0.0 - 1.0 | Peso do Bloco 6 (padrão: 1.0) |
| `blocks.block7.` | FLOAT | Sim | 0.0 - 1.0 | Peso do Bloco 7 (padrão: 1.0) |
| `blocks.block8.` | FLOAT | Sim | 0.0 - 1.0 | Peso do Bloco 8 (padrão: 1.0) |
| `blocks.block9.` | FLOAT | Sim | 0.0 - 1.0 | Peso do Bloco 9 (padrão: 1.0) |
| `blocks.block10.` | FLOAT | Sim | 0.0 - 1.0 | Peso do Bloco 10 (padrão: 1.0) |
| `blocks.block11.` | FLOAT | Sim | 0.0 - 1.0 | Peso do Bloco 11 (padrão: 1.0) |
| `blocks.block12.` | FLOAT | Sim | 0.0 - 1.0 | Peso do Bloco 12 (padrão: 1.0) |
| `blocks.block13.` | FLOAT | Sim | 0.0 - 1.0 | Peso do Bloco 13 (padrão: 1.0) |
| `blocks.block14.` | FLOAT | Sim | 0.0 - 1.0 | Peso do Bloco 14 (padrão: 1.0) |
| `blocks.block15.` | FLOAT | Sim | 0.0 - 1.0 | Peso do Bloco 15 (padrão: 1.0) |
| `blocks.block16.` | FLOAT | Sim | 0.0 - 1.0 | Peso do Bloco 16 (padrão: 1.0) |
| `blocks.block17.` | FLOAT | Sim | 0.0 - 1.0 | Peso do Bloco 17 (padrão: 1.0) |
| `blocks.block18.` | FLOAT | Sim | 0.0 - 1.0 | Peso do Bloco 18 (padrão: 1.0) |
| `blocks.block19.` | FLOAT | Sim | 0.0 - 1.0 | Peso do Bloco 19 (padrão: 1.0) |
| `blocks.block20.` | FLOAT | Sim | 0.0 - 1.0 | Peso do Bloco 20 (padrão: 1.0) |
| `blocks.block21.` | FLOAT | Sim | 0.0 - 1.0 | Peso do Bloco 21 (padrão: 1.0) |
| `blocks.block22.` | FLOAT | Sim | 0.0 - 1.0 | Peso do Bloco 22 (padrão: 1.0) |
| `blocks.block23.` | FLOAT | Sim | 0.0 - 1.0 | Peso do Bloco 23 (padrão: 1.0) |
| `blocks.block24.` | FLOAT | Sim | 0.0 - 1.0 | Peso do Bloco 24 (padrão: 1.0) |
| `blocks.block25.` | FLOAT | Sim | 0.0 - 1.0 | Peso do Bloco 25 (padrão: 1.0) |
| `blocks.block26.` | FLOAT | Sim | 0.0 - 1.0 | Peso do Bloco 26 (padrão: 1.0) |
| `blocks.block27.` | FLOAT | Sim | 0.0 - 1.0 | Peso do Bloco 27 (padrão: 1.0) |
| `blocks.block28.` | FLOAT | Sim | 0.0 - 1.0 | Peso do Bloco 28 (padrão: 1.0) |
| `blocks.block29.` | FLOAT | Sim | 0.0 - 1.0 | Peso do Bloco 29 (padrão: 1.0) |
| `blocks.block30.` | FLOAT | Sim | 0.0 - 1.0 | Peso do Bloco 30 (padrão: 1.0) |
| `blocks.block31.` | FLOAT | Sim | 0.0 - 1.0 | Peso do Bloco 31 (padrão: 1.0) |
| `blocks.block32.` | FLOAT | Sim | 0.0 - 1.0 | Peso do Bloco 32 (padrão: 1.0) |
| `blocks.block33.` | FLOAT | Sim | 0.0 - 1.0 | Peso do Bloco 33 (padrão: 1.0) |
| `blocks.block34.` | FLOAT | Sim | 0.0 - 1.0 | Peso do Bloco 34 (padrão: 1.0) |
| `blocks.block35.` | FLOAT | Sim | 0.0 - 1.0 | Peso do Bloco 35 (padrão: 1.0) |
| `final_layer.` | FLOAT | Sim | 0.0 - 1.0 | Peso da camada final (padrão: 1.0) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo mesclado que combina características de ambos os modelos de entrada |
