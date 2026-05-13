> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmosPredict2_14B/pt-BR.md)

O nó ModelMergeCosmosPredict2_14B mescla dois modelos de IA combinando seus componentes internos. Ele oferece controle preciso sobre o quanto cada parte do segundo modelo influencia o resultado final mesclado, usando valores de peso ajustáveis para camadas e componentes específicos.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|---------------|-------------|-----------|-----------|
| `model1` | MODEL | Sim | - | O modelo base para mesclar |
| `model2` | MODEL | Sim | - | O modelo secundário para mesclar ao modelo base |
| `pos_embedder.` | FLOAT | Sim | 0.0 - 1.0 | Peso da mesclagem do incorporador de posição (padrão: 1.0) |
| `x_embedder.` | FLOAT | Sim | 0.0 - 1.0 | Peso da mesclagem do incorporador de entrada (padrão: 1.0) |
| `t_embedder.` | FLOAT | Sim | 0.0 - 1.0 | Peso da mesclagem do incorporador de tempo (padrão: 1.0) |
| `t_embedding_norm.` | FLOAT | Sim | 0.0 - 1.0 | Peso da mesclagem da normalização da incorporação de tempo (padrão: 1.0) |
| `blocks.0.` | FLOAT | Sim | 0.0 - 1.0 | Peso da mesclagem do bloco 0 (padrão: 1.0) |
| `blocks.1.` | FLOAT | Sim | 0.0 - 1.0 | Peso da mesclagem do bloco 1 (padrão: 1.0) |
| `blocks.2.` | FLOAT | Sim | 0.0 - 1.0 | Peso da mesclagem do bloco 2 (padrão: 1.0) |
| `blocks.3.` | FLOAT | Sim | 0.0 - 1.0 | Peso da mesclagem do bloco 3 (padrão: 1.0) |
| `blocks.4.` | FLOAT | Sim | 0.0 - 1.0 | Peso da mesclagem do bloco 4 (padrão: 1.0) |
| `blocks.5.` | FLOAT | Sim | 0.0 - 1.0 | Peso da mesclagem do bloco 5 (padrão: 1.0) |
| `blocks.6.` | FLOAT | Sim | 0.0 - 1.0 | Peso da mesclagem do bloco 6 (padrão: 1.0) |
| `blocks.7.` | FLOAT | Sim | 0.0 - 1.0 | Peso da mesclagem do bloco 7 (padrão: 1.0) |
| `blocks.8.` | FLOAT | Sim | 0.0 - 1.0 | Peso da mesclagem do bloco 8 (padrão: 1.0) |
| `blocks.9.` | FLOAT | Sim | 0.0 - 1.0 | Peso da mesclagem do bloco 9 (padrão: 1.0) |
| `blocks.10.` | FLOAT | Sim | 0.0 - 1.0 | Peso da mesclagem do bloco 10 (padrão: 1.0) |
| `blocks.11.` | FLOAT | Sim | 0.0 - 1.0 | Peso da mesclagem do bloco 11 (padrão: 1.0) |
| `blocks.12.` | FLOAT | Sim | 0.0 - 1.0 | Peso da mesclagem do bloco 12 (padrão: 1.0) |
| `blocks.13.` | FLOAT | Sim | 0.0 - 1.0 | Peso da mesclagem do bloco 13 (padrão: 1.0) |
| `blocks.14.` | FLOAT | Sim | 0.0 - 1.0 | Peso da mesclagem do bloco 14 (padrão: 1.0) |
| `blocks.15.` | FLOAT | Sim | 0.0 - 1.0 | Peso da mesclagem do bloco 15 (padrão: 1.0) |
| `blocks.16.` | FLOAT | Sim | 0.0 - 1.0 | Peso da mesclagem do bloco 16 (padrão: 1.0) |
| `blocks.17.` | FLOAT | Sim | 0.0 - 1.0 | Peso da mesclagem do bloco 17 (padrão: 1.0) |
| `blocks.18.` | FLOAT | Sim | 0.0 - 1.0 | Peso da mesclagem do bloco 18 (padrão: 1.0) |
| `blocks.19.` | FLOAT | Sim | 0.0 - 1.0 | Peso da mesclagem do bloco 19 (padrão: 1.0) |
| `blocks.20.` | FLOAT | Sim | 0.0 - 1.0 | Peso da mesclagem do bloco 20 (padrão: 1.0) |
| `blocks.21.` | FLOAT | Sim | 0.0 - 1.0 | Peso da mesclagem do bloco 21 (padrão: 1.0) |
| `blocks.22.` | FLOAT | Sim | 0.0 - 1.0 | Peso da mesclagem do bloco 22 (padrão: 1.0) |
| `blocks.23.` | FLOAT | Sim | 0.0 - 1.0 | Peso da mesclagem do bloco 23 (padrão: 1.0) |
| `blocks.24.` | FLOAT | Sim | 0.0 - 1.0 | Peso da mesclagem do bloco 24 (padrão: 1.0) |
| `blocks.25.` | FLOAT | Sim | 0.0 - 1.0 | Peso da mesclagem do bloco 25 (padrão: 1.0) |
| `blocks.26.` | FLOAT | Sim | 0.0 - 1.0 | Peso da mesclagem do bloco 26 (padrão: 1.0) |
| `blocks.27.` | FLOAT | Sim | 0.0 - 1.0 | Peso da mesclagem do bloco 27 (padrão: 1.0) |
| `blocks.28.` | FLOAT | Sim | 0.0 - 1.0 | Peso da mesclagem do bloco 28 (padrão: 1.0) |
| `blocks.29.` | FLOAT | Sim | 0.0 - 1.0 | Peso da mesclagem do bloco 29 (padrão: 1.0) |
| `blocks.30.` | FLOAT | Sim | 0.0 - 1.0 | Peso da mesclagem do bloco 30 (padrão: 1.0) |
| `blocks.31.` | FLOAT | Sim | 0.0 - 1.0 | Peso da mesclagem do bloco 31 (padrão: 1.0) |
| `blocks.32.` | FLOAT | Sim | 0.0 - 1.0 | Peso da mesclagem do bloco 32 (padrão: 1.0) |
| `blocks.33.` | FLOAT | Sim | 0.0 - 1.0 | Peso da mesclagem do bloco 33 (padrão: 1.0) |
| `blocks.34.` | FLOAT | Sim | 0.0 - 1.0 | Peso da mesclagem do bloco 34 (padrão: 1.0) |
| `blocks.35.` | FLOAT | Sim | 0.0 - 1.0 | Peso da mesclagem do bloco 35 (padrão: 1.0) |
| `final_layer.` | FLOAT | Sim | 0.0 - 1.0 | Peso da mesclagem da camada final (padrão: 1.0) |

**Nota:** Todos os parâmetros de peso de mesclagem aceitam valores entre 0.0 e 1.0, onde 0.0 significa nenhuma contribuição do model2 e 1.0 significa contribuição total do model2 para aquele componente específico.

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|---------------|---------------|-----------|
| `model` | MODEL | O modelo mesclado combinando características de ambos os modelos de entrada |

---
**Source fingerprint (SHA-256):** `5e72608391bc47c2610c93fda19e6e12a1695f95f6135a08efe97e3d400acf84`
