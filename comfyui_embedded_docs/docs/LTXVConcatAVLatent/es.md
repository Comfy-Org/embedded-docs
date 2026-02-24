> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConcatAVLatent/es.md)

El nodo LTXVConcatAVLatent combina una representación latente de video y una representación latente de audio en una única salida latente concatenada. Fusiona los tensores `samples` de ambas entradas y, si están presentes, también sus tensores `noise_mask`, preparándolos para su posterior procesamiento en un pipeline de generación de video.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `video_latent` | LATENT | Sí | | La representación latente de los datos de video. |
| `audio_latent` | LATENT | Sí | | La representación latente de los datos de audio. |

**Nota:** Los tensores `samples` de las entradas `video_latent` y `audio_latent` se concatenan. Si cualquiera de las entradas contiene un `noise_mask`, se utilizará; si falta uno, se crea una máscara de unos (con la misma forma que el `samples` correspondiente) para ella. Las máscaras resultantes también se concatenan.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `latent` | LATENT | Un único diccionario latente que contiene los `samples` concatenados y, si corresponde, el `noise_mask` concatenado de las entradas de video y audio. |
