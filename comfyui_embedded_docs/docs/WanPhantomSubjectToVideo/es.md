> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanPhantomSubjectToVideo/es.md)

El nodo WanPhantomSubjectToVideo genera contenido de video procesando entradas de condicionamiento e imágenes de referencia opcionales. Crea representaciones latentes para la generación de video y puede incorporar guía visual de imágenes de entrada cuando se proporcionan. El nodo prepara datos de condicionamiento con concatenación temporal para modelos de video y genera condicionamiento modificado junto con datos latentes de video.

## Entradas

| Parámetro | Tipo de Datos | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sí | - | Entrada de condicionamiento positivo para guiar la generación de video |
| `negative` | CONDITIONING | Sí | - | Entrada de condicionamiento negativo para evitar ciertas características |
| `vae` | VAE | Sí | - | Modelo VAE para codificar imágenes cuando se proporcionan |
| `width` | INT | No | 16 a MAX_RESOLUTION | Ancho del video de salida en píxeles (por defecto: 832, debe ser divisible por 16) |
| `height` | INT | No | 16 a MAX_RESOLUTION | Alto del video de salida en píxeles (por defecto: 480, debe ser divisible por 16) |
| `length` | INT | No | 1 a MAX_RESOLUTION | Número de frames en el video generado (por defecto: 81, debe ser divisible por 4) |
| `batch_size` | INT | No | 1 a 4096 | Número de videos a generar simultáneamente (por defecto: 1) |
| `images` | IMAGE | No | - | Imágenes de referencia opcionales para condicionamiento temporal |

**Nota:** Cuando se proporcionan `images`, se escalan automáticamente para coincidir con el `width` y `height` especificados, y solo se utilizan los primeros `length` frames para el procesamiento.

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Condicionamiento positivo modificado con concatenación temporal cuando se proporcionan imágenes |
| `negative_text` | CONDITIONING | Condicionamiento negativo modificado con concatenación temporal cuando se proporcionan imágenes |
| `negative_img_text` | CONDITIONING | Condicionamiento negativo con concatenación temporal puesta a cero cuando se proporcionan imágenes |
| `latent` | LATENT | Representación latente de video generada con las dimensiones y longitud especificadas |