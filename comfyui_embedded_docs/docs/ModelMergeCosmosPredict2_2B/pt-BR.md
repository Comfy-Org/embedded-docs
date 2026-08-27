# ModelMergeCosmosPredict2_2B

O nó ModelMergeCosmosPredict2_2B mescla dois modelos de difusão usando uma abordagem baseada em blocos com controle refinado sobre diferentes componentes do modelo. Ele permite combinar partes específicas de dois modelos ajustando pesos de interpolação para incorporadores de posição, incorporadores de tempo, blocos transformadores e camadas finais. Isso proporciona controle preciso sobre como diferentes componentes arquitetônicos de cada modelo contribuem para o resultado mesclado final.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model1` | O primeiro modelo a ser mesclado | MODEL | Sim | - |
| `model2` | O segundo modelo a ser mesclado | MODEL | Sim | - |
| `pos_embedder.` | Peso de interpolação do incorporador de posição (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `x_embedder.` | Peso de interpolação do incorporador de entrada (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `t_embedder.` | Peso de interpolação do incorporador de tempo (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `t_embedding_norm.` | Peso de interpolação da normalização da incorporação de tempo (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocos.0.` | Peso de interpolação do bloco transformador 0 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocos.1.` | Peso de interpolação do bloco transformador 1 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocos.2.` | Peso de interpolação do bloco transformador 2 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocos.3.` | Peso de interpolação do bloco transformador 3 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocos.4.` | Peso de interpolação do bloco transformador 4 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocos.5.` | Peso de interpolação do bloco transformador 5 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocos.6.` | Peso de interpolação do bloco transformador 6 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocos.7.` | Peso de interpolação do bloco transformador 7 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocos.8.` | Peso de interpolação do bloco transformador 8 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocos.9.` | Peso de interpolação do bloco transformador 9 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocos.10.` | Peso de interpolação do bloco transformador 10 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocos.11.` | Peso de interpolação do bloco transformador 11 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocos.12.` | Peso de interpolação do bloco transformador 12 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocos.13.` | Peso de interpolação do bloco transformador 13 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocos.14.` | Peso de interpolação do bloco transformador 14 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocos.15.` | Peso de interpolação do bloco transformador 15 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocos.16.` | Peso de interpolação do bloco transformador 16 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocos.17.` | Peso de interpolação do bloco transformador 17 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocos.18.` | Peso de interpolação do bloco transformador 18 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocos.19.` | Peso de interpolação do bloco transformador 19 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocos.20.` | Peso de interpolação do bloco transformador 20 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocos.21.` | Peso de interpolação do bloco transformador 21 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocos.22.` | Peso de interpolação do bloco transformador 22 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocos.23.` | Peso de interpolação do bloco transformador 23 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocos.24.` | Peso de interpolação do bloco transformador 24 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocos.25.` | Peso de interpolação do bloco transformador 25 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocos.26.` | Peso de interpolação do bloco transformador 26 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocos.27.` | Peso de interpolação do bloco transformador 27 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `final_layer.` | Peso de interpolação da camada final (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model` | O modelo mesclado combinando características de ambos os modelos de entrada | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmosPredict2_2B/pt-BR.md)

---
**Source fingerprint (SHA-256):** `53a8de66d6b731f5b29af326832f66cc973284bc8fdf09d779575f2346cc75a7`
