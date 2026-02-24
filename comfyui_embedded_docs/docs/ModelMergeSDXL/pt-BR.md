> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSDXL/pt-BR.md)

O nó ModelMergeSDXL permite combinar dois modelos SDXL ajustando a influência de cada modelo em diferentes partes da arquitetura. Você pode controlar quanto cada modelo contribui para os embeddings de tempo, embeddings de rótulo e vários blocos dentro da estrutura do modelo. Isso cria um modelo híbrido que combina características de ambos os modelos de entrada.

## Entradas

| Parâmetro | Tipo de Dados | Obrigatório | Intervalo | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Sim | - | O primeiro modelo SDXL a ser mesclado |
| `model2` | MODEL | Sim | - | O segundo modelo SDXL a ser mesclado |
| `time_embed.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura para as camadas de embedding de tempo (padrão: 1.0) |
| `label_emb.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura para as camadas de embedding de rótulo (padrão: 1.0) |
| `input_blocks.0` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura para o bloco de entrada 0 (padrão: 1.0) |
| `input_blocks.1` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura para o bloco de entrada 1 (padrão: 1.0) |
| `input_blocks.2` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura para o bloco de entrada 2 (padrão: 1.0) |
| `input_blocks.3` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura para o bloco de entrada 3 (padrão: 1.0) |
| `input_blocks.4` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura para o bloco de entrada 4 (padrão: 1.0) |
| `input_blocks.5` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura para o bloco de entrada 5 (padrão: 1.0) |
| `input_blocks.6` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura para o bloco de entrada 6 (padrão: 1.0) |
| `input_blocks.7` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura para o bloco de entrada 7 (padrão: 1.0) |
| `input_blocks.8` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura para o bloco de entrada 8 (padrão: 1.0) |
| `middle_block.0` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura para o bloco intermediário 0 (padrão: 1.0) |
| `middle_block.1` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura para o bloco intermediário 1 (padrão: 1.0) |
| `middle_block.2` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura para o bloco intermediário 2 (padrão: 1.0) |
| `output_blocks.0` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura para o bloco de saída 0 (padrão: 1.0) |
| `output_blocks.1` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura para o bloco de saída 1 (padrão: 1.0) |
| `output_blocks.2` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura para o bloco de saída 2 (padrão: 1.0) |
| `output_blocks.3` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura para o bloco de saída 3 (padrão: 1.0) |
| `output_blocks.4` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura para o bloco de saída 4 (padrão: 1.0) |
| `output_blocks.5` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura para o bloco de saída 5 (padrão: 1.0) |
| `output_blocks.6` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura para o bloco de saída 6 (padrão: 1.0) |
| `output_blocks.7` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura para o bloco de saída 7 (padrão: 1.0) |
| `output_blocks.8` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura para o bloco de saída 8 (padrão: 1.0) |
| `out.` | FLOAT | Sim | 0.0 - 1.0 | Peso de mistura para as camadas de saída (padrão: 1.0) |

## Saídas

| Nome da Saída | Tipo de Dados | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo SDXL mesclado, combinando características de ambos os modelos de entrada |
