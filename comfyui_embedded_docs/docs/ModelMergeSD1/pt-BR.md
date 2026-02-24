> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD1/pt-BR.md)

O nó ModelMergeSD1 permite combinar dois modelos Stable Diffusion 1.x ajustando a influência de diferentes componentes do modelo. Ele oferece controle individual sobre a incorporação de tempo, a incorporação de rótulo e todos os blocos de entrada, intermediários e de saída, permitindo uma fusão de modelos afinada para casos de uso específicos.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Sim | - | O primeiro modelo a ser mesclado |
| `model2` | MODEL | Sim | - | O segundo modelo a ser mesclado |
| `time_embed.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura da camada de incorporação de tempo (padrão: 1.0) |
| `label_emb.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura da camada de incorporação de rótulo (padrão: 1.0) |
| `input_blocks.0.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do bloco de entrada 0 (padrão: 1.0) |
| `input_blocks.1.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do bloco de entrada 1 (padrão: 1.0) |
| `input_blocks.2.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do bloco de entrada 2 (padrão: 1.0) |
| `input_blocks.3.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do bloco de entrada 3 (padrão: 1.0) |
| `input_blocks.4.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do bloco de entrada 4 (padrão: 1.0) |
| `input_blocks.5.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do bloco de entrada 5 (padrão: 1.0) |
| `input_blocks.6.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do bloco de entrada 6 (padrão: 1.0) |
| `input_blocks.7.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do bloco de entrada 7 (padrão: 1.0) |
| `input_blocks.8.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do bloco de entrada 8 (padrão: 1.0) |
| `input_blocks.9.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do bloco de entrada 9 (padrão: 1.0) |
| `input_blocks.10.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do bloco de entrada 10 (padrão: 1.0) |
| `input_blocks.11.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do bloco de entrada 11 (padrão: 1.0) |
| `middle_block.0.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do bloco intermediário 0 (padrão: 1.0) |
| `middle_block.1.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do bloco intermediário 1 (padrão: 1.0) |
| `middle_block.2.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do bloco intermediário 2 (padrão: 1.0) |
| `output_blocks.0.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do bloco de saída 0 (padrão: 1.0) |
| `output_blocks.1.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do bloco de saída 1 (padrão: 1.0) |
| `output_blocks.2.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do bloco de saída 2 (padrão: 1.0) |
| `output_blocks.3.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do bloco de saída 3 (padrão: 1.0) |
| `output_blocks.4.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do bloco de saída 4 (padrão: 1.0) |
| `output_blocks.5.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do bloco de saída 5 (padrão: 1.0) |
| `output_blocks.6.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do bloco de saída 6 (padrão: 1.0) |
| `output_blocks.7.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do bloco de saída 7 (padrão: 1.0) |
| `output_blocks.8.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do bloco de saída 8 (padrão: 1.0) |
| `output_blocks.9.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do bloco de saída 9 (padrão: 1.0) |
| `output_blocks.10.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do bloco de saída 10 (padrão: 1.0) |
| `output_blocks.11.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura do bloco de saída 11 (padrão: 1.0) |
| `out.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura da camada de saída (padrão: 1.0) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `MODEL` | MODEL | O modelo mesclado que combina características de ambos os modelos de entrada |
