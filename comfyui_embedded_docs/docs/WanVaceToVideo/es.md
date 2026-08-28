# WanVaceToVideo

El nodo WanVaceToVideo prepara datos de acondicionamiento de video para modelos de generación de video. Toma entradas de acondicionamiento positivo y negativo junto con un video de control opcional, máscaras e imagen de referencia, y las codifica en representaciones latentes que guían la generación de video. El nodo maneja el escalado, el relleno, el enmascaramiento y la codificación VAE para construir la estructura de acondicionamiento adecuada para modelos de video.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `positivo` | Entrada de acondicionamiento positivo para guiar la generación | CONDITIONING | Sí | - |
| `negativo` | Entrada de acondicionamiento negativo para guiar la generación | CONDITIONING | Sí | - |
| `vae` | Modelo VAE utilizado para codificar imágenes y fotogramas de video | VAE | Sí | - |
| `ancho` | Ancho del video de salida en píxeles (predeterminado: 832, paso: 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `alto` | Alto del video de salida en píxeles (predeterminado: 480, paso: 16) | INT | Sí | 16 a MAX_RESOLUTION |
| `longitud` | Número de fotogramas en el video (predeterminado: 81, paso: 4) | INT | Sí | 1 a MAX_RESOLUTION |
| `tamaño_lote` | Número de videos a generar simultáneamente (predeterminado: 1) | INT | Sí | 1 a 4096 |
| `fuerza` | Fuerza de acondicionamiento para el control VACE (predeterminado: 1.0, paso: 0.01). Esto no es una fuerza LoRA. Los pesos LoRA se aplican mediante nodos LoRA separados. | FLOAT | Sí | 0.0 a 1000.0 |
| `control_video` | Video de entrada opcional utilizado para el acondicionamiento de control. Si no se proporciona, se crea automáticamente un video gris neutro. | IMAGE | No | - |
| `máscaras_de_control` | Máscaras opcionales que determinan qué partes del video de control están activas. Si no se proporcionan, se utiliza una máscara completamente blanca. | MASK | No | - |
| `imagen_de_referencia` | Imagen de referencia opcional para acondicionamiento adicional. Cuando se proporciona, se codifica y se antepone a la secuencia latente. | IMAGE | No | - |

**Nota:** Cuando se proporciona `control_video`, se trunca a `length` fotogramas y se escala a las `width` y `height` especificadas; si tiene menos fotogramas que `length`, los fotogramas faltantes se rellenan con gris neutro (valor 0.5). Cuando no se proporciona, se crea automáticamente un video gris neutro de `length` fotogramas. `control_masks` se escalan a las `width` y `height` especificadas, se truncan a `length` fotogramas y se rellenan con valor 1.0 si son más cortas. La máscara separa el video de control en partes inactivas y reactivas, cada una codificada con VAE y concatenada a lo largo de la dimensión de canales; la máscara también se reduce a resolución latente. Cuando se proporciona `reference_image`, se codifica con VAE y se antepone a la secuencia latente. El número de fotogramas latentes se calcula como `((length - 1) // 4) + 1`, y las dimensiones espaciales latentes son `height / 8` y `width / 8`.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `positivo` | Acondicionamiento positivo con datos de control de video (vace_frames, vace_mask, vace_strength) aplicados | CONDITIONING |
| `negativo` | Acondicionamiento negativo con datos de control de video (vace_frames, vace_mask, vace_strength) aplicados | CONDITIONING |
| `latente` | Tensor latente vacío listo para la generación de video con forma [batch_size, 16, latent_length, height/8, width/8] | LATENT |
| `latente_recortado` | Número de fotogramas latentes a recortar cuando se utiliza una imagen de referencia; 0 si no se proporciona ninguna imagen de referencia | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanVaceToVideo/es.md)

---
**Source fingerprint (SHA-256):** `2039b7509ce5b731e9e41d9cd2dad022d4c5004751f571a4cf88c1ba0cae405b`
