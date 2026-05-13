> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD35_Large/pt-BR.md)

O nó ModelMergeSD35_Large permite mesclar dois modelos Stable Diffusion 3.5 Large, ajustando a influência de diferentes componentes do modelo. Ele oferece controle preciso sobre quanto cada parte do segundo modelo contribui para o modelo mesclado final, desde camadas de incorporação até blocos conjuntos e camadas finais.

## Entradas

| Parâmetro | Tipo de Dado | Obrigatório | Faixa | Descrição |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Sim | - | O modelo base que serve como fundação para a mesclagem |
| `model2` | MODEL | Sim | - | O modelo secundário cujos componentes serão mesclados ao modelo base |
| `pos_embed.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto da incorporação de posição do model2 é mesclada ao modelo final (padrão: 1.0) |
| `x_embedder.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto do incorporador x do model2 é mesclado ao modelo final (padrão: 1.0) |
| `context_embedder.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto do incorporador de contexto do model2 é mesclado ao modelo final (padrão: 1.0) |
| `y_embedder.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto do incorporador y do model2 é mesclado ao modelo final (padrão: 1.0) |
| `t_embedder.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto do incorporador t do model2 é mesclado ao modelo final (padrão: 1.0) |
| `joint_blocks.0.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto do bloco conjunto 0 do model2 é mesclado ao modelo final (padrão: 1.0) |
| `joint_blocks.1.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto do bloco conjunto 1 do model2 é mesclado ao modelo final (padrão: 1.0) |
| `joint_blocks.2.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto do bloco conjunto 2 do model2 é mesclado ao modelo final (padrão: 1.0) |
| `joint_blocks.3.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto do bloco conjunto 3 do model2 é mesclado ao modelo final (padrão: 1.0) |
| `joint_blocks.4.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto do bloco conjunto 4 do model2 é mesclado ao modelo final (padrão: 1.0) |
| `joint_blocks.5.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto do bloco conjunto 5 do model2 é mesclado ao modelo final (padrão: 1.0) |
| `joint_blocks.6.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto do bloco conjunto 6 do model2 é mesclado ao modelo final (padrão: 1.0) |
| `joint_blocks.7.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto do bloco conjunto 7 do model2 é mesclado ao modelo final (padrão: 1.0) |
| `joint_blocks.8.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto do bloco conjunto 8 do model2 é mesclado ao modelo final (padrão: 1.0) |
| `joint_blocks.9.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto do bloco conjunto 9 do model2 é mesclado ao modelo final (padrão: 1.0) |
| `joint_blocks.10.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto do bloco conjunto 10 do model2 é mesclado ao modelo final (padrão: 1.0) |
| `joint_blocks.11.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto do bloco conjunto 11 do model2 é mesclado ao modelo final (padrão: 1.0) |
| `joint_blocks.12.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto do bloco conjunto 12 do model2 é mesclado ao modelo final (padrão: 1.0) |
| `joint_blocks.13.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto do bloco conjunto 13 do model2 é mesclado ao modelo final (padrão: 1.0) |
| `joint_blocks.14.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto do bloco conjunto 14 do model2 é mesclado ao modelo final (padrão: 1.0) |
| `joint_blocks.15.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto do bloco conjunto 15 do model2 é mesclado ao modelo final (padrão: 1.0) |
| `joint_blocks.16.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto do bloco conjunto 16 do model2 é mesclado ao modelo final (padrão: 1.0) |
| `joint_blocks.17.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto do bloco conjunto 17 do model2 é mesclado ao modelo final (padrão: 1.0) |
| `joint_blocks.18.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto do bloco conjunto 18 do model2 é mesclado ao modelo final (padrão: 1.0) |
| `joint_blocks.19.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto do bloco conjunto 19 do model2 é mesclado ao modelo final (padrão: 1.0) |
| `joint_blocks.20.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto do bloco conjunto 20 do model2 é mesclado ao modelo final (padrão: 1.0) |
| `joint_blocks.21.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto do bloco conjunto 21 do model2 é mesclado ao modelo final (padrão: 1.0) |
| `joint_blocks.22.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto do bloco conjunto 22 do model2 é mesclado ao modelo final (padrão: 1.0) |
| `joint_blocks.23.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto do bloco conjunto 23 do model2 é mesclado ao modelo final (padrão: 1.0) |
| `joint_blocks.24.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto do bloco conjunto 24 do model2 é mesclado ao modelo final (padrão: 1.0) |
| `joint_blocks.25.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto do bloco conjunto 25 do model2 é mesclado ao modelo final (padrão: 1.0) |
| `joint_blocks.26.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto do bloco conjunto 26 do model2 é mesclado ao modelo final (padrão: 1.0) |
| `joint_blocks.27.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto do bloco conjunto 27 do model2 é mesclado ao modelo final (padrão: 1.0) |
| `joint_blocks.28.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto do bloco conjunto 28 do model2 é mesclado ao modelo final (padrão: 1.0) |
| `joint_blocks.29.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto do bloco conjunto 29 do model2 é mesclado ao modelo final (padrão: 1.0) |
| `joint_blocks.30.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto do bloco conjunto 30 do model2 é mesclado ao modelo final (padrão: 1.0) |
| `joint_blocks.31.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto do bloco conjunto 31 do model2 é mesclado ao modelo final (padrão: 1.0) |
| `joint_blocks.32.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto do bloco conjunto 32 do model2 é mesclado ao modelo final (padrão: 1.0) |
| `joint_blocks.33.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto do bloco conjunto 33 do model2 é mesclado ao modelo final (padrão: 1.0) |
| `joint_blocks.34.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto do bloco conjunto 34 do model2 é mesclado ao modelo final (padrão: 1.0) |
| `joint_blocks.35.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto do bloco conjunto 35 do model2 é mesclado ao modelo final (padrão: 1.0) |
| `joint_blocks.36.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto do bloco conjunto 36 do model2 é mesclado ao modelo final (padrão: 1.0) |
| `joint_blocks.37.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto do bloco conjunto 37 do model2 é mesclado ao modelo final (padrão: 1.0) |
| `final_layer.` | FLOAT | Sim | 0.0 a 1.0 | Controla quanto da camada final do model2 é mesclada ao modelo final (padrão: 1.0) |

**Nota:** Todos os parâmetros de mesclagem aceitam valores de 0.0 a 1.0, onde 0.0 significa nenhuma contribuição do model2 e 1.0 significa contribuição total do model2 para aquele componente específico.

## Saídas

| Nome da Saída | Tipo de Dado | Descrição |
|-------------|-----------|-------------|
| `model` | MODEL | O modelo mesclado resultante, combinando características de ambos os modelos de entrada de acordo com os parâmetros de mesclagem especificados |

---
**Source fingerprint (SHA-256):** `1b491bd96cc40c6098fd8194f66753bc0f7aa485ea5f97b67b4d864cc9615c9a`
