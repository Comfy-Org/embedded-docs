O nó ModelMergeSD35_Large permite mesclar dois modelos Stable Diffusion 3.5 Large, ajustando a influência de diferentes componentes do modelo. Ele oferece controle preciso sobre quanto cada parte do segundo modelo contribui para o modelo mesclado final, desde camadas de incorporação até blocos conjuntos e camadas finais.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model1` | O modelo base que serve como fundação para a mesclagem | MODEL | Sim | - |
| `model2` | O modelo secundário cujos componentes serão mesclados ao modelo base | MODEL | Sim | - |
| `pos_embed.` | Controla quanto da incorporação de posição do model2 é mesclada ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `x_embedder.` | Controla quanto do incorporador x do model2 é mesclado ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `context_embedder.` | Controla quanto do incorporador de contexto do model2 é mesclado ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `y_embedder.` | Controla quanto do incorporador y do model2 é mesclado ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `t_embedder.` | Controla quanto do incorporador t do model2 é mesclado ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `joint_blocks.0.` | Controla quanto do bloco conjunto 0 do model2 é mesclado ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `joint_blocks.1.` | Controla quanto do bloco conjunto 1 do model2 é mesclado ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `joint_blocks.2.` | Controla quanto do bloco conjunto 2 do model2 é mesclado ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `joint_blocks.3.` | Controla quanto do bloco conjunto 3 do model2 é mesclado ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `joint_blocks.4.` | Controla quanto do bloco conjunto 4 do model2 é mesclado ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `joint_blocks.5.` | Controla quanto do bloco conjunto 5 do model2 é mesclado ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `joint_blocks.6.` | Controla quanto do bloco conjunto 6 do model2 é mesclado ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `joint_blocks.7.` | Controla quanto do bloco conjunto 7 do model2 é mesclado ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `joint_blocks.8.` | Controla quanto do bloco conjunto 8 do model2 é mesclado ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `joint_blocks.9.` | Controla quanto do bloco conjunto 9 do model2 é mesclado ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `joint_blocks.10.` | Controla quanto do bloco conjunto 10 do model2 é mesclado ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `joint_blocks.11.` | Controla quanto do bloco conjunto 11 do model2 é mesclado ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `joint_blocks.12.` | Controla quanto do bloco conjunto 12 do model2 é mesclado ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `joint_blocks.13.` | Controla quanto do bloco conjunto 13 do model2 é mesclado ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `joint_blocks.14.` | Controla quanto do bloco conjunto 14 do model2 é mesclado ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `joint_blocks.15.` | Controla quanto do bloco conjunto 15 do model2 é mesclado ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `joint_blocks.16.` | Controla quanto do bloco conjunto 16 do model2 é mesclado ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `joint_blocks.17.` | Controla quanto do bloco conjunto 17 do model2 é mesclado ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `joint_blocks.18.` | Controla quanto do bloco conjunto 18 do model2 é mesclado ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `joint_blocks.19.` | Controla quanto do bloco conjunto 19 do model2 é mesclado ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `joint_blocks.20.` | Controla quanto do bloco conjunto 20 do model2 é mesclado ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `joint_blocks.21.` | Controla quanto do bloco conjunto 21 do model2 é mesclado ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `joint_blocks.22.` | Controla quanto do bloco conjunto 22 do model2 é mesclado ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `joint_blocks.23.` | Controla quanto do bloco conjunto 23 do model2 é mesclado ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `joint_blocks.24.` | Controla quanto do bloco conjunto 24 do model2 é mesclado ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `joint_blocks.25.` | Controla quanto do bloco conjunto 25 do model2 é mesclado ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `joint_blocks.26.` | Controla quanto do bloco conjunto 26 do model2 é mesclado ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `joint_blocks.27.` | Controla quanto do bloco conjunto 27 do model2 é mesclado ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `joint_blocks.28.` | Controla quanto do bloco conjunto 28 do model2 é mesclado ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `joint_blocks.29.` | Controla quanto do bloco conjunto 29 do model2 é mesclado ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `joint_blocks.30.` | Controla quanto do bloco conjunto 30 do model2 é mesclado ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `joint_blocks.31.` | Controla quanto do bloco conjunto 31 do model2 é mesclado ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `joint_blocks.32.` | Controla quanto do bloco conjunto 32 do model2 é mesclado ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `joint_blocks.33.` | Controla quanto do bloco conjunto 33 do model2 é mesclado ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `joint_blocks.34.` | Controla quanto do bloco conjunto 34 do model2 é mesclado ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `joint_blocks.35.` | Controla quanto do bloco conjunto 35 do model2 é mesclado ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `joint_blocks.36.` | Controla quanto do bloco conjunto 36 do model2 é mesclado ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `joint_blocks.37.` | Controla quanto do bloco conjunto 37 do model2 é mesclado ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |
| `final_layer.` | Controla quanto da camada final do model2 é mesclada ao modelo final (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 |

**Nota:** Todos os parâmetros de mesclagem aceitam valores de 0.0 a 1.0, onde 0.0 significa nenhuma contribuição do model2 e 1.0 significa contribuição total do model2 para aquele componente específico.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model` | O modelo mesclado resultante, combinando características de ambos os modelos de entrada de acordo com os parâmetros de mesclagem especificados | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD35_Large/pt-BR.md)

---
**Source fingerprint (SHA-256):** `1b491bd96cc40c6098fd8194f66753bc0f7aa485ea5f97b67b4d864cc9615c9a`
