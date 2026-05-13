> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunInpaintToVideo/es.md)

El nodo WanFunInpaintToVideo crea secuencias de video mediante interpolación entre imágenes de inicio y fin. Toma condicionamientos positivo y negativo junto con imágenes de fotogramas opcionales para generar latentes de video. El nodo maneja la generación de video con dimensiones configurables y parámetros de longitud.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `positivo` | CONDITIONING | Sí | - | Indicaciones de condicionamiento positivo para la generación de video |
| `negativo` | CONDITIONING | Sí | - | Indicaciones de condicionamiento negativo a evitar en la generación de video |
| `vae` | VAE | Sí | - | Modelo VAE para operaciones de codificación/decodificación |
| `ancho` | INT | Sí | 16 a MAX_RESOLUTION | Ancho del video de salida en píxeles (predeterminado: 832, paso: 16) |
| `alto` | INT | Sí | 16 a MAX_RESOLUTION | Alto del video de salida en píxeles (predeterminado: 480, paso: 16) |
| `longitud` | INT | Sí | 1 a MAX_RESOLUTION | Número de fotogramas en la secuencia de video (predeterminado: 81, paso: 4) |
| `tamaño_de_lote` | INT | Sí | 1 a 4096 | Número de videos a generar en un lote (predeterminado: 1) |
| `clip_vision_output` | CLIP_VISION_OUTPUT | No | - | Salida de visión CLIP opcional para condicionamiento adicional |
| `imagen_inicial` | IMAGE | No | - | Imagen de fotograma inicial opcional para la generación de video |
| `imagen_final` | IMAGE | No | - | Imagen de fotograma final opcional para la generación de video |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `negativo` | CONDITIONING | Salida de condicionamiento positivo procesado |
| `latente` | CONDITIONING | Salida de condicionamiento negativo procesado |
| `latent` | LATENT | Representación latente del video generado |

---
**Source fingerprint (SHA-256):** `bbc5c2614f5fc21877345b3f01686ea57bee5108cdb253fb5dbf4b2cce9e59dd`
