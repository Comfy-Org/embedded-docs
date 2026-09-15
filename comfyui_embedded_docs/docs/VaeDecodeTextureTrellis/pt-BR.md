# VaeDecodeTextureTrellis

Este nó decodifica um latente de textura do Trellis2 em cores de voxels usando um VAE. O latente de entrada contém amostras de características esparsas com coordenadas; o nó reconstrói a cor de cada voxel e retorna o resultado como uma grade de voxels que nós posteriores, como o PaintMesh, podem usar para colorir uma malha 3D.

## Entradas

| Parâmetro | Descrição | Tipo de Dados | Obrigatório | Intervalo |
|-----------|-------------|-----------|----------|-------|
| `Amostras` | O latente de textura a ser decodificado. Contém as características das amostras e coordenadas esparsas, e pode incluir metadados opcionais, como contagens de coordenadas (`coord_counts`), referencial do modelo (`model_frame`, padrão: "y_up") e resolução de coordenadas (`coord_resolution`). | LATENT | Sim | — |
| `vae` | O VAE do Trellis2 usado para decodificar o latente de textura em cores de voxels. | VAE | Sim | — |
| `shape_subdivides` | Informações de forma usadas para orientar a reconstrução com maior nível de detalhe durante a decodificação. Ajuda a preservar a consistência estrutural em resoluções mais altas. | SHAPE_SUBDIVIDES | Sim | — |

Observação: Quando o latente `samples` inclui `coord_counts`, as contagens devem ser não negativas, seu total deve corresponder ao número de linhas de coordenadas, e cada lote deve conter exatamente o número esperado de linhas; caso contrário, o nó gera um erro. Se o `model_frame` do latente for "z_up", as coordenadas de voxels decodificadas são remapeadas para Y-up para que se alinhem aos vértices da malha. Quando `coord_resolution` é fornecido, a resolução da textura de saída é esse valor multiplicado por 16. Caso contrário, ela é inferida a partir da maior coordenada de voxel mais um, arredondada para cima para um dos valores 256, 512, 1024, 1536 ou 2048; se o valor necessário exceder 2048, esse valor maior será usado. Se nenhuma coordenada estiver disponível, a resolução padrão é 1024.

## Saídas

| Nome da Saída | Descrição | Tipo de Dados |
|-------------|-------------|-----------|
| `voxel_colors` | Dados de voxels decodificados contendo coordenadas, características de cor e resolução de textura. Cada voxel tem 6 canais de cor: cor base (RGB), metálico, rugosidade e alfa, todos no intervalo [0, 1]. Consumidores de cor de vértice, como o PaintMesh, usam os 3 primeiros canais. | VOXEL |

> Esta documentação foi gerada por IA. Se você encontrar erros ou tiver sugestões de melhoria, sinta-se à vontade para contribuir! [Editar no GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VaeDecodeTextureTrellis/pt-BR.md)

---
**Source fingerprint (SHA-256):** `952ea7d7a0147519392bebe352a0da731462db278c8640fa527aa5b6f64e4aa7`
