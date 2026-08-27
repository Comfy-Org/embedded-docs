# VaeDecodeTextureTrellis

Este nodo decodifica un latente de textura Trellis2 en colores de voxel utilizando un VAE. El latente de entrada contiene muestras de características dispersas con coordenadas; el nodo reconstruye el color de cada voxel y devuelve el resultado como una rejilla de voxel que nodos posteriores, como PaintMesh, pueden usar para colorear una malla 3D.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `samples` | El latente de textura a decodificar. Contiene las características de muestra y las coordenadas dispersas, y puede incluir metadatos opcionales como conteos de coordenadas, marco del modelo y resolución de coordenadas. | LATENT | Sí | — |
| `vae` | El VAE Trellis2 utilizado para decodificar el latente de textura en colores de voxel. | VAE | Sí | — |
| `shape_subdivides` | Información de forma utilizada para guiar la reconstrucción de mayor detalle durante la decodificación. Ayuda a preservar la consistencia estructural en resoluciones más altas. | SHAPE_SUBDIVIDES | Sí | — |

Nota: Cuando el latente `samples` incluye conteos de coordenadas, estos deben ser no negativos, su total debe coincidir con el número de filas de coordenadas, y cada lote debe tener exactamente el número esperado de filas; de lo contrario, el nodo genera un error. Si el marco del modelo del latente es "z_up", las coordenadas de voxel decodificadas se reasignan a Y-up para que se alineen con los vértices de la malla. Cuando se proporciona una resolución de coordenadas, la resolución de textura de salida es ese valor multiplicado por 16; de lo contrario, se infiere de la coordenada de voxel más grande y se redondea a uno de 256, 512, 1024, 1536 o 2048 (1024 cuando no hay coordenadas disponibles).

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `voxel_colors` | Datos de voxel decodificados que contienen coordenadas, características de color y resolución de textura. Cada voxel tiene 6 canales de color: color base (RGB), metálico, rugosidad y alfa, todos en el rango [0, 1]. Los consumidores de color por vértice, como PaintMesh, utilizan los primeros 3 canales. | VOXEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VaeDecodeTextureTrellis/es.md)

---
**Source fingerprint (SHA-256):** `cfbe59efb18d2c3c7c597c5212900fea54d660aa98005817debf4711401a6967`
