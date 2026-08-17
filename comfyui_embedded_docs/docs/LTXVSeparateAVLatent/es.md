# Separar AV Latent

El nodo LTXVSeparateAVLatent toma una representación latente audiovisual combinada y la divide en dos latentes separados: uno para video y otro para audio. Funciona con cualquier modelo audiovisual, como LTXV o MiniMax H3.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `av_latent` | La representación latente audiovisual combinada que se va a separar. | LATENT | Sí | N/A |

**Nota:** Se espera que el tensor `samples` del latente de entrada tenga al menos dos elementos a lo largo de la primera dimensión (dimensión de lote). El primer elemento se usa para el latente de video y el segundo para el latente de audio. Si `noise_mask` está presente, se divide de la misma manera.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `video_latent` | La representación latente que contiene los datos de video separados. | LATENT |
| `audio_latent` | La representación latente que contiene los datos de audio separados. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSeparateAVLatent/es.md)

---
**Source fingerprint (SHA-256):** `22ed38bbc1b5716cee380c35c50455810f79c273f51bbe6a535c9ae33192afe6`
