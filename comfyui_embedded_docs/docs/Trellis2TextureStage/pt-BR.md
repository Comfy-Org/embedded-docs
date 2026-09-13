# Trellis2TextureStage

Este nó configura a passagem de amostragem do estágio de textura para a geração Trellis2. Ele lê o layout de coordenadas e o latent de forma por voxel a partir do latent de forma recebido, constrói um latent esparso vazio com 32 canais no mesmo layout de coordenadas e anexa os metadados necessários do estágio de textura ao condicionamento.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `positive` | O condicionamento positivo usado para a passagem de geração de textura. Os metadados do estágio de textura são anexados a ele. | CONDITIONING | Sim | - |
| `negative` | O condicionamento negativo usado para a passagem de geração de textura. Os metadados do estágio de textura são anexados a ele. | CONDITIONING | Sim | - |
| `shape_latent` | O dict latent produzido por Trellis2ShapeStage ou Trellis2UpsampleStage. Ele deve conter `coords` (o layout de coordenadas, forma [N, 4]) e `samples` (o latent de forma por voxel); `coord_resolution` e `model_frame` são opcionais. | LATENT | Sim | - |

Notas:
- `shape_latent` deve ser a saída de Trellis2ShapeStage ou Trellis2UpsampleStage; ele fornece o layout de coordenadas e o latent de forma por voxel usado pela passagem de textura.
- O layout de coordenadas é validado: os ids de lote na primeira coluna de `coords` devem ser não negativos e contíguos, e o número total de linhas deve corresponder às contagens de coordenadas.
- O latent de forma é aceito tanto como um tensor esparso 4D (que é achatado junto com suas coordenadas) quanto já na forma achatada.
- Quando `positive` carrega um pacote de recursos de projeção (condicionamento Pixal3D) e `shape_latent` inclui `coord_resolution`, recursos de projeção com resolução de textura 1024 são calculados e anexados ao condicionamento.
- O frame do modelo é lido de `shape_latent`; quando ausente, o padrão é `"y_up"` se recursos de projeção estiverem presentes e `"z_up"` caso contrário.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `positive` | O condicionamento positivo com metadados do estágio de textura anexados (modo de geração, coordenadas, contagens de coordenadas, latent de forma, frame do modelo e recursos de projeção quando aplicável). | CONDITIONING |
| `negative` | O condicionamento negativo com os mesmos metadados do estágio de textura anexados. | CONDITIONING |
| `latent` | Um novo latent esparso vazio com 32 canais no mesmo layout de coordenadas do latent de forma recebido. Seu dict inclui `samples`, `type` ("trellis2"), `coords`, `coord_counts` e `model_frame`; `coord_resolution` é incluído quando disponível. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2TextureStage/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ae612021af7c74cd09206d905e7b800fa48367a22daf9b0335b444c854a78b1e`
