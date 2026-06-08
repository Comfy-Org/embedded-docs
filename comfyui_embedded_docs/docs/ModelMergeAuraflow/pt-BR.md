O nó ModelMergeAuraflow permite combinar dois modelos diferentes ajustando pesos específicos de mesclagem para vários componentes do modelo. Ele oferece controle refinado sobre como diferentes partes dos modelos são mescladas, desde as camadas iniciais até as saídas finais. Este nó é particularmente útil para criar combinações personalizadas de modelos com controle preciso sobre o processo de mesclagem.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model1` | O primeiro modelo a ser mesclado | MODEL | Sim | - |
| `model2` | O segundo modelo a ser mesclado | MODEL | Sim | - |
| `init_x_linear.` | Peso de mesclagem para a transformação linear inicial (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `codificação_posicional` | Peso de mesclagem para componentes de codificação posicional (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `cond_seq_linear.` | Peso de mesclagem para camadas lineares de sequência condicional (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `registrar_tokens` | Peso de mesclagem para componentes de registro de tokens (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `t_embedder.` | Peso de mesclagem para componentes de incorporação temporal (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `double_layers.0.` | Peso de mesclagem para o grupo de camada dupla 0 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `double_layers.1.` | Peso de mesclagem para o grupo de camada dupla 1 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `double_layers.2.` | Peso de mesclagem para o grupo de camada dupla 2 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `double_layers.3.` | Peso de mesclagem para o grupo de camada dupla 3 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `single_layers.0.` | Peso de mesclagem para a camada única 0 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `single_layers.1.` | Peso de mesclagem para a camada única 1 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `single_layers.2.` | Peso de mesclagem para a camada única 2 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `single_layers.3.` | Peso de mesclagem para a camada única 3 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `single_layers.4.` | Peso de mesclagem para a camada única 4 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `single_layers.5.` | Peso de mesclagem para a camada única 5 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `single_layers.6.` | Peso de mesclagem para a camada única 6 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `single_layers.7.` | Peso de mesclagem para a camada única 7 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `single_layers.8.` | Peso de mesclagem para a camada única 8 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `single_layers.9.` | Peso de mesclagem para a camada única 9 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `single_layers.10.` | Peso de mesclagem para a camada única 10 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `single_layers.11.` | Peso de mesclagem para a camada única 11 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `single_layers.12.` | Peso de mesclagem para a camada única 12 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `single_layers.13.` | Peso de mesclagem para a camada única 13 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `single_layers.14.` | Peso de mesclagem para a camada única 14 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `single_layers.15.` | Peso de mesclagem para a camada única 15 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `single_layers.16.` | Peso de mesclagem para a camada única 16 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `single_layers.17.` | Peso de mesclagem para a camada única 17 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `single_layers.18.` | Peso de mesclagem para a camada única 18 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `single_layers.19.` | Peso de mesclagem para a camada única 19 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `single_layers.20.` | Peso de mesclagem para a camada única 20 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `single_layers.21.` | Peso de mesclagem para a camada única 21 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `single_layers.22.` | Peso de mesclagem para a camada única 22 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `single_layers.23.` | Peso de mesclagem para a camada única 23 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `single_layers.24.` | Peso de mesclagem para a camada única 24 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `single_layers.25.` | Peso de mesclagem para a camada única 25 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `single_layers.26.` | Peso de mesclagem para a camada única 26 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `single_layers.27.` | Peso de mesclagem para a camada única 27 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `single_layers.28.` | Peso de mesclagem para a camada única 28 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `single_layers.29.` | Peso de mesclagem para a camada única 29 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `single_layers.30.` | Peso de mesclagem para a camada única 30 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `single_layers.31.` | Peso de mesclagem para a camada única 31 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `modF.` | Peso de mesclagem para componentes modF (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `final_linear.` | Peso de mesclagem para a transformação linear final (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model` | O modelo mesclado combinando características de ambos os modelos de entrada de acordo com os pesos de mesclagem especificados | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeAuraflow/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c4959321bba252eb24c945343198d72f50d6021d4dac9945f94e3eb28f1bc3c9`
