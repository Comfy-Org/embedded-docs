El nodo Wan22ImageToVideoLatent crea representaciones latentes de video a partir de imágenes. Genera un espacio latente de video en blanco con dimensiones específicas y puede codificar opcionalmente una secuencia de imágenes inicial en los primeros fotogramas. Cuando se proporciona una imagen de inicio, codifica la imagen en el espacio latente y crea una máscara de ruido correspondiente para las regiones editadas.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `vae` | El modelo VAE utilizado para codificar imágenes en el espacio latente | VAE | Sí | - |
| `ancho` | El ancho del video de salida en píxeles (predeterminado: 1280, paso: 32) | INT | Sí | 32 a MAX_RESOLUTION |
| `alto` | La altura del video de salida en píxeles (predeterminado: 704, paso: 32) | INT | Sí | 32 a MAX_RESOLUTION |
| `duración` | El número de fotogramas en la secuencia de video (predeterminado: 49, paso: 4) | INT | Sí | 1 a MAX_RESOLUTION |
| `tamaño_lote` | El número de lotes a generar (predeterminado: 1) | INT | Sí | 1 a 4096 |
| `imagen_inicio` | Secuencia de imágenes inicial opcional para codificar en el video latente | IMAGE | No | - |

**Nota:** Cuando se proporciona `start_image`, el nodo codifica la secuencia de imágenes en los primeros fotogramas del espacio latente y genera una máscara de ruido correspondiente. Los parámetros de ancho y alto deben ser divisibles entre 16 para obtener dimensiones de espacio latente adecuadas. El parámetro `length` determina el número de fotogramas en el video latente; la dimensión temporal del espacio latente se calcula como `((length - 1) // 4) + 1`.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `samples` | La representación latente de video generada | LATENT |
| `noise_mask` | La máscara de ruido que indica qué regiones deben ser eliminadas de ruido durante la generación | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22ImageToVideoLatent/es.md)

---
**Source fingerprint (SHA-256):** `0f27e20bcc63f0dd224cda0fa26ee676c42898ac74fcfbe0a2b591def933689c`
