# ModelMergeSDXL

O nó ModelMergeSDXL permite mesclar dois modelos SDXL ajustando a influência de cada modelo em diferentes partes da arquitetura. Você pode controlar o quanto cada modelo contribui para os embeddings de tempo, embeddings de rótulo e vários blocos dentro da estrutura do modelo. Isso cria um modelo híbrido que combina características de ambos os modelos de entrada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model1` | O primeiro modelo SDXL a ser mesclado | MODEL | Sim | - |
| `model2` | O segundo modelo SDXL a ser mesclado | MODEL | Sim | - |
| `time_embed.` | Peso de mistura para as camadas de embeddings de tempo (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `label_emb.` | Peso de mistura para as camadas de embeddings de rótulo (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `input_blocks.0` | Peso de mistura para o bloco de entrada 0 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `input_blocks.1` | Peso de mistura para o bloco de entrada 1 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `input_blocks.2` | Peso de mistura para o bloco de entrada 2 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `input_blocks.3` | Peso de mistura para o bloco de entrada 3 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `input_blocks.4` | Peso de mistura para o bloco de entrada 4 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `input_blocks.5` | Peso de mistura para o bloco de entrada 5 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `input_blocks.6` | Peso de mistura para o bloco de entrada 6 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `input_blocks.7` | Peso de mistura para o bloco de entrada 7 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `input_blocks.8` | Peso de mistura para o bloco de entrada 8 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `middle_block.0` | Peso de mistura para o bloco intermediário 0 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `middle_block.1` | Peso de mistura para o bloco intermediário 1 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `middle_block.2` | Peso de mistura para o bloco intermediário 2 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `output_blocks.0` | Peso de mistura para o bloco de saída 0 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `output_blocks.1` | Peso de mistura para o bloco de saída 1 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `output_blocks.2` | Peso de mistura para o bloco de saída 2 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `output_blocks.3` | Peso de mistura para o bloco de saída 3 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `output_blocks.4` | Peso de mistura para o bloco de saída 4 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `output_blocks.5` | Peso de mistura para o bloco de saída 5 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `output_blocks.6` | Peso de mistura para o bloco de saída 6 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `output_blocks.7` | Peso de mistura para o bloco de saída 7 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `output_blocks.8` | Peso de mistura para o bloco de saída 8 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `out.` | Peso de mistura para as camadas de saída (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |

Todos os parâmetros de peso de mistura são valores FLOAT obrigatórios entre 0.0 e 1.0, com padrão 1.0, e podem ser ajustados em passos de 0.01.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo SDXL mesclado que combina características de ambos os modelos de entrada | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSDXL/pt-BR.md)

---
**Source fingerprint (SHA-256):** `9a1b0645ee19c2eddb274dd6ea3f9a05997115119cc654a7f055d58475745bb2`
