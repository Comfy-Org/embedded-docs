> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanVaceToVideo/es.md)

El nodo WanVaceToVideo procesa datos de condicionamiento de video para modelos de generación de video. Toma entradas de condicionamiento positivo y negativo junto con datos de control de video y prepara representaciones latentes para la generación de video. El nodo maneja el escalado de video, el enmascaramiento y la codificación VAE para crear la estructura de condicionamiento adecuada para modelos de video.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `positive` | CONDITIONING | Sí | - | Entrada de condicionamiento positivo para guiar la generación |
| `negative` | CONDITIONING | Sí | - | Entrada de condicionamiento negativo para guiar la generación |
| `vae` | VAE | Sí | - | Modelo VAE utilizado para codificar imágenes y fotogramas de video |
| `width` | INT | Sí | 16 a MAX_RESOLUTION | Ancho del video de salida en píxeles (predeterminado: 832, paso: 16) |
| `height` | INT | Sí | 16 a MAX_RESOLUTION | Alto del video de salida en píxeles (predeterminado: 480, paso: 16) |
| `length` | INT | Sí | 1 a MAX_RESOLUTION | Número de fotogramas en el video (predeterminado: 81, paso: 4) |
| `batch_size` | INT | Sí | 1 a 4096 | Número de videos a generar simultáneamente (predeterminado: 1) |
| `strength` | FLOAT | Sí | 0.0 a 1000.0 | Intensidad de control para el condicionamiento de video (predeterminado: 1.0, paso: 0.01) |
| `control_video` | IMAGE | No | - | Video de entrada opcional para condicionamiento de control |
| `control_masks` | MASK | No | - | Máscaras opcionales para controlar qué partes del video modificar |
| `reference_image` | IMAGE | No | - | Imagen de referencia opcional para condicionamiento adicional |

**Nota:** Cuando se proporciona `control_video`, se escalará para que coincida con el ancho y alto especificados. Si se proporcionan `control_masks`, deben coincidir con las dimensiones del video de control. La `reference_image` se codifica a través del VAE y se antepone a la secuencia latente cuando se proporciona.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | Condicionamiento positivo con datos de control de video aplicados |
| `negative` | CONDITIONING | Condicionamiento negativo con datos de control de video aplicados |
| `latent` | LATENT | Tensor latente vacío listo para la generación de video |
| `trim_latent` | INT | Número de fotogramas latentes a recortar cuando se utiliza una imagen de referencia |

---
**Source fingerprint (SHA-256):** `66e50a360dc99ac49cac8f3f1c8649bf4298da2934c1bd9a0bc7cfbec620b291`
