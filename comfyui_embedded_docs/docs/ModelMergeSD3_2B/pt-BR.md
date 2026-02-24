> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD3_2B/pt-BR.md)

O nó ModelMergeSD3_2B permite mesclar dois modelos Stable Diffusion 3 2B combinando seus componentes com pesos ajustáveis. Ele oferece controle individual sobre camadas de incorporação (embeddings) e blocos do transformador, possibilitando combinações de modelos afinadas para tarefas de geração especializadas.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Sim | - | O primeiro modelo a ser mesclado |
| `model2` | MODEL | Sim | - | O segundo modelo a ser mesclado |
| `pos_embed.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação da incorporação de posição (padrão: 1.0) |
| `x_embedder.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação da incorporação de entrada (padrão: 1.0) |
| `context_embedder.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação da incorporação de contexto (padrão: 1.0) |
| `y_embedder.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação da incorporação Y (padrão: 1.0) |
| `t_embedder.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação da incorporação de tempo (padrão: 1.0) |
| `joint_blocks.0.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco conjunto 0 (padrão: 1.0) |
| `joint_blocks.1.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco conjunto 1 (padrão: 1.0) |
| `joint_blocks.2.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco conjunto 2 (padrão: 1.0) |
| `joint_blocks.3.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco conjunto 3 (padrão: 1.0) |
| `joint_blocks.4.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco conjunto 4 (padrão: 1.0) |
| `joint_blocks.5.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco conjunto 5 (padrão: 1.0) |
| `joint_blocks.6.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco conjunto 6 (padrão: 1.0) |
| `joint_blocks.7.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco conjunto 7 (padrão: 1.0) |
| `joint_blocks.8.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco conjunto 8 (padrão: 1.0) |
| `joint_blocks.9.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco conjunto 9 (padrão: 1.0) |
| `joint_blocks.10.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco conjunto 10 (padrão: 1.0) |
| `joint_blocks.11.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco conjunto 11 (padrão: 1.0) |
| `joint_blocks.12.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco conjunto 12 (padrão: 1.0) |
| `joint_blocks.13.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco conjunto 13 (padrão: 1.0) |
| `joint_blocks.14.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco conjunto 14 (padrão: 1.0) |
| `joint_blocks.15.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco conjunto 15 (padrão: 1.0) |
| `joint_blocks.16.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco conjunto 16 (padrão: 1.0) |
| `joint_blocks.17.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco conjunto 17 (padrão: 1.0) |
| `joint_blocks.18.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco conjunto 18 (padrão: 1.0) |
| `joint_blocks.19.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco conjunto 19 (padrão: 1.0) |
| `joint_blocks.20.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco conjunto 20 (padrão: 1.0) |
| `joint_blocks.21.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco conjunto 21 (padrão: 1.0) |
| `joint_blocks.22.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco conjunto 22 (padrão: 1.0) |
| `joint_blocks.23.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação do bloco conjunto 23 (padrão: 1.0) |
| `final_layer.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação da camada final (padrão: 1.0) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo mesclado, combinando características de ambos os modelos de entrada |
