> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanPhantomSubjectToVideo/es.md)

El nodo WanPhantomSubjectToVideo genera contenido de video procesando entradas de condicionamiento e imágenes de referencia opcionales. Crea representaciones latentes para la generación de video y puede incorporar guía visual a partir de imágenes de entrada cuando se proporcionan. El nodo prepara datos de condicionamiento con concatenación de dimensión temporal para modelos de video y genera condicionamiento modificado junto con datos de video latente generados.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sí | - | Entrada de condicionamiento positivo para guiar la generación de video |
| `negative` | CONDITIONING | Sí | - | Entrada de condicionamiento negativo para evitar ciertas características |
| `vae` | VAE | Sí | - | Modelo VAE para codificar imágenes cuando se proporcionan |
| `width` | INT | Sí | 16 a MAX_RESOLUTION | Ancho del video de salida en píxeles (predeterminado: 832, debe ser divisible por 16) |
| `height` | INT | Sí | 16 a MAX_RESOLUTION | Alto del video de salida en píxeles (predeterminado: 480, debe ser divisible por 16) |
| `length` | INT | Sí | 1 a MAX_RESOLUTION | Número de fotogramas en el video generado (predeterminado: 81, debe ser divisible por 4) |
| `batch_size` | INT | Sí | 1 a 4096 | Número de videos a generar simultáneamente (predeterminado: 1) |
| `images` | IMAGE | No | - | Imágenes de referencia opcionales para condicionamiento de dimensión temporal |

**Nota:** Cuando se proporcionan `images`, se redimensionan automáticamente para coincidir con el `width` y `height` especificados, y solo se utilizan los primeros `length` fotogramas para el procesamiento.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Condicionamiento positivo modificado con concatenación de dimensión temporal cuando se proporcionan imágenes |
| `negative_text` | CONDITIONING | Condicionamiento negativo modificado con concatenación de dimensión temporal cuando se proporcionan imágenes |
| `negative_img_text` | CONDITIONING | Condicionamiento negativo con concatenación de dimensión temporal puesta a cero cuando se proporcionan imágenes |
| `latent` | LATENT | Representación de video latente generada con las dimensiones y longitud especificadas |

---
**Source fingerprint (SHA-256):** `2e3e8277dca9e998220fc5939c2cc72fdc15e80cc4b95daa33f5b92e2270dd73`
