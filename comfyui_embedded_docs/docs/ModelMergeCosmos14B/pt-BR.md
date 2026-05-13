> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmos14B/pt-BR.md)

O nó **ModelMergeCosmos14B** mescla dois modelos de IA usando uma abordagem baseada em blocos, projetada especificamente para a arquitetura do modelo Cosmos 14B. Ele permite combinar diferentes componentes dos modelos ajustando valores de peso entre 0.0 e 1.0 para cada bloco do modelo e camada de incorporação.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Faixa | Descrição |
|-----------|---------------|-------------|-------|-----------|
| `model1` | MODEL | Sim | - | Primeiro modelo a ser mesclado |
| `model2` | MODEL | Sim | - | Segundo modelo a ser mesclado |
| `pos_embedder.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o componente de incorporador de posição (padrão: 1.0) |
| `extra_pos_embedder.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o componente de incorporador de posição extra (padrão: 1.0) |
| `x_embedder.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o componente de incorporador x (padrão: 1.0) |
| `t_embedder.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o componente de incorporador t (padrão: 1.0) |
| `affline_norm.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o componente de normalização afim (padrão: 1.0) |
| `blocks.block0.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco 0 (padrão: 1.0) |
| `blocks.block1.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco 1 (padrão: 1.0) |
| `blocks.block2.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco 2 (padrão: 1.0) |
| `blocks.block3.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco 3 (padrão: 1.0) |
| `blocks.block4.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco 4 (padrão: 1.0) |
| `blocks.block5.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco 5 (padrão: 1.0) |
| `blocks.block6.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco 6 (padrão: 1.0) |
| `blocks.block7.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco 7 (padrão: 1.0) |
| `blocks.block8.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco 8 (padrão: 1.0) |
| `blocks.block9.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco 9 (padrão: 1.0) |
| `blocks.block10.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco 10 (padrão: 1.0) |
| `blocks.block11.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco 11 (padrão: 1.0) |
| `blocks.block12.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco 12 (padrão: 1.0) |
| `blocks.block13.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco 13 (padrão: 1.0) |
| `blocks.block14.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco 14 (padrão: 1.0) |
| `blocks.block15.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco 15 (padrão: 1.0) |
| `blocks.block16.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco 16 (padrão: 1.0) |
| `blocks.block17.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco 17 (padrão: 1.0) |
| `blocks.block18.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco 18 (padrão: 1.0) |
| `blocks.block19.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco 19 (padrão: 1.0) |
| `blocks.block20.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco 20 (padrão: 1.0) |
| `blocks.block21.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco 21 (padrão: 1.0) |
| `blocks.block22.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco 22 (padrão: 1.0) |
| `blocks.block23.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco 23 (padrão: 1.0) |
| `blocks.block24.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco 24 (padrão: 1.0) |
| `blocks.block25.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco 25 (padrão: 1.0) |
| `blocks.block26.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco 26 (padrão: 1.0) |
| `blocks.block27.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco 27 (padrão: 1.0) |
| `blocks.block28.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco 28 (padrão: 1.0) |
| `blocks.block29.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco 29 (padrão: 1.0) |
| `blocks.block30.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco 30 (padrão: 1.0) |
| `blocks.block31.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco 31 (padrão: 1.0) |
| `blocks.block32.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco 32 (padrão: 1.0) |
| `blocks.block33.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco 33 (padrão: 1.0) |
| `blocks.block34.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco 34 (padrão: 1.0) |
| `blocks.block35.` | FLOAT | Sim | 0.0 - 1.0 | Peso para o bloco 35 (padrão: 1.0) |
| `final_layer.` | FLOAT | Sim | 0.0 - 1.0 | Peso para a camada final (padrão: 1.0) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `model` | MODEL | O modelo mesclado combinando características de ambos os modelos de entrada |

---
**Source fingerprint (SHA-256):** `6fcb4fefe7738d0addef49d386c0d3d22cda4c68f0e49ad003d1df595cf0e9d9`
