> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTextToVideoApi/es.md)

El nodo Wan Text to Video genera contenido de video basado en descripciones de texto. Utiliza modelos de IA para crear videos a partir de prompts y admite varios tamaños de video, duraciones y entradas de audio opcionales. El nodo puede generar audio automáticamente cuando es necesario y proporciona opciones para mejora de prompts y marca de agua.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sí | "wan2.5-t2v-preview" | Modelo a utilizar (por defecto: "wan2.5-t2v-preview") |
| `prompt` | STRING | Sí | - | Prompt utilizado para describir los elementos y características visuales, admite inglés/chino (por defecto: "") |
| `negative_prompt` | STRING | No | - | Prompt de texto negativo para guiar qué evitar (por defecto: "") |
| `size` | COMBO | No | "480p: 1:1 (624x624)"<br>"480p: 16:9 (832x480)"<br>"480p: 9:16 (480x832)"<br>"720p: 1:1 (960x960)"<br>"720p: 16:9 (1280x720)"<br>"720p: 9:16 (720x1280)"<br>"720p: 4:3 (1088x832)"<br>"720p: 3:4 (832x1088)"<br>"1080p: 1:1 (1440x1440)"<br>"1080p: 16:9 (1920x1080)"<br>"1080p: 9:16 (1080x1920)"<br>"1080p: 4:3 (1632x1248)"<br>"1080p: 3:4 (1248x1632)" | Resolución y relación de aspecto del video (por defecto: "480p: 1:1 (624x624)") |
| `duration` | INT | No | 5-10 | Duraciones disponibles: 5 y 10 segundos (por defecto: 5) |
| `audio` | AUDIO | No | - | El audio debe contener una voz clara y fuerte, sin ruido extraño, música de fondo |
| `seed` | INT | No | 0-2147483647 | Semilla a utilizar para la generación (por defecto: 0) |
| `generate_audio` | BOOLEAN | No | - | Si no hay entrada de audio, generar audio automáticamente (por defecto: False) |
| `prompt_extend` | BOOLEAN | No | - | Si mejorar el prompt con asistencia de IA (por defecto: True) |
| `watermark` | BOOLEAN | No | - | Si agregar una marca de agua "AI generated" al resultado (por defecto: True) |

**Nota:** El parámetro `duration` solo acepta valores de 5 o 10 segundos, ya que estas son las duraciones disponibles. Al proporcionar entrada de audio, debe tener una duración entre 3.0 y 29.0 segundos y contener voz clara sin ruido de fondo ni música.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El video generado basado en los parámetros de entrada |