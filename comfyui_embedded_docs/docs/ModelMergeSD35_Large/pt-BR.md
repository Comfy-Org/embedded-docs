# ModelMergeSD35_Large

O nó ModelMergeSD35_Large permite mesclar dois modelos Stable Diffusion 3.5 Large, ajustando a influência de diferentes componentes do modelo. Ele oferece controle preciso sobre o quanto cada parte do segundo modelo contribui para o modelo mesclado final, desde as camadas de embedding até os blocos conjuntos e a camada final.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model1` | O modelo base que serve de base para a mesclagem | MODEL | Sim | - |
| `model2` | O modelo secundário cujos componentes serão mesclados ao modelo base | MODEL | Sim | - |
| `pos_embed.` | Controla o quanto do embedding posicional do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `x_embedder.` | Controla o quanto do x embedder do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `context_embedder.` | Controla o quanto do context embedder do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `y_embedder.` | Controla o quanto do y embedder do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `t_embedder.` | Controla o quanto do t embedder do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `joint_blocks.0.` | Controla o quanto do bloco conjunto 0 do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `joint_blocks.1.` | Controla o quanto do bloco conjunto 1 do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `joint_blocks.2.` | Controla o quanto do bloco conjunto 2 do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `joint_blocks.3.` | Controla o quanto do bloco conjunto 3 do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `joint_blocks.4.` | Controla o quanto do bloco conjunto 4 do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `joint_blocks.5.` | Controla o quanto do bloco conjunto 5 do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `joint_blocks.6.` | Controla o quanto do bloco conjunto 6 do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `joint_blocks.7.` | Controla o quanto do bloco conjunto 7 do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `joint_blocks.8.` | Controla o quanto do bloco conjunto 8 do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `joint_blocks.9.` | Controla o quanto do bloco conjunto 9 do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `joint_blocks.10.` | Controla o quanto do bloco conjunto 10 do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `joint_blocks.11.` | Controla o quanto do bloco conjunto 11 do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `joint_blocks.12.` | Controla o quanto do bloco conjunto 12 do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `joint_blocks.13.` | Controla o quanto do bloco conjunto 13 do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `joint_blocks.14.` | Controla o quanto do bloco conjunto 14 do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `joint_blocks.15.` | Controla o quanto do bloco conjunto 15 do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `joint_blocks.16.` | Controla o quanto do bloco conjunto 16 do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `joint_blocks.17.` | Controla o quanto do bloco conjunto 17 do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `joint_blocks.18.` | Controla o quanto do bloco conjunto 18 do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `joint_blocks.19.` | Controla o quanto do bloco conjunto 19 do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `joint_blocks.20.` | Controla o quanto do bloco conjunto 20 do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `joint_blocks.21.` | Controla o quanto do bloco conjunto 21 do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `joint_blocks.22.` | Controla o quanto do bloco conjunto 22 do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `joint_blocks.23.` | Controla o quanto do bloco conjunto 23 do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `joint_blocks.24.` | Controla o quanto do bloco conjunto 24 do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `joint_blocks.25.` | Controla o quanto do bloco conjunto 25 do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `joint_blocks.26.` | Controla o quanto do bloco conjunto 26 do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `joint_blocks.27.` | Controla o quanto do bloco conjunto 27 do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `joint_blocks.28.` | Controla o quanto do bloco conjunto 28 do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `joint_blocks.29.` | Controla o quanto do bloco conjunto 29 do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `joint_blocks.30.` | Controla o quanto do bloco conjunto 30 do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `joint_blocks.31.` | Controla o quanto do bloco conjunto 31 do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `joint_blocks.32.` | Controla o quanto do bloco conjunto 32 do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `joint_blocks.33.` | Controla o quanto do bloco conjunto 33 do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `joint_blocks.34.` | Controla o quanto do bloco conjunto 34 do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `joint_blocks.35.` | Controla o quanto do bloco conjunto 35 do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `joint_blocks.36.` | Controla o quanto do bloco conjunto 36 do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `joint_blocks.37.` | Controla o quanto do bloco conjunto 37 do model2 é mesclado no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |
| `final_layer.` | Controla o quanto da camada final do model2 é mesclada no modelo mesclado (padrão: 1.0) | FLOAT | Sim | 0.0 to 1.0 |

**Observação:** Todos os parâmetros de mesclagem aceitam valores de 0.0 a 1.0, onde 0.0 significa nenhuma contribuição do model2 e 1.0 significa contribuição total do model2 para aquele componente específico. Eles são incrementados em passos de 0.01.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `model` | O modelo mesclado resultante, que combina características de ambos os modelos de entrada de acordo com os parâmetros de mesclagem especificados. | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD35_Large/pt-BR.md)

---
**Source fingerprint (SHA-256):** `c489c710e18d01adcf4320d9c010ed587ca5e12babb468448f56d79acdc40f6c`
