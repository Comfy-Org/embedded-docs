# ModelMergeCosmosPredict2_2B

O nó **ModelMergeCosmosPredict2_2B** mescla dois modelos de difusão usando uma abordagem baseada em blocos, com controle refinado sobre diferentes componentes do modelo. Ele permite combinar partes específicas de dois modelos ajustando os pesos de interpolação para codificadores de posição, codificadores de tempo, blocos Transformer e camadas finais. Isso proporciona controle preciso sobre como diferentes componentes arquitetônicos de cada modelo contribuem para o resultado final mesclado.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model1` | O primeiro modelo a ser mesclado | MODEL | Sim | - |
| `model2` | O segundo modelo a ser mesclado | MODEL | Sim | - |
| `pos_embedder.` | Peso de interpolação do codificador de posição (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `x_embedder.` | Peso de interpolação do codificador de entrada (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `t_embedder.` | Peso de interpolação do codificador de tempo (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `t_embedding_norm.` | Peso de interpolação da normalização do embedding de tempo (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.0.` | Peso de interpolação do bloco Transformer 0 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.1.` | Peso de interpolação do bloco Transformer 1 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.2.` | Peso de interpolação do bloco Transformer 2 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.3.` | Peso de interpolação do bloco Transformer 3 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.4.` | Peso de interpolação do bloco Transformer 4 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.5.` | Peso de interpolação do bloco Transformer 5 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.6.` | Peso de interpolação do bloco Transformer 6 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.7.` | Peso de interpolação do bloco Transformer 7 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.8.` | Peso de interpolação do bloco Transformer 8 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.9.` | Peso de interpolação do bloco Transformer 9 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.10.` | Peso de interpolação do bloco Transformer 10 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.11.` | Peso de interpolação do bloco Transformer 11 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.12.` | Peso de interpolação do bloco Transformer 12 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.13.` | Peso de interpolação do bloco Transformer 13 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.14.` | Peso de interpolação do bloco Transformer 14 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.15.` | Peso de interpolação do bloco Transformer 15 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.16.` | Peso de interpolação do bloco Transformer 16 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.17.` | Peso de interpolação do bloco Transformer 17 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.18.` | Peso de interpolação do bloco Transformer 18 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.19.` | Peso de interpolação do bloco Transformer 19 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.20.` | Peso de interpolação do bloco Transformer 20 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.21.` | Peso de interpolação do bloco Transformer 21 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.22.` | Peso de interpolação do bloco Transformer 22 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.23.` | Peso de interpolação do bloco Transformer 23 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.24.` | Peso de interpolação do bloco Transformer 24 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.25.` | Peso de interpolação do bloco Transformer 25 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.26.` | Peso de interpolação do bloco Transformer 26 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.27.` | Peso de interpolação do bloco Transformer 27 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `final_layer.` | Peso de interpolação da camada final (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo mesclado que combina características de ambos os modelos de entrada | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmosPredict2_2B/pt-BR.md)

---
**Source fingerprint (SHA-256):** `3586868201320ae9a326a08f6a9bd74511a5342bf8496e7efcb9f45cf4b7c55d`
