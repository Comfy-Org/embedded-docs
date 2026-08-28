# Trellis2TextureStage

Este nó configura o passe de amostragem do estágio de textura para a geração Trellis2. Ele lê o layout de coordenadas e o latente de forma por voxel do latente de forma de entrada, constrói um novo latente esparso vazio com 32 canais no mesmo layout de coordenadas e anexa os metadados necessários do estágio de textura ao condicionamento.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Faixa |
|-----------|-------------|-----------|----------|-------|
| `positive` | O condicionamento positivo usado no passe de geração de textura. Os metadados do estágio de textura são anexados a ele. | CONDITIONING | Sim | - |
| `negative` | O condicionamento negativo usado no passe de geração de textura. Os metadados do estágio de textura são anexados a ele. | CONDITIONING | Sim | - |
| `shape_latent` | O dicionário latente produzido por Trellis2ShapeStage ou Trellis2UpsampleStage. Deve conter `coords` (o layout de coordenadas, formato [N, 4]) e `samples` (o latente de forma por voxel); `coord_resolution` e `model_frame` são opcionais. | LATENT | Sim | - |

Notas:
- `shape_latent` deve ser a saída de Trellis2ShapeStage ou Trellis2UpsampleStage; ele fornece o layout de coordenadas e o latente de forma por voxel usado no passe de textura.
- O layout de coordenadas é validado: os IDs de lote na primeira coluna de `coords` devem ser não negativos e contíguos, e o número total de linhas deve corresponder às contagens de coordenadas.
- Quando `positive` contém um pacote de características de projeção (condicionamento Pixal3D) e `shape_latent` inclui `coord_resolution`, as características de projeção na resolução de textura 1024 são calculadas e anexadas ao condicionamento.
- O frame do modelo é lido de `shape_latent`; quando ausente, o padrão é `"y_up"` se houver características de projeção e `"z_up"` caso contrário.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `positive` | O condicionamento positivo com os metadados do estágio de textura anexados (modo de geração, coordenadas, contagens de coordenadas, latente de forma, frame do modelo e características de projeção quando aplicável). | CONDITIONING |
| `negative` | O condicionamento negativo com os mesmos metadados do estágio de textura anexados. | CONDITIONING |
| `latent` | Um novo latente esparso vazio com 32 canais no mesmo layout de coordenadas do latente de forma de entrada. Seu dicionário inclui `samples`, `type` (`"trellis2"`), `coords`, `coord_counts` e `model_frame`; `coord_resolution` é incluído quando disponível. | LATENT |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2TextureStage/pt-BR.md)

---
**Source fingerprint (SHA-256):** `ae612021af7c74cd09206d905e7b800fa48367a22daf9b0335b444c854a78b1e`
