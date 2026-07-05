# WanFunInpaintToVideo

El nodo WanFunInpaintToVideo crea secuencias de video mediante interpolación entre imágenes de inicio y fin. Toma condicionamientos positivo y negativo junto con imágenes de fotogramas opcionales para generar latentes de video. El nodo maneja la generación de video con dimensiones configurables y parámetros de longitud.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `positivo` | Indicaciones de condicionamiento positivo para la generación de video | CONDITIONING | Sí | - |
| `negativo` | Indicaciones de condicionamiento negativo a evitar en la generación de video | CONDITIONING | Sí | - |
| `vae` | Modelo VAE para operaciones de codificación/decodificación | VAE | Sí | - |
| `ancho` | Ancho del video de salida en píxeles (predeterminado: 832, paso: 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `alto` | Alto del video de salida en píxeles (predeterminado: 480, paso: 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `longitud` | Número de fotogramas en la secuencia de video (predeterminado: 81, paso: 4) | INT | Sí | 1 a MAX_RESOLUTION |
| `tamaño_de_lote` | Número de videos a generar en un lote (predeterminado: 1) | INT | Sí | 1 a 4096 |
| `clip_vision_output` | Salida de visión CLIP opcional para condicionamiento adicional | CLIP_VISION_OUTPUT | No | - |
| `imagen_inicial` | Imagen de fotograma inicial opcional para la generación de video | IMAGE | No | - |
| `imagen_final` | Imagen de fotograma final opcional para la generación de video | IMAGE | No | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `negativo` | Salida de condicionamiento positivo procesado | CONDITIONING |
| `latente` | Salida de condicionamiento negativo procesado | CONDITIONING |
| `latent` | Representación latente del video generado | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunInpaintToVideo/es.md)

---
**Source fingerprint (SHA-256):** `bbc5c2614f5fc21877345b3f01686ea57bee5108cdb253fb5dbf4b2cce9e59dd`
