# WanPhantomSubjectToVideo

El nodo WanPhantomSubjectToVideo genera contenido de video procesando entradas de condicionamiento e imágenes de referencia opcionales. Crea representaciones latentes para la generación de video y puede incorporar guía visual de las imágenes de entrada cuando se proporcionan. El nodo prepara datos de condicionamiento con concatenación en la dimensión temporal para los modelos de video Wan y genera condicionamiento modificado junto con los datos de video latente generados.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `positive` | Entrada de condicionamiento positivo para guiar la generación de video | CONDITIONING | Sí | - |
| `negative` | Entrada de condicionamiento negativo para evitar ciertas características | CONDITIONING | Sí | - |
| `vae` | Modelo VAE para codificar imágenes cuando se proporcionan | VAE | Sí | - |
| `width` | Ancho del video de salida en píxeles (por defecto: 832, debe ser divisible por 16) | INT | Sí | 16 to MAX_RESOLUTION |
| `height` | Alto del video de salida en píxeles (por defecto: 480, debe ser divisible por 16) | INT | Sí | 16 to MAX_RESOLUTION |
| `length` | Número de fotogramas en el video generado (por defecto: 81, debe ser divisible por 4) | INT | Sí | 1 to MAX_RESOLUTION |
| `batch_size` | Número de videos a generar simultáneamente (por defecto: 1) | INT | Sí | 1 to 4096 |
| `images` | Imágenes de referencia opcionales para el condicionamiento en la dimensión temporal | IMAGE | No | - |

**Nota:** Cuando se proporcionan `images`, se escalan automáticamente para coincidir con `width` y `height` especificados, y solo se utilizan los primeros `length` fotogramas para el procesamiento. Cada imagen se reduce a sus primeros 3 canales de color antes de ser codificada por el VAE. Cuando no se proporcionan `images`, las entradas de condicionamiento pasan sin cambios.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `positive` | Condicionamiento positivo modificado con concatenación en la dimensión temporal cuando se proporcionan imágenes | CONDITIONING |
| `negative_text` | Condicionamiento negativo modificado con concatenación en la dimensión temporal cuando se proporcionan imágenes | CONDITIONING |
| `negative_img_text` | Condicionamiento negativo con concatenación en la dimensión temporal puesta a cero cuando se proporcionan imágenes | CONDITIONING |
| `latent` | Representación de video latente rellena con ceros, con 16 canales, una dimensión temporal de ((length - 1) // 4) + 1, y dimensiones espaciales de height // 8 y width // 8 | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanPhantomSubjectToVideo/es.md)

---
**Source fingerprint (SHA-256):** `a1853382f6e564f66262b69dd7b06cc58e26b93386a460a98e6fcc2ff6acf12b`
