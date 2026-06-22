# NormalizeVideoLatentStart

Esta documentación fue generada por IA. Si encuentras algún error o tienes sugerencias de mejora, ¡no dudes en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeVideoLatentStart/en.md)

Este nodo ajusta los primeros fotogramas de un latente de video para que se asemejen más a los fotogramas posteriores. Calcula el promedio y la variación a partir de un conjunto de fotogramas de referencia ubicados más adelante en el video, y aplica esas mismas características a los fotogramas iniciales. Esto ayuda a crear una transición visual más suave y consistente al comienzo de un video.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `latent` | La representación latente del video a procesar. | LATENT | Sí | - |
| `start_frame_count` | Número de fotogramas latentes a normalizar, contados desde el inicio (predeterminado: 4). | INT | Sí | 1 a 16384 |
| `reference_frame_count` | Número de fotogramas latentes después de los fotogramas iniciales para usar como referencia (predeterminado: 5). | INT | Sí | 1 a 16384 |

**Nota:** El `reference_frame_count` se limita automáticamente al número de fotogramas disponibles después de los fotogramas iniciales. Si el latente de video tiene solo 1 fotograma de longitud, no se realiza ninguna normalización y se devuelve el latente original sin cambios.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `latent` | El latente de video procesado con los fotogramas iniciales normalizados. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeVideoLatentStart/es.md)

---
**Source fingerprint (SHA-256):** `64844f3bf1735952334dcca3a829e8f666fd89e817ab66cf3c2dc04ecbbdff56`
