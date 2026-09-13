# ModelMergeLTXV

O nó ModelMergeLTXV mescla dois modelos LTXV combinando seus componentes correspondentes. Cada parte do modelo — como blocos transformer, camadas de projeção e a tabela de deslocamento de escala — pode ser combinada separadamente com seu próprio peso, oferecendo controle refinado sobre como os dois modelos são combinados.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model1` | O primeiro modelo a ser mesclado | MODEL | Sim | - |
| `model2` | O segundo modelo a ser mesclado | MODEL | Sim | - |
| `patchify_proj.` | Peso de interpolação para camadas de projeção patchify (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (step: 0.01) |
| `adaln_single.` | Peso de interpolação para camadas individuais de normalização adaptativa de camada (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (step: 0.01) |
| `caption_projection.` | Peso de interpolação para camadas de projeção de legenda (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.0.` | Peso de interpolação para o bloco transformer 0 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.1.` | Peso de interpolação para o bloco transformer 1 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.2.` | Peso de interpolação para o bloco transformer 2 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.3.` | Peso de interpolação para o bloco transformer 3 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.4.` | Peso de interpolação para o bloco transformer 4 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.5.` | Peso de interpolação para o bloco transformer 5 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.6.` | Peso de interpolação para o bloco transformer 6 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.7.` | Peso de interpolação para o bloco transformer 7 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.8.` | Peso de interpolação para o bloco transformer 8 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.9.` | Peso de interpolação para o bloco transformer 9 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.10.` | Peso de interpolação para o bloco transformer 10 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.11.` | Peso de interpolação para o bloco transformer 11 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.12.` | Peso de interpolação para o bloco transformer 12 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.13.` | Peso de interpolação para o bloco transformer 13 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.14.` | Peso de interpolação para o bloco transformer 14 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.15.` | Peso de interpolação para o bloco transformer 15 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.16.` | Peso de interpolação para o bloco transformer 16 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.17.` | Peso de interpolação para o bloco transformer 17 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.18.` | Peso de interpolação para o bloco transformer 18 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.19.` | Peso de interpolação para o bloco transformer 19 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.20.` | Peso de interpolação para o bloco transformer 20 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.21.` | Peso de interpolação para o bloco transformer 21 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.22.` | Peso de interpolação para o bloco transformer 22 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.23.` | Peso de interpolação para o bloco transformer 23 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.24.` | Peso de interpolação para o bloco transformer 24 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.25.` | Peso de interpolação para o bloco transformer 25 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.26.` | Peso de interpolação para o bloco transformer 26 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (step: 0.01) |
| `transformer_blocks.27.` | Peso de interpolação para o bloco transformer 27 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (step: 0.01) |
| `scale_shift_table` | Peso de interpolação para a tabela de deslocamento de escala (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (step: 0.01) |
| `proj_out.` | Peso de interpolação para camadas de saída de projeção (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 (step: 0.01) |

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo mesclado que combina características de ambos os modelos de entrada de acordo com os pesos de interpolação especificados | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeLTXV/pt-BR.md)

---
**Source fingerprint (SHA-256):** `0ff5f93aee831259066679a27fff8f7cbd4a9686242091f1bc7dd3805725566e`
