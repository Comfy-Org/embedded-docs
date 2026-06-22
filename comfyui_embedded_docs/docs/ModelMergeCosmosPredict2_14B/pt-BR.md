# ModelMergeCosmosPredict2_14B

O nó ModelMergeCosmosPredict2_14B mescla dois modelos de IA combinando seus componentes internos. Ele oferece controle preciso sobre o quanto cada parte do segundo modelo influencia o resultado final mesclado, usando valores de peso ajustáveis para camadas e componentes específicos.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model1` | O modelo base para mesclar | MODEL | Sim | - |
| `model2` | O modelo secundário para mesclar ao modelo base | MODEL | Sim | - |
| `pos_embedder.` | Peso da mesclagem do incorporador de posição (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `x_embedder.` | Peso da mesclagem do incorporador de entrada (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `t_embedder.` | Peso da mesclagem do incorporador de tempo (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `t_embedding_norm.` | Peso da mesclagem da normalização da incorporação de tempo (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.0.` | Peso da mesclagem do bloco 0 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.1.` | Peso da mesclagem do bloco 1 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.2.` | Peso da mesclagem do bloco 2 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.3.` | Peso da mesclagem do bloco 3 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.4.` | Peso da mesclagem do bloco 4 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.5.` | Peso da mesclagem do bloco 5 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.6.` | Peso da mesclagem do bloco 6 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.7.` | Peso da mesclagem do bloco 7 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.8.` | Peso da mesclagem do bloco 8 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.9.` | Peso da mesclagem do bloco 9 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.10.` | Peso da mesclagem do bloco 10 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.11.` | Peso da mesclagem do bloco 11 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.12.` | Peso da mesclagem do bloco 12 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.13.` | Peso da mesclagem do bloco 13 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.14.` | Peso da mesclagem do bloco 14 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.15.` | Peso da mesclagem do bloco 15 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.16.` | Peso da mesclagem do bloco 16 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.17.` | Peso da mesclagem do bloco 17 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.18.` | Peso da mesclagem do bloco 18 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.19.` | Peso da mesclagem do bloco 19 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.20.` | Peso da mesclagem do bloco 20 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.21.` | Peso da mesclagem do bloco 21 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.22.` | Peso da mesclagem do bloco 22 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.23.` | Peso da mesclagem do bloco 23 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.24.` | Peso da mesclagem do bloco 24 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.25.` | Peso da mesclagem do bloco 25 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.26.` | Peso da mesclagem do bloco 26 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.27.` | Peso da mesclagem do bloco 27 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.28.` | Peso da mesclagem do bloco 28 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.29.` | Peso da mesclagem do bloco 29 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.30.` | Peso da mesclagem do bloco 30 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.31.` | Peso da mesclagem do bloco 31 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.32.` | Peso da mesclagem do bloco 32 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.33.` | Peso da mesclagem do bloco 33 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.34.` | Peso da mesclagem do bloco 34 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.35.` | Peso da mesclagem do bloco 35 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `final_layer.` | Peso da mesclagem da camada final (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |

**Nota:** Todos os parâmetros de peso de mesclagem aceitam valores entre 0.0 e 1.0, onde 0.0 significa nenhuma contribuição do model2 e 1.0 significa contribuição total do model2 para aquele componente específico.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo mesclado combinando características de ambos os modelos de entrada | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmosPredict2_14B/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5e72608391bc47c2610c93fda19e6e12a1695f95f6135a08efe97e3d400acf84`
