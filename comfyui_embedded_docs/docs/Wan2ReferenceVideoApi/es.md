> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ReferenceVideoApi/es.md)

Este nodo genera un video que presenta a una persona u objeto basándose en materiales de referencia proporcionados. Utiliza el modelo Wan 2.7 para crear videos a partir de un texto descriptivo, admitiendo actuaciones de un solo personaje e interacciones de múltiples personajes. Debes proporcionar al menos un video o imagen de referencia para que la generación funcione.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sí | `"wan2.7-r2v"` | El modelo específico a utilizar para la generación del video. |
| `model.prompt` | STRING | Sí | - | Texto descriptivo que define el video. Utiliza identificadores como 'character1' y 'character2' para referirse a los personajes de referencia. |
| `model.negative_prompt` | STRING | No | - | Texto descriptivo negativo que indica qué se debe evitar en el video generado (por defecto: vacío). |
| `model.resolution` | COMBO | Sí | `"720P"`<br>`"1080P"` | La resolución del video de salida. |
| `model.ratio` | COMBO | Sí | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` | La relación de aspecto del video de salida. |
| `model.duration` | INT | Sí | 2 a 10 | La duración del video generado en segundos (por defecto: 5). |
| `model.reference_videos` | VIDEO | No | - | Una lista de videos de referencia. Puedes añadir hasta 3 videos. |
| `model.reference_images` | IMAGE | No | - | Una lista de imágenes de referencia. Puedes añadir hasta 5 imágenes. |
| `seed` | INT | No | 0 a 2147483647 | Semilla para usar en la generación, que ayuda a controlar la aleatoriedad de la salida (por defecto: 0). |
| `watermark` | BOOLEAN | No | - | Indica si se debe añadir una marca de agua generada por IA al resultado (por defecto: Falso). Esta es una configuración avanzada. |

**Restricciones importantes:**
*   Debes proporcionar al menos un video de referencia o una imagen de referencia en las entradas `model.reference_videos` o `model.reference_images`.
*   El número total combinado de videos e imágenes de referencia no puede exceder 5.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El archivo de video generado. |