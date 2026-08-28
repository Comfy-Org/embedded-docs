# ModelMergeCosmos7B

O nó **ModelMergeCosmos7B** mescla dois modelos de IA usando uma combinação ponderada de componentes específicos. Ele permite controle fino sobre como diferentes partes dos modelos são combinadas, ajustando pesos individuais para incorporações de posição, blocos de transformadores e camadas finais.

## Entradas

| Parâmetro | Descrição | Tipo de Dado | Obrigatório | Faixa |
| --- | --- | --- | --- | --- |
| `model1` | Primeiro modelo a mesclar | MODEL | Sim | - |
| `model2` | Segundo modelo a mesclar | MODEL | Sim | - |
| `pos_embedder.` | Peso para o componente de incorporação de posição (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `extra_pos_embedder.` | Peso para o componente extra de incorporação de posição (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `x_embedder.` | Peso para o componente incorporador x (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `t_embedder.` | Peso para o componente incorporador t (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `affline_norm.` | Peso para o componente de normalização afim (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.block0.` | Peso para o bloco de transformador 0 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.block1.` | Peso para o bloco de transformador 1 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.block2.` | Peso para o bloco de transformador 2 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.block3.` | Peso para o bloco de transformador 3 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.block4.` | Peso para o bloco de transformador 4 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.block5.` | Peso para o bloco de transformador 5 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.block6.` | Peso para o bloco de transformador 6 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.block7.` | Peso para o bloco de transformador 7 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.block8.` | Peso para o bloco de transformador 8 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.block9.` | Peso para o bloco de transformador 9 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.block10.` | Peso para o bloco de transformador 10 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.block11.` | Peso para o bloco de transformador 11 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.block12.` | Peso para o bloco de transformador 12 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.block13.` | Peso para o bloco de transformador 13 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.block14.` | Peso para o bloco de transformador 14 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.block15.` | Peso para o bloco de transformador 15 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.block16.` | Peso para o bloco de transformador 16 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.block17.` | Peso para o bloco de transformador 17 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.block18.` | Peso para o bloco de transformador 18 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.block19.` | Peso para o bloco de transformador 19 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.block20.` | Peso para o bloco de transformador 20 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.block21.` | Peso para o bloco de transformador 21 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.block22.` | Peso para o bloco de transformador 22 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.block23.` | Peso para o bloco de transformador 23 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.block24.` | Peso para o bloco de transformador 24 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.block25.` | Peso para o bloco de transformador 25 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.block26.` | Peso para o bloco de transformador 26 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `blocks.block27.` | Peso para o bloco de transformador 27 (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |
| `final_layer.` | Peso para o componente de camada final (padrão: 1.0) | FLOAT | Sim | 0.0 - 1.0 |

Todos os parâmetros de peso aceitam valores de 0.0 a 1.0 em passos de 0.01 e o padrão é 1.0.

## Saídas

| Nome da Saída | Descrição | Tipo de Dado |
| --- | --- | --- |
| `model` | O modelo mesclado que combina características de ambos os modelos de entrada | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmos7B/pt-BR.md)

---
**Source fingerprint (SHA-256):** `2cc4dcaa3576c5383c630e233cef55dedc8d742c20197cc83f5832dc9e887dac`
