# NormalizeVideoLatentStart

Este nodo ajusta los primeros fotogramas de un latente de video para que se parezcan más a los fotogramas posteriores. Calcula el promedio y la variación de un conjunto de fotogramas de referencia posteriores en el video y aplica esas mismas características a los fotogramas iniciales. Esto ayuda a crear una transición visual más suave y consistente al comienzo de un video.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `latent` | La representación latente del video a procesar. | LATENT | Sí | - |
| `start_frame_count` | Número de fotogramas latentes a normalizar, contados desde el inicio (por defecto: 4). | INT | Sí | 1 a 16384 (resolución máxima) |
| `reference_frame_count` | Número de fotogramas latentes después de los fotogramas iniciales que se usan como referencia (por defecto: 5). | INT | Sí | 1 a 16384 (resolución máxima) |

**Nota:** El `reference_frame_count` se limita automáticamente al número de fotogramas disponibles después de los fotogramas iniciales. Si el latente de video tiene solo 1 fotograma de longitud, no se realiza ninguna normalización y se devuelve el latente original sin cambios.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `latent` | El latente de video procesado con los fotogramas iniciales normalizados. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeVideoLatentStart/es.md)

---
**Source fingerprint (SHA-256):** `383e5a19ee4cd8bdea5983567ddbdc30bb09c373142a1a934cea985f1b9d1b0d`
