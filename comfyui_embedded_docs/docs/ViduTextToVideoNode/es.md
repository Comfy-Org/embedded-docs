> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduTextToVideoNode/es.md)

El nodo Vidu Text To Video Generation crea videos a partir de descripciones de texto. Utiliza varios modelos de generación de video para transformar sus indicaciones de texto en contenido de video con configuraciones personalizables para duración, relación de aspecto y estilo visual.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sí | `vidu_q1`<br>*Otras opciones de VideoModelName* | Nombre del modelo (por defecto: vidu_q1) |
| `prompt` | STRING | Sí | - | Una descripción textual para la generación de video |
| `duration` | INT | No | 5-5 | Duración del video de salida en segundos (por defecto: 5) |
| `seed` | INT | No | 0-2147483647 | Semilla para la generación de video (0 para aleatorio) (por defecto: 0) |
| `aspect_ratio` | COMBO | No | `r_16_9`<br>*Otras opciones de AspectRatio* | La relación de aspecto del video de salida (por defecto: r_16_9) |
| `resolution` | COMBO | No | `r_1080p`<br>*Otras opciones de Resolution* | Los valores admitidos pueden variar según el modelo y la duración (por defecto: r_1080p) |
| `movement_amplitude` | COMBO | No | `auto`<br>*Otras opciones de MovementAmplitude* | La amplitud de movimiento de los objetos en el cuadro (por defecto: auto) |

**Nota:** El campo `prompt` es obligatorio y no puede estar vacío. El parámetro `duration` está actualmente fijado en 5 segundos.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El video generado basado en la indicación de texto |