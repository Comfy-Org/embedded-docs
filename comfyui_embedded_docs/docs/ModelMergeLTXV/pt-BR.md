> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeLTXV/pt-BR.md)

O nó ModelMergeLTXV realiza operações avançadas de fusão de modelos especificamente projetadas para arquiteturas de modelo LTXV. Ele permite combinar dois modelos diferentes ajustando pesos de interpolação para vários componentes do modelo, incluindo blocos transformadores, camadas de projeção e outros módulos especializados.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Sim | - | O primeiro modelo a ser mesclado |
| `model2` | MODEL | Sim | - | O segundo modelo a ser mesclado |
| `patchify_proj.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação para as camadas de projeção patchify (padrão: 1.0) |
| `adaln_single.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação para as camadas únicas de normalização adaptativa de camada (padrão: 1.0) |
| `caption_projection.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação para as camadas de projeção de legenda (padrão: 1.0) |
| `transformer_blocks.0.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação para o bloco transformador 0 (padrão: 1.0) |
| `transformer_blocks.1.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação para o bloco transformador 1 (padrão: 1.0) |
| `transformer_blocks.2.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação para o bloco transformador 2 (padrão: 1.0) |
| `transformer_blocks.3.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação para o bloco transformador 3 (padrão: 1.0) |
| `transformer_blocks.4.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação para o bloco transformador 4 (padrão: 1.0) |
| `transformer_blocks.5.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação para o bloco transformador 5 (padrão: 1.0) |
| `transformer_blocks.6.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação para o bloco transformador 6 (padrão: 1.0) |
| `transformer_blocks.7.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação para o bloco transformador 7 (padrão: 1.0) |
| `transformer_blocks.8.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação para o bloco transformador 8 (padrão: 1.0) |
| `transformer_blocks.9.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação para o bloco transformador 9 (padrão: 1.0) |
| `transformer_blocks.10.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação para o bloco transformador 10 (padrão: 1.0) |
| `transformer_blocks.11.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação para o bloco transformador 11 (padrão: 1.0) |
| `transformer_blocks.12.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação para o bloco transformador 12 (padrão: 1.0) |
| `transformer_blocks.13.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação para o bloco transformador 13 (padrão: 1.0) |
| `transformer_blocks.14.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação para o bloco transformador 14 (padrão: 1.0) |
| `transformer_blocks.15.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação para o bloco transformador 15 (padrão: 1.0) |
| `transformer_blocks.16.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação para o bloco transformador 16 (padrão: 1.0) |
| `transformer_blocks.17.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação para o bloco transformador 17 (padrão: 1.0) |
| `transformer_blocks.18.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação para o bloco transformador 18 (padrão: 1.0) |
| `transformer_blocks.19.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação para o bloco transformador 19 (padrão: 1.0) |
| `transformer_blocks.20.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação para o bloco transformador 20 (padrão: 1.0) |
| `transformer_blocks.21.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação para o bloco transformador 21 (padrão: 1.0) |
| `transformer_blocks.22.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação para o bloco transformador 22 (padrão: 1.0) |
| `transformer_blocks.23.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação para o bloco transformador 23 (padrão: 1.0) |
| `transformer_blocks.24.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação para o bloco transformador 24 (padrão: 1.0) |
| `transformer_blocks.25.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação para o bloco transformador 25 (padrão: 1.0) |
| `transformer_blocks.26.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação para o bloco transformador 26 (padrão: 1.0) |
| `transformer_blocks.27.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação para o bloco transformador 27 (padrão: 1.0) |
| `scale_shift_table` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação para a tabela de escala e deslocamento (padrão: 1.0) |
| `proj_out.` | FLOAT | Sim | 0.0 - 1.0 | Peso de interpolação para as camadas de saída de projeção (padrão: 1.0) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo mesclado que combina características de ambos os modelos de entrada de acordo com os pesos de interpolação especificados |
