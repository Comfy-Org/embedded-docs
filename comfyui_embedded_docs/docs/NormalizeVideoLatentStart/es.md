> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/NormalizeVideoLatentStart/es.md)

Este nodo ajusta los primeros fotogramas de un latente de video para que se asemejen más a los fotogramas posteriores. Calcula el promedio y la variación de un conjunto de fotogramas de referencia ubicados más adelante en el video y aplica esas mismas características a los fotogramas iniciales. Esto ayuda a crear una transición visual más suave y consistente al comienzo de un video.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `latent` | LATENT | Sí | - | La representación latente de video a procesar. |
| `start_frame_count` | INT | No | 1 a 16384 | Número de fotogramas latentes a normalizar, contando desde el inicio (por defecto: 4). |
| `reference_frame_count` | INT | No | 1 a 16384 | Número de fotogramas latentes posteriores a los iniciales que se usarán como referencia (por defecto: 5). |

**Nota:** El valor de `reference_frame_count` se limita automáticamente al número de fotogramas disponibles después de los fotogramas iniciales. Si el latente de video tiene solo 1 fotograma, no se realiza ninguna normalización y se devuelve el latente original sin cambios.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `latent` | LATENT | El latente de video procesado, con los fotogramas iniciales normalizados. |
