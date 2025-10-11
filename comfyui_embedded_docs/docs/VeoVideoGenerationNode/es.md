> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeoVideoGenerationNode/es.md)

Genera videos a partir de prompts de texto utilizando la API Veo de Google. Este nodo puede crear videos a partir de descripciones de texto y entradas de imagen opcionales, con control sobre parámetros como la relación de aspecto, duración y más.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | - | Descripción de texto del video (valor por defecto: vacío) |
| `aspect_ratio` | COMBO | Sí | "16:9"<br>"9:16" | Relación de aspecto del video de salida (valor por defecto: "16:9") |
| `negative_prompt` | STRING | No | - | Prompt de texto negativo para guiar lo que se debe evitar en el video (valor por defecto: vacío) |
| `duration_seconds` | INT | No | 5-8 | Duración del video de salida en segundos (valor por defecto: 5) |
| `enhance_prompt` | BOOLEAN | No | - | Si se debe mejorar el prompt con asistencia de IA (valor por defecto: True) |
| `person_generation` | COMBO | No | "ALLOW"<br>"BLOCK" | Si se permite generar personas en el video (valor por defecto: "ALLOW") |
| `seed` | INT | No | 0-4294967295 | Semilla para la generación de video (0 para aleatorio) (valor por defecto: 0) |
| `image` | IMAGE | No | - | Imagen de referencia opcional para guiar la generación del video |
| `model` | COMBO | No | "veo-2.0-generate-001" | Modelo Veo 2 a utilizar para la generación de video (valor por defecto: "veo-2.0-generate-001") |

**Nota:** El parámetro `generate_audio` solo está disponible para modelos Veo 3.0 y es manejado automáticamente por el nodo según el modelo seleccionado.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El archivo de video generado |