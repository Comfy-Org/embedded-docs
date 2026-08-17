# ModelMergeCosmosPredict2_14B

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model1` | O modelo base a ser mesclado | MODEL | Sim | - |
| `model2` | O modelo secundário a ser mesclado ao modelo base | MODEL | Sim | - |
| `pos_embedder.` | Peso de mesclagem da camada de embedding de posição (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `x_embedder.` | Peso de mesclagem da camada de embedding de entrada (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `t_embedder.` | Peso de mesclagem da camada de embedding de tempo (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `t_embedding_norm.` | Peso de mesclagem da normalização do embedding de tempo (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.0.` | Peso de mesclagem do bloco 0 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.1.` | Peso de mesclagem do bloco 1 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.2.` | Peso de mesclagem do bloco 2 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.3.` | Peso de mesclagem do bloco 3 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.4.` | Peso de mesclagem do bloco 4 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.5.` | Peso de mesclagem do bloco 5 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.6.` | Peso de mesclagem do bloco 6 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.7.` | Peso de mesclagem do bloco 7 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.8.` | Peso de mesclagem do bloco 8 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.9.` | Peso de mesclagem do bloco 9 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.10.` | Peso de mesclagem do bloco 10 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.11.` | Peso de mesclagem do bloco 11 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.12.` | Peso de mesclagem do bloco 12 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.13.` | Peso de mesclagem do bloco 13 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.14.` | Peso de mesclagem do bloco 14 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.15.` | Peso de mesclagem do bloco 15 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.16.` | Peso de mesclagem do bloco 16 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.17.` | Peso de mesclagem do bloco 17 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.18.` | Peso de mesclagem do bloco 18 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.19.` | Peso de mesclagem do bloco 19 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.20.` | Peso de mesclagem do bloco 20 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.21.` | Peso de mesclagem do bloco 21 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.22.` | Peso de mesclagem do bloco 22 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.23.` | Peso de mesclagem do bloco 23 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.24.` | Peso de mesclagem do bloco 24 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.25.` | Peso de mesclagem do bloco 25 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.26.` | Peso de mesclagem do bloco 26 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.27.` | Peso de mesclagem do bloco 27 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.28.` | Peso de mesclagem do bloco 28 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.29.` | Peso de mesclagem do bloco 29 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.30.` | Peso de mesclagem do bloco 30 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.31.` | Peso de mesclagem do bloco 31 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.32.` | Peso de mesclagem do bloco 32 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.33.` | Peso de mesclagem do bloco 33 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.34.` | Peso de mesclagem do bloco 34 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.35.` | Peso de mesclagem do bloco 35 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `final_layer.` | Peso de mesclagem da camada final (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |

**Observação:** Todos os parâmetros de peso de mesclagem aceitam valores entre 0.0 e 1.0, onde 0.0 significa nenhuma contribuição do model2 e 1.0 significa contribuição total do model2 para esse componente específico.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model` | O modelo mesclado que combina características de ambos os modelos de entrada | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmosPredict2_14B/pt-BR.md)

---
**Source fingerprint (SHA-256):** `a5f34deda62dc03f22613517e43996b908a8673dc5da10d8f1b7f6411ece2f0a`
