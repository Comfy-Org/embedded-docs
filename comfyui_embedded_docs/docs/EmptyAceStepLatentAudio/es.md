> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStepLatentAudio/es.md)

El nodo EmptyAceStepLatentAudio crea muestras latentes de audio vacías de una duración específica. Genera un lote de latentes de audio silenciosos con ceros, donde la longitud se calcula en base a los segundos de entrada y los parámetros de procesamiento de audio. Este nodo es útil para inicializar flujos de trabajo de procesamiento de audio que requieren representaciones latentes.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `seconds` | FLOAT | No | 1.0 - 1000.0 | La duración del audio en segundos (valor por defecto: 120.0) |
| `batch_size` | INT | No | 1 - 4096 | El número de imágenes latentes en el lote (valor por defecto: 1) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | LATENT | Devuelve muestras latentes de audio vacías con ceros |
