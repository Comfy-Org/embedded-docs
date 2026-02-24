> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSeparateAVLatent/es.md)

El nodo LTXVSeparateAVLatent toma una representación latente audiovisual combinada y la divide en dos partes distintas: una para video y otra para audio. Separa las muestras y, si está presente, las máscaras de ruido del latente de entrada, creando dos nuevos objetos latentes.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `av_latent` | LATENT | Sí | N/A | La representación latente audiovisual combinada que se va a separar. |

**Nota:** Se espera que el tensor `samples` del latente de entrada tenga al menos dos elementos a lo largo de la primera dimensión (dimensión de lote). El primer elemento se utiliza para el latente de video y el segundo para el latente de audio. Si hay una `noise_mask` presente, se divide de la misma manera.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `video_latent` | LATENT | La representación latente que contiene los datos de video separados. |
| `audio_latent` | LATENT | La representación latente que contiene los datos de audio separados. |
