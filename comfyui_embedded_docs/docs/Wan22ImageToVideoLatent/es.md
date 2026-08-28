# Wan22ImageToVideoLatent

Wan22ImageToVideoLatent crea representaciones latentes de video a partir de imágenes. Genera un espacio latente de video en blanco con el ancho, alto, longitud de fotogramas y tamaño de lote especificados, y opcionalmente puede codificar una secuencia de imagen inicial en los primeros fotogramas. Cuando se proporciona una imagen de inicio, el nodo la codifica en el espacio latente y crea una máscara de ruido correspondiente que indica qué regiones deben someterse a eliminación de ruido durante la generación.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `vae` | El modelo VAE utilizado para codificar la imagen de inicio en el espacio latente | VAE | Sí | - |
| `ancho` | El ancho del video de salida en píxeles (predeterminado: 1280, paso: 32) | INT | Sí | 32 a MAX_RESOLUTION |
| `alto` | El alto del video de salida en píxeles (predeterminado: 704, paso: 32) | INT | Sí | 32 a MAX_RESOLUTION |
| `duración` | El número de fotogramas en la secuencia de video (predeterminado: 49, paso: 4) | INT | Sí | 1 a MAX_RESOLUTION |
| `tamaño_lote` | El número de latentes de video a generar (predeterminado: 1) | INT | Sí | 1 a 4096 |
| `imagen_inicio` | Secuencia de imagen inicial opcional para codificar en los primeros fotogramas del latente de video (usa los primeros `length` fotogramas) | IMAGE | No | - |

**Nota:** Cuando se proporciona `start_image`, la secuencia de imagen se amplía a las dimensiones objetivo de `width` y `height`, se codifica con el VAE y se coloca en los primeros fotogramas del latente. La máscara de ruido para esos fotogramas se establece en 0 (preservados), mientras que los fotogramas restantes tienen un valor de máscara de 1 (para eliminar ruido). El latente siempre tiene 48 canales, dimensiones espaciales de `height / 16` por `width / 16`, y una dimensión temporal de `((length - 1) // 4) + 1`. `width` y `height` deben ser divisibles por 16 (garantizado por el paso de 32), y `length` aumenta la dimensión temporal en pasos de 4.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `samples` | La representación latente de video generada, repetida para cada elemento del lote | LATENT |
| `noise_mask` | La máscara de ruido que indica qué regiones deben someterse a eliminación de ruido (valor 1) y cuáles conservan la imagen de inicio codificada (valor 0) | LATENT |

Ambos campos se devuelven juntos dentro de una única salida LATENT.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22ImageToVideoLatent/es.md)

---
**Source fingerprint (SHA-256):** `3d05980641eeef2e86df7a845aa8b2bd703882db98fe71adef2746ab34a9d717`
