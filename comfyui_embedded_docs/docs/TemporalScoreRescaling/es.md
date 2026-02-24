> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TemporalScoreRescaling/es.md)

Este nodo aplica el Reajuste Temporal de Puntuación (TSR) a un modelo de difusión. Modifica el comportamiento de muestreo del modelo reajustando el ruido o la puntuación predicha durante el proceso de eliminación de ruido, lo que puede dirigir la diversidad de la salida generada. Esto se implementa como una función posterior a la Guía Libre de Clasificador (CFG).

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo de difusión que se va a parchear con la función TSR. |
| `tsr_k` | FLOAT | No | 0.01 - 100.0 | Controla la intensidad del reajuste. Un k más bajo produce resultados más detallados; un k más alto produce resultados más suaves en la generación de imágenes. Establecer k = 1 desactiva el reajuste. (por defecto: 0.95) |
| `tsr_sigma` | FLOAT | No | 0.01 - 100.0 | Controla qué tan temprano entra en efecto el reajuste. Valores más grandes entran en efecto antes. (por defecto: 1.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `patched_model` | MODEL | El modelo de entrada, ahora parcheado con la función de Reajuste Temporal de Puntuación aplicada a su proceso de muestreo. |
