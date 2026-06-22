# ModelMergeSD3_2B

O nó ModelMergeSD3_2B permite mesclar dois modelos Stable Diffusion 3 2B combinando seus componentes com pesos ajustáveis. Ele fornece controle individual sobre camadas de incorporação e blocos transformadores, possibilitando combinações de modelos finamente ajustadas para tarefas especializadas de geração.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model1` | O primeiro modelo a ser mesclado | MODEL | Sim | - |
| `model2` | O segundo modelo a ser mesclado | MODEL | Sim | - |
| `pos_embed.` | Peso de interpolação da incorporação de posição (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `x_embedder.` | Peso de interpolação da incorporação de entrada (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `context_embedder.` | Peso de interpolação da incorporação de contexto (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `y_embedder.` | Peso de interpolação da incorporação Y (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `t_embedder.` | Peso de interpolação da incorporação temporal (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `joint_blocks.0.` | Peso de interpolação do bloco conjunto 0 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `joint_blocks.1.` | Peso de interpolação do bloco conjunto 1 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `joint_blocks.2.` | Peso de interpolação do bloco conjunto 2 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `joint_blocks.3.` | Peso de interpolação do bloco conjunto 3 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `joint_blocks.4.` | Peso de interpolação do bloco conjunto 4 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `joint_blocks.5.` | Peso de interpolação do bloco conjunto 5 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `joint_blocks.6.` | Peso de interpolação do bloco conjunto 6 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `joint_blocks.7.` | Peso de interpolação do bloco conjunto 7 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `joint_blocks.8.` | Peso de interpolação do bloco conjunto 8 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `joint_blocks.9.` | Peso de interpolação do bloco conjunto 9 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `joint_blocks.10.` | Peso de interpolação do bloco conjunto 10 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `joint_blocks.11.` | Peso de interpolação do bloco conjunto 11 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `joint_blocks.12.` | Peso de interpolação do bloco conjunto 12 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `joint_blocks.13.` | Peso de interpolação do bloco conjunto 13 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `joint_blocks.14.` | Peso de interpolação do bloco conjunto 14 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `joint_blocks.15.` | Peso de interpolação do bloco conjunto 15 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `joint_blocks.16.` | Peso de interpolação do bloco conjunto 16 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `joint_blocks.17.` | Peso de interpolação do bloco conjunto 17 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `joint_blocks.18.` | Peso de interpolação do bloco conjunto 18 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `joint_blocks.19.` | Peso de interpolação do bloco conjunto 19 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `joint_blocks.20.` | Peso de interpolação do bloco conjunto 20 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `joint_blocks.21.` | Peso de interpolação do bloco conjunto 21 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `joint_blocks.22.` | Peso de interpolação do bloco conjunto 22 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `joint_blocks.23.` | Peso de interpolação do bloco conjunto 23 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `final_layer.` | Peso de interpolação da camada final (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model` | O modelo mesclado combinando características de ambos os modelos de entrada | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD3_2B/pt-BR.md)

---
**Source fingerprint (SHA-256):** `5b0c28c66e1828742873191be424956a9006e59ea1167a5941069ba0b7bc390b`
