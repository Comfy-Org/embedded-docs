# WanVaceToVideo

El nodo WanVaceToVideo procesa datos de condicionamiento de video para modelos de generación de video. Toma entradas de condicionamiento positivas y negativas junto con datos de control de video y prepara representaciones latentes para la generación de video. El nodo maneja el escalado de video, el enmascaramiento y la codificación VAE para crear la estructura de condicionamiento adecuada para modelos de video.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `positive` | Entrada de condicionamiento positiva para guiar la generación | CONDITIONING | Sí | - |
| `negative` | Entrada de condicionamiento negativa para guiar la generación | CONDITIONING | Sí | - |
| `vae` | Modelo VAE utilizado para codificar imágenes y fotogramas de video | VAE | Sí | - |
| `width` | Ancho del video de salida en píxeles (predeterminado: 832, paso: 16) | INT | Sí | 16 to MAX_RESOLUTION |
| `height` | Altura del video de salida en píxeles (predeterminado: 480, paso: 16) | INT | Sí | 16 to MAX_RESOLUTION |
| `length` | Número de fotogramas en el video (predeterminado: 81, paso: 4) | INT | Sí | 1 to MAX_RESOLUTION |
| `batch_size` | Número de videos a generar simultáneamente (predeterminado: 1) | INT | Sí | 1 to 4096 |
| `strength` | Fuerza de condicionamiento para el control VACE (predeterminado: 1.0, paso: 0.01). Esto no es una fuerza LoRA. Los pesos LoRA se aplican a través de nodos LoRA separados. | FLOAT | Sí | 0.0 to 1000.0 |
| `control_video` | Video de entrada opcional para el condicionamiento de control. Si no se proporciona, se crea automáticamente un video gris neutro. Cuando se proporciona, se escala a `width` × `height` y se limita a los primeros `length` fotogramas; si tiene menos fotogramas, los fotogramas faltantes se rellenan con gris neutro. | IMAGE | No | - |
| `control_masks` | Máscaras opcionales para controlar qué partes del video modificar. Si no se proporcionan, se utiliza una máscara completamente blanca. Cuando se proporcionan, las máscaras se escalan a `width` × `height`, se limitan a `length` fotogramas y se rellenan con blanco si tienen menos fotogramas. | MASK | No | - |
| `reference_image` | Imagen de referencia opcional para condicionamiento adicional. Cuando se proporciona, se escala a `width` × `height`, se codifica con el VAE y se antepone a la secuencia latente. | IMAGE | No | - |

**Nota:** Cuando se proporciona `control_video`, se escala a los valores especificados de `width` y `height`. Si se proporcionan `control_masks`, se escalan para que coincidan con las mismas dimensiones. Cuando se proporciona `reference_image`, se codifica a través del VAE y se antepone a la secuencia latente. El parámetro `length` determina el número de fotogramas, y la longitud latente se calcula como `((length - 1) // 4) + 1`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `positive` | Condicionamiento positivo con datos de control de video aplicados (vace_frames, vace_mask, vace_strength) | CONDITIONING |
| `negative` | Condicionamiento negativo con datos de control de video aplicados (vace_frames, vace_mask, vace_strength) | CONDITIONING |
| `latent` | Tensor latente vacío listo para la generación de video con forma [batch_size, 16, latent_length, height/8, width/8] | LATENT |
| `trim_latent` | Número de fotogramas latentes a recortar cuando se utiliza una imagen de referencia (0 si no se proporciona imagen de referencia) | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanVaceToVideo/es.md)

---
**Source fingerprint (SHA-256):** `2039b7509ce5b731e9e41d9cd2dad022d4c5004751f571a4cf88c1ba0cae405b`
