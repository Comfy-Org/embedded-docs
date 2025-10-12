> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentAudio/es.md)

El nodo EmptyLatentAudio crea tensores latentes vacíos para procesamiento de audio. Genera una representación latente de audio en blanco con duración y tamaño de lote especificados, que puede utilizarse como entrada para flujos de trabajo de generación o procesamiento de audio. El nodo calcula las dimensiones latentes apropiadas basándose en la duración del audio y la frecuencia de muestreo.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `segundos` | FLOAT | Sí | 1.0 - 1000.0 | La duración del audio en segundos (valor por defecto: 47.6) |
| `tamaño_del_lote` | INT | Sí | 1 - 4096 | El número de imágenes latentes en el lote (valor por defecto: 1) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `LATENT` | LATENT | Devuelve un tensor latente vacío para procesamiento de audio con duración y tamaño de lote especificados |