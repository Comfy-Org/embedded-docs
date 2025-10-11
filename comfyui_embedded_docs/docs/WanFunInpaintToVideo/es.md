> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunInpaintToVideo/es.md)

El nodo WanFunInpaintToVideo crea secuencias de video mediante la técnica de inpaint entre imágenes de inicio y fin. Toma condicionamientos positivos y negativos junto con imágenes de fotogramas opcionales para generar latentes de video. El nodo maneja la generación de video con parámetros configurables de dimensiones y longitud.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sí | - | Prompts de condicionamiento positivo para la generación de video |
| `negative` | CONDITIONING | Sí | - | Prompts de condicionamiento negativo a evitar en la generación de video |
| `vae` | VAE | Sí | - | Modelo VAE para operaciones de codificación/decodificación |
| `width` | INT | Sí | 16 a MAX_RESOLUTION | Ancho del video de salida en píxeles (valor por defecto: 832, paso: 16) |
| `height` | INT | Sí | 16 a MAX_RESOLUTION | Alto del video de salida en píxeles (valor por defecto: 480, paso: 16) |
| `length` | INT | Sí | 1 a MAX_RESOLUTION | Número de fotogramas en la secuencia de video (valor por defecto: 81, paso: 4) |
| `batch_size` | INT | Sí | 1 a 4096 | Número de videos a generar en un lote (valor por defecto: 1) |
| `clip_vision_output` | CLIP_VISION_OUTPUT | No | - | Salida de visión CLIP opcional para condicionamiento adicional |
| `start_image` | IMAGE | No | - | Imagen de fotograma inicial opcional para la generación de video |
| `end_image` | IMAGE | No | - | Imagen de fotograma final opcional para la generación de video |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Salida de condicionamiento positivo procesada |
| `negative` | CONDITIONING | Salida de condicionamiento negativo procesada |
| `latent` | LATENT | Representación latente del video generado |