# VaeDecodeTextureTrellis

Este nó decodifica um latente de textura Trellis2 em cores de voxel usando uma VAE. O latente de entrada contém amostras de características esparsas com coordenadas; o nó reconstrói a cor para cada voxel e retorna o resultado como uma grade de voxels que nós posteriores, como o PaintMesh, podem usar para colorir uma malha 3D.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|---------------|-------------|-----------|
| `Amostras` | O latente de textura a ser decodificado. Contém as características das amostras e coordenadas esparsas, e pode incluir metadados opcionais, como contagens de coordenadas, frame do modelo e resolução de coordenadas. | LATENT | Sim | — |
| `vae` | A VAE Trellis2 usada para decodificar o latente de textura em cores de voxel. | VAE | Sim | — |
| `shape_subdivides` | Informações de forma usadas para orientar a reconstrução em maior detalhe durante a decodificação. Ajuda a preservar a consistência estrutural em resoluções mais altas. | SHAPE_SUBDIVIDES | Sim | — |

Observação: quando o latente `samples` inclui contagens de coordenadas, as contagens devem ser não negativas, o total delas deve corresponder ao número de linhas de coordenadas, e cada lote deve ter exatamente o número esperado de linhas; caso contrário, o nó gera um erro. Se o frame do modelo do latente for `z_up`, as coordenadas de voxel decodificadas são remapeadas para o sistema Y-up, de modo a se alinharem aos vértices da malha. Quando uma resolução de coordenadas é fornecida, a resolução da textura de saída é esse valor multiplicado por 16; caso contrário, ela é inferida a partir da maior coordenada de voxel e arredondada para cima para um dos seguintes valores: 256, 512, 1024, 1536 ou 2048 (1024 quando nenhuma coordenada está disponível).

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|---------------|-------------|---------------|
| `voxel_colors` | Dados de voxel decodificados contendo coordenadas, características de cor e resolução de textura. Cada voxel tem 6 canais de cor: cor base (RGB), metálico, rugosidade e alfa, todos no intervalo [0, 1]. Consumidores de cor por vértice, como o PaintMesh, usam os primeiros 3 canais. | VOXEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VaeDecodeTextureTrellis/pt-BR.md)

---
**Source fingerprint (SHA-256):** `cfbe59efb18d2c3c7c597c5212900fea54d660aa98005817debf4711401a6967`
