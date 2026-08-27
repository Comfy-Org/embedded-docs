# Trellis2ShapeStage

Este nó configura a primeira passada de amostragem para geração de forma do pipeline Trellis2. Ele recebe o voxel de estrutura densa produzido por VaeDecodeStructureTrellis2, extrai as coordenadas esparsas dos voxels preenchidos, cria um tensor latente esparso vazio e anexa os metadados de amostragem ao condicionamento para que o modelo possa lê-los durante a amostragem. Para a segunda passada de forma após o upsampling, use Trellis2UpsampleStage, que combina a cascata com a configuração do estágio da segunda passada.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `positive` | O condicionamento positivo a ser preparado para o estágio de forma. Pode ser um condicionamento Trellis2 padrão ou um condicionamento Pixal3D que forneça um pacote de características de projeção; quando houver características de projeção, elas são calculadas para o estágio selecionado e anexadas ao condicionamento de saída. | CONDITIONING | Sim | Qualquer condicionamento Trellis2 ou Pixal3D |
| `negative` | O condicionamento negativo a ser preparado para o estágio de forma. Os mesmos metadados do estágio de forma anexados ao condicionamento positivo também são anexados a ele. | CONDITIONING | Sim | Qualquer condicionamento Trellis2 ou Pixal3D |
| `voxel` | Voxel de estrutura densa proveniente de VaeDecodeStructureTrellis2. | VOXEL | Sim | Qualquer grade de voxels; a resolução da grade (voxels por eixo) seleciona o estágio do pipeline |

### Notas

- A resolução da grade de voxels seleciona o estágio do pipeline: resolução menor ou igual a 32 usa o modo `shape_generation_512` com o estágio `shape_512`; resolução maior que 32 usa o modo `shape_generation` com o estágio `shape_1024`.
- O voxel deve conter pelo menos um voxel preenchido; um voxel vazio gera um erro. Os índices de lote derivados do voxel devem ser não negativos e contíguos.
- Quando o condicionamento `positive` contém um `proj_feat_pack` (como fornecido pelo condicionamento Pixal3D), as características de projeção são calculadas para o estágio selecionado e o referencial do modelo do tensor latente de saída é definido como `y_up`. Caso contrário, nenhuma característica de projeção é anexada e o referencial do modelo é definido como `z_up`.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `positive` | O condicionamento positivo com os metadados do estágio de forma anexados: modo de geração, coordenadas esparsas, contagens de coordenadas por lote e características de projeção quando o condicionamento de origem as fornece. | CONDITIONING |
| `negative` | O condicionamento negativo com os mesmos metadados do estágio de forma anexados. | CONDITIONING |
| `latent` | Um tensor latente esparso vazio (formato: tamanho do lote, 32, contagem de tokens, 1) juntamente com as coordenadas esparsas extraídas, contagens de coordenadas por lote, resolução de coordenadas, o marcador de tipo `trellis2` e a orientação do referencial do modelo. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2ShapeStage/pt-BR.md)

---
**Source fingerprint (SHA-256):** `7dbee8a5b6ef7111f07def4dbe1cc4908533e00ffcb775f5a284099360c7eed3`
