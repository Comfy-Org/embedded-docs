> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduStartEndToVideoNode/es.md)

El nodo Vidu Start End To Video Generation crea un video generando fotogramas entre un fotograma inicial y un fotograma final. Utiliza un mensaje de texto para guiar el proceso de generación de video y admite varios modelos de video con diferentes configuraciones de resolución y movimiento. El nodo valida que los fotogramas inicial y final tengan relaciones de aspecto compatibles antes del procesamiento.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sí | `"vidu_q1"`<br>[Otros valores de modelo del enum VideoModelName] | Nombre del modelo (por defecto: "vidu_q1") |
| `first_frame` | IMAGE | Sí | - | Fotograma inicial |
| `end_frame` | IMAGE | Sí | - | Fotograma final |
| `prompt` | STRING | No | - | Una descripción textual para la generación del video |
| `duration` | INT | No | 5-5 | Duración del video de salida en segundos (por defecto: 5, fijado en 5 segundos) |
| `seed` | INT | No | 0-2147483647 | Semilla para la generación del video (0 para aleatorio) (por defecto: 0) |
| `resolution` | COMBO | No | `"1080p"`<br>[Otros valores de resolución del enum Resolution] | Los valores admitidos pueden variar según el modelo y la duración (por defecto: "1080p") |
| `movement_amplitude` | COMBO | No | `"auto"`<br>[Otros valores de amplitud de movimiento del enum MovementAmplitude] | La amplitud de movimiento de los objetos en el fotograma (por defecto: "auto") |

**Nota:** Los fotogramas inicial y final deben tener relaciones de aspecto compatibles (validado con una tolerancia de relación min_rel=0.8, max_rel=1.25).

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El archivo de video generado |