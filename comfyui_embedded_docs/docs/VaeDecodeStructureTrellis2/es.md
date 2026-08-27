# VaeDecodeStructureTrellis2

Este nodo convierte muestras latentes de estructura de Trellis en una rejilla de voxeles 3D utilizando el decodificador de estructura de un VAE. Lee solo los primeros 8 canales del latente, reconstruye la ocupación de voxeles y ajusta la resolución de salida a 32 o 64 según lo solicitado.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `samples` | La representación latente de la estructura a decodificar. Solo los primeros 8 canales del latente se utilizan para la decodificación. | LATENT | Sí | - |
| `vae` | El VAE cuyo decodificador de estructura convierte el latente en una rejilla de voxeles. La decodificación se realiza en lotes. | VAE | Sí | - |
| `resolution` | La resolución espacial objetivo de la rejilla de voxeles de salida (por defecto: "32"). Si la rejilla decodificada tiene una resolución diferente, se reduce de resolución para que coincida. | COMBO | Sí | "32"<br>"64" |

Nota: Cuando la resolución de la rejilla de voxeles decodificada difiere de la `resolution` seleccionada, la rejilla se reduce de resolución mediante agrupación máxima 3D al tamaño solicitado.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `voxel` | Una rejilla binaria de ocupación de voxeles como un tensor flotante con forma [batch, depth, height, width]. Los valores son 1.0 para voxeles ocupados y 0.0 para voxeles vacíos. | VOXEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VaeDecodeStructureTrellis2/es.md)

---
**Source fingerprint (SHA-256):** `37764ef7351b3619d4cddb57b11d9a0da24dadeedc0fc0f70d089038d37e03b0`
