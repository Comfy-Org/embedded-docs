# ModelMergeSD2

O nó ModelMergeSD2 mescla dois modelos Stable Diffusion 2.x combinando seus componentes correspondentes, com um peso separado para o embedding de tempo, o embedding de rótulo e cada bloco de entrada, intermediário e de saída. O layout dos blocos é o mesmo do ModelMergeSD1, portanto ambos os nós expõem o mesmo conjunto de proporções.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
| --- | --- | --- | --- | --- |
| `model1` | O primeiro modelo a mesclar. Tudo aquilo com que o segundo modelo não contribui é mantido a partir deste modelo | MODEL | Sim | - |
| `model2` | O segundo modelo a mesclar. Seus pesos são misturados de acordo com as proporções abaixo | MODEL | Sim | - |
| `time_embed.` | Proporção de mistura para a camada de embedding de tempo (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `label_emb.` | Proporção de mistura para a camada de embedding de rótulo (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `input_blocks.0.` até `input_blocks.11.` | Proporção de mistura para cada um dos 12 blocos de entrada (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `middle_block.0.` até `middle_block.2.` | Proporção de mistura para cada um dos 3 blocos intermediários (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `output_blocks.0.` até `output_blocks.11.` | Proporção de mistura para cada um dos 12 blocos de saída (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |
| `out.` | Proporção de mistura para a camada de saída (padrão: 1.0) | FLOAT | Sim | 0.0 a 1.0 (passo: 0.01) |

Uma proporção de 0.0 mantém esse componente como está em `model1`; uma proporção de 1.0 o obtém inteiramente de `model2`; e valores intermediários produzem uma mistura ponderada. Ambas as entradas devem ser modelos Stable Diffusion 2.x com a mesma estrutura de blocos.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
| --- | --- | --- |
| `MODEL` | O modelo mesclado, combinando ambas as entradas de acordo com as proporções especificadas | MODEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD2/pt-BR.md)

---
**Source fingerprint (SHA-256):** `b9d53f126139412fbd8b21be72e1dcdb02736519ab4dc9e28c7840d69acb7c87`
