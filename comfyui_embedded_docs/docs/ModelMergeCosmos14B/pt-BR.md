# ModelMergeCosmos14B

The **ModelMergeCosmos14B** node merges two AI models using a block-based approach specifically designed for the Cosmos 14B model architecture. It allows you to blend different components of the models by adjusting weight values between 0.0 and 1.0 for each model block and embedding layer.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `model1` | Primeiro modelo a ser mesclado | MODEL | Sim | - |
| `model2` | Segundo modelo a ser mesclado | MODEL | Sim | - |
| `pos_embedder.` | Peso para o componente de embedding de posição (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `extra_pos_embedder.` | Peso para o componente de embedding de posição extra (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `x_embedder.` | Peso para o componente de embedding x (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `t_embedder.` | Peso para o componente de embedding t (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `affline_norm.` | Peso para o componente de normalização afim (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocos.bloco0.` | Peso para o bloco 0 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocos.bloco1.` | Peso para o bloco 1 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocos.bloco2.` | Peso para o bloco 2 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocos.bloco3.` | Peso para o bloco 3 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocos.bloco4.` | Peso para o bloco 4 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocos.bloco5.` | Peso para o bloco 5 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocos.bloco6.` | Peso para o bloco 6 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocos.bloco7.` | Peso para o bloco 7 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocos.bloco8.` | Peso para o bloco 8 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocos.bloco9.` | Peso para o bloco 9 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocos.bloco10.` | Peso para o bloco 10 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocos.bloco11.` | Peso para o bloco 11 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocos.bloco12.` | Peso para o bloco 12 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocos.bloco13.` | Peso para o bloco 13 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocos.bloco14.` | Peso para o bloco 14 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocos.bloco15.` | Peso para o bloco 15 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocos.bloco16.` | Peso para o bloco 16 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocos.bloco17.` | Peso para o bloco 17 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocos.bloco18.` | Peso para o bloco 18 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocos.bloco19.` | Peso para o bloco 19 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocos.bloco20.` | Peso para o bloco 20 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocos.bloco21.` | Peso para o bloco 21 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocos.bloco22.` | Peso para o bloco 22 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocos.bloco23.` | Peso para o bloco 23 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocos.bloco24.` | Peso para o bloco 24 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocos.bloco25.` | Peso para o bloco 25 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocos.bloco26.` | Peso para o bloco 26 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocos.bloco27.` | Peso para o bloco 27 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocos.bloco28.` | Peso para o bloco 28 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocos.bloco29.` | Peso para o bloco 29 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocos.bloco30.` | Peso para o bloco 30 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocos.bloco31.` | Peso para o bloco 31 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocos.bloco32.` | Peso para o bloco 32 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocos.bloco33.` | Peso para o bloco 33 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocos.bloco34.` | Peso para o bloco 34 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocos.bloco35.` | Peso para o bloco 35 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `final_layer.` | Peso para a camada final (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |

Todos os parâmetros de peso aceitam valores de 0.0 a 1.0 em incrementos de 0.01, e todos eles têm valor padrão 1.0. Os parâmetros de bloco abrangem 36 blocos transformer, numerados de `blocks.block0.` a `blocks.block35.`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `model` | O modelo mesclado, combinando características de ambos os modelos de entrada | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmos14B/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1d1e5dc176643f577723bb0bb9375748a392a6fafa5c9e5e78ef4c4d8289f77c`
