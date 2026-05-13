> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeMochiPreview/pt-BR.md)

Este nó mescla dois modelos de IA usando uma abordagem baseada em blocos com controle refinado sobre diferentes componentes do modelo. Ele permite combinar modelos ajustando os pesos de interpolação para seções específicas, incluindo frequências posicionais, camadas de incorporação (embedding) e blocos individuais do transformador. O processo de mesclagem combina as arquiteturas e parâmetros de ambos os modelos de entrada de acordo com os valores de peso especificados.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Sim | - | O primeiro modelo a ser mesclado |
| `model2` | MODEL | Sim | - | O segundo modelo a ser mesclado |
| `pos_frequencies.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação das frequências posicionais (padrão: 1.0) |
| `t_embedder.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do incorporador temporal (padrão: 1.0) |
| `t5_y_embedder.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do incorporador T5-Y (padrão: 1.0) |
| `t5_yproj.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação da projeção T5-Y (padrão: 1.0) |
| `blocks.0.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 0 (padrão: 1.0) |
| `blocks.1.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 1 (padrão: 1.0) |
| `blocks.2.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 2 (padrão: 1.0) |
| `blocks.3.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 3 (padrão: 1.0) |
| `blocks.4.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 4 (padrão: 1.0) |
| `blocks.5.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 5 (padrão: 1.0) |
| `blocks.6.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 6 (padrão: 1.0) |
| `blocks.7.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 7 (padrão: 1.0) |
| `blocks.8.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 8 (padrão: 1.0) |
| `blocks.9.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 9 (padrão: 1.0) |
| `blocks.10.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 10 (padrão: 1.0) |
| `blocks.11.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 11 (padrão: 1.0) |
| `blocks.12.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 12 (padrão: 1.0) |
| `blocks.13.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 13 (padrão: 1.0) |
| `blocks.14.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 14 (padrão: 1.0) |
| `blocks.15.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 15 (padrão: 1.0) |
| `blocks.16.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 16 (padrão: 1.0) |
| `blocks.17.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 17 (padrão: 1.0) |
| `blocks.18.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 18 (padrão: 1.0) |
| `blocks.19.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 19 (padrão: 1.0) |
| `blocks.20.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 20 (padrão: 1.0) |
| `blocks.21.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 21 (padrão: 1.0) |
| `blocks.22.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 22 (padrão: 1.0) |
| `blocks.23.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 23 (padrão: 1.0) |
| `blocks.24.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 24 (padrão: 1.0) |
| `blocks.25.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 25 (padrão: 1.0) |
| `blocks.26.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 26 (padrão: 1.0) |
| `blocks.27.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 27 (padrão: 1.0) |
| `blocks.28.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 28 (padrão: 1.0) |
| `blocks.29.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 29 (padrão: 1.0) |
| `blocks.30.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 30 (padrão: 1.0) |
| `blocks.31.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 31 (padrão: 1.0) |
| `blocks.32.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 32 (padrão: 1.0) |
| `blocks.33.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 33 (padrão: 1.0) |
| `blocks.34.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 34 (padrão: 1.0) |
| `blocks.35.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 35 (padrão: 1.0) |
| `blocks.36.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 36 (padrão: 1.0) |
| `blocks.37.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 37 (padrão: 1.0) |
| `blocks.38.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 38 (padrão: 1.0) |
| `blocks.39.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 39 (padrão: 1.0) |
| `blocks.40.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 40 (padrão: 1.0) |
| `blocks.41.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 41 (padrão: 1.0) |
| `blocks.42.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 42 (padrão: 1.0) |
| `blocks.43.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 43 (padrão: 1.0) |
| `blocks.44.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 44 (padrão: 1.0) |
| `blocks.45.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 45 (padrão: 1.0) |
| `blocks.46.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 46 (padrão: 1.0) |
| `blocks.47.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação do bloco 47 (padrão: 1.0) |
| `final_layer.` | FLOAT | Sim | 0.0 - 1.0 | Peso para interpolação da camada final (padrão: 1.0) |

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo mesclado combinando características de ambos os modelos de entrada de acordo com os pesos especificados |

---
**Source fingerprint (SHA-256):** `aebf536f3f89ca8c81141ac871b1b612082c3bd38a29984168b05eccf0cb57e3`
