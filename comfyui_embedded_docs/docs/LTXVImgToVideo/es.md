> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideo/es.md)

El nodo LTXVImgToVideo convierte una imagen de entrada en una representación latente de video para modelos de generación de video. Toma una sola imagen y la extiende en una secuencia de fotogramas utilizando el codificador VAE, luego aplica acondicionamiento con control de intensidad para determinar cuánto del contenido original de la imagen se conserva versus se modifica durante la generación del video.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `positivo` | CONDITIONING | Sí | - | Prompts de acondicionamiento positivo para guiar la generación del video |
| `negativo` | CONDITIONING | Sí | - | Prompts de acondicionamiento negativo para evitar ciertos elementos en el video |
| `vae` | VAE | Sí | - | Modelo VAE utilizado para codificar la imagen de entrada en el espacio latente |
| `imagen` | IMAGE | Sí | - | Imagen de entrada que se convertirá en fotogramas de video |
| `ancho` | INT | No | 64 a MAX_RESOLUTION | Ancho del video de salida en píxeles (por defecto: 768, paso: 32) |
| `altura` | INT | No | 64 a MAX_RESOLUTION | Alto del video de salida en píxeles (por defecto: 512, paso: 32) |
| `longitud` | INT | No | 9 a MAX_RESOLUTION | Número de fotogramas en el video generado (por defecto: 97, paso: 8) |
| `tamaño_lote` | INT | No | 1 a 4096 | Número de videos a generar simultáneamente (por defecto: 1) |
| `fuerza` | FLOAT | No | 0.0 a 1.0 | Control sobre cuánto se modifica la imagen original durante la generación del video, donde 1.0 preserva la mayor parte del contenido original y 0.0 permite la máxima modificación (por defecto: 1.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `negativo` | CONDITIONING | Acondicionamiento positivo procesado con máscara de fotogramas de video aplicada |
| `latente` | CONDITIONING | Acondicionamiento negativo procesado con máscara de fotogramas de video aplicada |
| `latent` | LATENT | Representación latente de video que contiene los fotogramas codificados y la máscara de ruido para la generación del video |