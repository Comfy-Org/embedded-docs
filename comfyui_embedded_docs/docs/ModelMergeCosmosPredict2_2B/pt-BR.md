> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmosPredict2_2B/pt-BR.md)

O nó ModelMergeCosmosPredict2_2B mescla dois modelos de difusão usando uma abordagem baseada em blocos com controle refinado sobre diferentes componentes do modelo. Ele permite combinar partes específicas de dois modelos ajustando pesos de interpolação para incorporadores de posição, incorporadores de tempo, blocos transformadores e camadas finais. Isso proporciona controle preciso sobre como diferentes componentes arquitetônicos de cada modelo contribuem para o resultado mesclado final.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Sim | - | O primeiro modelo a ser mesclado |
| `model2` | MODEL | Sim | - | O segundo modelo a ser mesclado |
| `pos_embedder.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do incorporador de posição (padrão: 1.0) |
| `x_embedder.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do incorporador de entrada (padrão: 1.0) |
| `t_embedder.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do incorporador de tempo (padrão: 1.0) |
| `t_embedding_norm.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação da normalização da incorporação de tempo (padrão: 1.0) |
| `blocks.0.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco transformador 0 (padrão: 1.0) |
| `blocks.1.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco transformador 1 (padrão: 1.0) |
| `blocks.2.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco transformador 2 (padrão: 1.0) |
| `blocks.3.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco transformador 3 (padrão: 1.0) |
| `blocks.4.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco transformador 4 (padrão: 1.0) |
| `blocks.5.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco transformador 5 (padrão: 1.0) |
| `blocks.6.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco transformador 6 (padrão: 1.0) |
| `blocks.7.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco transformador 7 (padrão: 1.0) |
| `blocks.8.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco transformador 8 (padrão: 1.0) |
| `blocks.9.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco transformador 9 (padrão: 1.0) |
| `blocks.10.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco transformador 10 (padrão: 1.0) |
| `blocks.11.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco transformador 11 (padrão: 1.0) |
| `blocks.12.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco transformador 12 (padrão: 1.0) |
| `blocks.13.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco transformador 13 (padrão: 1.0) |
| `blocks.14.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco transformador 14 (padrão: 1.0) |
| `blocks.15.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco transformador 15 (padrão: 1.0) |
| `blocks.16.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco transformador 16 (padrão: 1.0) |
| `blocks.17.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco transformador 17 (padrão: 1.0) |
| `blocks.18.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco transformador 18 (padrão: 1.0) |
| `blocks.19.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco transformador 19 (padrão: 1.0) |
| `blocks.20.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco transformador 20 (padrão: 1.0) |
| `blocks.21.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco transformador 21 (padrão: 1.0) |
| `blocks.22.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco transformador 22 (padrão: 1.0) |
| `blocks.23.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco transformador 23 (padrão: 1.0) |
| `blocks.24.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco transformador 24 (padrão: 1.0) |
| `blocks.25.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco transformador 25 (padrão: 1.0) |
| `blocks.26.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco transformador 26 (padrão: 1.0) |
| `blocks.27.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco transformador 27 (padrão: 1.0) |
| `final_layer.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação da camada final (padrão: 1.0) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo mesclado combinando características de ambos os modelos de entrada |

---
**Source fingerprint (SHA-256):** `53a8de66d6b731f5b29af326832f66cc973284bc8fdf09d779575f2346cc75a7`
