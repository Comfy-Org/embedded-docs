# ModelMergeSD1

O ModelMergeSD1 permite mesclar dois modelos Stable Diffusion 1.x ajustando a influência de seus componentes individuais. Ele fornece um peso de mesclagem separado para o embedding de tempo, o embedding de rótulo, cada bloco de entrada, cada bloco intermediário, cada bloco de saída e a camada de saída final, permitindo um controle refinado sobre como os dois modelos são combinados.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model1` | O primeiro modelo a ser mesclado | MODEL | Sim | - |
| `model2` | O segundo modelo a ser mesclado | MODEL | Sim | - |
| `time_embed.` | Peso de mesclagem da camada de embedding de tempo (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `label_emb.` | Peso de mesclagem da camada de embedding de rótulo (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `input_blocks.0.` | Peso de mesclagem do bloco de entrada 0 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `input_blocks.1.` | Peso de mesclagem do bloco de entrada 1 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `input_blocks.2.` | Peso de mesclagem do bloco de entrada 2 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `input_blocks.3.` | Peso de mesclagem do bloco de entrada 3 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `input_blocks.4.` | Peso de mesclagem do bloco de entrada 4 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `input_blocks.5.` | Peso de mesclagem do bloco de entrada 5 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `input_blocks.6.` | Peso de mesclagem do bloco de entrada 6 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `input_blocks.7.` | Peso de mesclagem do bloco de entrada 7 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `input_blocks.8.` | Peso de mesclagem do bloco de entrada 8 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `input_blocks.9.` | Peso de mesclagem do bloco de entrada 9 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `input_blocks.10.` | Peso de mesclagem do bloco de entrada 10 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `input_blocks.11.` | Peso de mesclagem do bloco de entrada 11 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `middle_block.0.` | Peso de mesclagem do bloco intermediário 0 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `middle_block.1.` | Peso de mesclagem do bloco intermediário 1 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `middle_block.2.` | Peso de mesclagem do bloco intermediário 2 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `output_blocks.0.` | Peso de mesclagem do bloco de saída 0 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `output_blocks.1.` | Peso de mesclagem do bloco de saída 1 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `output_blocks.2.` | Peso de mesclagem do bloco de saída 2 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `output_blocks.3.` | Peso de mesclagem do bloco de saída 3 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `output_blocks.4.` | Peso de mesclagem do bloco de saída 4 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `output_blocks.5.` | Peso de mesclagem do bloco de saída 5 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `output_blocks.6.` | Peso de mesclagem do bloco de saída 6 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `output_blocks.7.` | Peso de mesclagem do bloco de saída 7 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `output_blocks.8.` | Peso de mesclagem do bloco de saída 8 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `output_blocks.9.` | Peso de mesclagem do bloco de saída 9 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `output_blocks.10.` | Peso de mesclagem do bloco de saída 10 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `output_blocks.11.` | Peso de mesclagem do bloco de saída 11 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `out.` | Peso de mesclagem da camada de saída (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `MODEL` | O modelo mesclado que combina características de ambos os modelos de entrada | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD1/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b9d53f126139412fbd8b21be72e1dcdb02736519ab4dc9e28c7840d69acb7c87`
