# LTXVConcatAVLatent

El nodo LTXVConcatAVLatent combina una representación latente de video y una representación latente de audio en una única salida latente concatenada. Fusiona los tensores `samples` de ambas entradas y, si están presentes, también sus tensores `noise_mask`, preparándolos para su procesamiento posterior en un pipeline de generación de video.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `video_latent` | La representación latente de los datos de video. | LATENT | Sí |  |
| `audio_latent` | La representación latente de los datos de audio. | LATENT | Sí |  |

**Nota:** Los tensores `samples` de las entradas `video_latent` y `audio_latent` se concatenan. Si alguna de las entradas contiene un `noise_mask`, se utilizará; si falta alguna, se crea una máscara de unos (con la misma forma que los `samples` correspondientes) para dicha entrada. Las máscaras resultantes también se concatenan.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `latent` | Un diccionario latente único que contiene los `samples` concatenados y, si corresponde, el `noise_mask` concatenado de las entradas de video y audio. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConcatAVLatent/es.md)

---
**Source fingerprint (SHA-256):** `322d6870f110fb1ef8b472cb49649cc9fff7865f4c7a83fbfd536f1fdfd694f8`
