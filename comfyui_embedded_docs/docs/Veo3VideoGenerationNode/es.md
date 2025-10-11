> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Veo3VideoGenerationNode/es.md)

Genera videos a partir de descripciones de texto utilizando la API de Google Veo 3. Este nodo admite dos modelos de Veo 3: veo-3.0-generate-001 y veo-3.0-fast-generate-001. Extiende el nodo base de Veo con funciones específicas de Veo 3, incluida la generación de audio y una duración fija de 8 segundos.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | - | Descripción de texto del video (valor por defecto: "") |
| `aspect_ratio` | COMBO | Sí | "16:9"<br>"9:16" | Relación de aspecto del video de salida (valor por defecto: "16:9") |
| `negative_prompt` | STRING | No | - | Descripción de texto negativa para guiar lo que se debe evitar en el video (valor por defecto: "") |
| `duration_seconds` | INT | No | 8-8 | Duración del video de salida en segundos (Veo 3 solo admite 8 segundos) (valor por defecto: 8) |
| `enhance_prompt` | BOOLEAN | No | - | Si se debe mejorar la descripción con asistencia de IA (valor por defecto: True) |
| `person_generation` | COMBO | No | "ALLOW"<br>"BLOCK" | Si se permite generar personas en el video (valor por defecto: "ALLOW") |
| `seed` | INT | No | 0-4294967295 | Semilla para la generación del video (0 para aleatorio) (valor por defecto: 0) |
| `image` | IMAGE | No | - | Imagen de referencia opcional para guiar la generación del video |
| `model` | COMBO | No | "veo-3.0-generate-001"<br>"veo-3.0-fast-generate-001" | Modelo Veo 3 a utilizar para la generación del video (valor por defecto: "veo-3.0-generate-001") |
| `generate_audio` | BOOLEAN | No | - | Generar audio para el video. Compatible con todos los modelos Veo 3. (valor por defecto: False) |

**Nota:** El parámetro `duration_seconds` está fijado en 8 segundos para todos los modelos Veo 3 y no se puede cambiar.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El archivo de video generado |