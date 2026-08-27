# ModelMergeMochiPreview

Este nó mescla dois modelos Mochi AI usando uma abordagem baseada em blocos, com controle detalhado sobre diferentes componentes do modelo. Ele permite combinar modelos ajustando os pesos de interpolação para seções específicas, incluindo frequências posicionais, camadas de embedding e cada um dos 48 blocos individuais do transformer. O processo de mesclagem combina as arquiteturas e os parâmetros dos dois modelos de entrada de acordo com os valores de peso especificados.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model1` | O primeiro modelo a ser mesclado | MODEL | Sim | - |
| `model2` | O segundo modelo a ser mesclado | MODEL | Sim | - |
| `pos_frequencies.` | Peso para interpolação das frequências posicionais (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `t_embedder.` | Peso para interpolação do codificador de tempo (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `t5_y_embedder.` | Peso para interpolação do codificador T5-Y (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `t5_yproj.` | Peso para interpolação da projeção T5-Y (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.0.` | Peso para interpolação do bloco 0 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.1.` | Peso para interpolação do bloco 1 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.2.` | Peso para interpolação do bloco 2 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.3.` | Peso para interpolação do bloco 3 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.4.` | Peso para interpolação do bloco 4 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.5.` | Peso para interpolação do bloco 5 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.6.` | Peso para interpolação do bloco 6 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.7.` | Peso para interpolação do bloco 7 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.8.` | Peso para interpolação do bloco 8 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.9.` | Peso para interpolação do bloco 9 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.10.` | Peso para interpolação do bloco 10 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.11.` | Peso para interpolação do bloco 11 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.12.` | Peso para interpolação do bloco 12 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.13.` | Peso para interpolação do bloco 13 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.14.` | Peso para interpolação do bloco 14 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.15.` | Peso para interpolação do bloco 15 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.16.` | Peso para interpolação do bloco 16 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.17.` | Peso para interpolação do bloco 17 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.18.` | Peso para interpolação do bloco 18 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.19.` | Peso para interpolação do bloco 19 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.20.` | Peso para interpolação do bloco 20 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.21.` | Peso para interpolação do bloco 21 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.22.` | Peso para interpolação do bloco 22 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.23.` | Peso para interpolação do bloco 23 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.24.` | Peso para interpolação do bloco 24 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.25.` | Peso para interpolação do bloco 25 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.26.` | Peso para interpolação do bloco 26 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.27.` | Peso para interpolação do bloco 27 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.28.` | Peso para interpolação do bloco 28 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.29.` | Peso para interpolação do bloco 29 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.30.` | Peso para interpolação do bloco 30 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.31.` | Peso para interpolação do bloco 31 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.32.` | Peso para interpolação do bloco 32 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.33.` | Peso para interpolação do bloco 33 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.34.` | Peso para interpolação do bloco 34 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.35.` | Peso para interpolação do bloco 35 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.36.` | Peso para interpolação do bloco 36 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.37.` | Peso para interpolação do bloco 37 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.38.` | Peso para interpolação do bloco 38 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.39.` | Peso para interpolação do bloco 39 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.40.` | Peso para interpolação do bloco 40 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.41.` | Peso para interpolação do bloco 41 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.42.` | Peso para interpolação do bloco 42 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.43.` | Peso para interpolação do bloco 43 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.44.` | Peso para interpolação do bloco 44 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.45.` | Peso para interpolação do bloco 45 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.46.` | Peso para interpolação do bloco 46 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `blocks.47.` | Peso para interpolação do bloco 47 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |
| `final_layer.` | Peso para interpolação da camada final (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (passo: 0.01) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo mesclado que combina características de ambos os modelos de entrada de acordo com os pesos especificados | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeMochiPreview/pt-BR.md)

---
**Source fingerprint (SHA-256):** `8fdf5d023d97ef04bf2b40577be5dbc4c16f8f4437586a98adbdbf7f9fa8a359`
