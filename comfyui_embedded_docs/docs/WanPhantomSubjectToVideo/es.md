# WanPhantomSubjectToVideo

El nodo WanPhantomSubjectToVideo prepara los datos de condicionamiento y un latent para la generación de videos Wan. Crea un video latent vacío a partir del ancho, alto, longitud y tamaño de lote solicitados y, cuando se suministran imágenes de referencia, las codifica con el VAE y las añade a los condicionamientos como guía visual en la dimensión temporal.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `positivo` | Entrada de condicionamiento positivo para guiar la generación de video | CONDITIONING | Sí | - |
| `negativo` | Entrada de condicionamiento negativo para evitar ciertas características | CONDITIONING | Sí | - |
| `vae` | Modelo VAE utilizado para codificar las imágenes de referencia cuando se proporcionan | VAE | Sí | - |
| `ancho` | Ancho del video de salida en píxeles (predeterminado: 832, debe ser múltiplo de 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `alto` | Alto del video de salida en píxeles (predeterminado: 480, debe ser múltiplo de 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `longitud` | Número de fotogramas del video generado (predeterminado: 81, debe ser múltiplo de 4) | INT | Sí | 1 a MAX_RESOLUTION |
| `tamaño_lote` | Número de videos a generar simultáneamente (predeterminado: 1) | INT | Sí | 1 a 4096 |
| `imágenes` | Imágenes de referencia opcionales utilizadas como guía visual en la dimensión temporal | IMAGE | No | - |

**Nota:** Cuando se proporcionan `images`, estas se escalan automáticamente para coincidir con el `width` y `height` especificados, y solo se utilizan las primeras `length` imágenes para el procesamiento. Cada imagen se codifica con el `vae` y se concatena a lo largo de la dimensión temporal; solo se usan los canales RGB de cada imagen.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `positivo` | Condicionamiento positivo con concatenación en la dimensión temporal de las imágenes de referencia codificadas cuando se proporcionan imágenes; de lo contrario, se devuelve la entrada `positive` sin cambios | CONDITIONING |
| `texto_negativo` | Condicionamiento negativo con concatenación en la dimensión temporal de las imágenes de referencia codificadas cuando se proporcionan imágenes; de lo contrario, se devuelve la entrada `negative` sin cambios | CONDITIONING |
| `texto_img_negativa` | Condicionamiento negativo con concatenación en la dimensión temporal puesta a cero cuando se proporcionan imágenes; de lo contrario, se devuelve la entrada `negative` sin cambios | CONDITIONING |
| `latente` | Tensor de video latent relleno con ceros y 16 canales; su cantidad de fotogramas se deriva de `length` y sus dimensiones espaciales de `height` y `width` | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanPhantomSubjectToVideo/es.md)

---
**Source fingerprint (SHA-256):** `a1853382f6e564f66262b69dd7b06cc58e26b93386a460a98e6fcc2ff6acf12b`
