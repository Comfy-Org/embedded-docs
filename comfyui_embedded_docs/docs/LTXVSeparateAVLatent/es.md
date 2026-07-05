# LTXVSeparateAVLatent

El nodo LTXVSeparateAVLatent toma una representación latente audiovisual combinada y la divide en dos partes distintas: una para video y otra para audio. Separa las muestras y, si están presentes, las máscaras de ruido del latente de entrada, creando dos nuevos objetos latentes.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `av_latente` | La representación latente audiovisual combinada que se va a separar. | LATENT | Sí | N/A |

**Nota:** Se espera que el tensor `samples` del latente de entrada tenga al menos dos elementos a lo largo de la primera dimensión (dimensión de lote). El primer elemento se utiliza para el latente de video y el segundo elemento para el latente de audio. Si hay una `noise_mask` presente, se divide de la misma manera.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `latente_audio` | La representación latente que contiene los datos de video separados. | LATENT |
| `audio_latent` | La representación latente que contiene los datos de audio separados. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSeparateAVLatent/es.md)

---
**Source fingerprint (SHA-256):** `55bce5d768e7fe13f885cc32d34ecdac5cdcbb667b03743004866ea4b6d58d46`
