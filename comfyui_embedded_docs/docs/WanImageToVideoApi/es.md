> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideoApi/es.md)

El nodo Wan Image to Video genera contenido de video a partir de una única imagen de entrada y un texto descriptivo. Crea secuencias de video extendiendo el fotograma inicial de acuerdo con la descripción proporcionada, con opciones para controlar la calidad del video, la duración y la integración de audio.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sí | "wan2.5-i2v-preview"<br>"wan2.5-i2v-preview" | Modelo a utilizar (por defecto: "wan2.5-i2v-preview") |
| `image` | IMAGE | Sí | - | Imagen de entrada que sirve como primer fotograma para la generación de video |
| `prompt` | STRING | Sí | - | Texto descriptivo utilizado para describir los elementos y características visuales, admite inglés/chino (por defecto: vacío) |
| `negative_prompt` | STRING | No | - | Texto descriptivo negativo para guiar qué elementos evitar (por defecto: vacío) |
| `resolution` | COMBO | No | "480P"<br>"720P"<br>"1080P" | Calidad de resolución del video (por defecto: "480P") |
| `duration` | INT | No | 5-10 | Duraciones disponibles: 5 y 10 segundos (por defecto: 5) |
| `audio` | AUDIO | No | - | El audio debe contener una voz clara y alta, sin ruido extraño ni música de fondo |
| `seed` | INT | No | 0-2147483647 | Semilla a utilizar para la generación (por defecto: 0) |
| `generate_audio` | BOOLEAN | No | - | Si no hay entrada de audio, generar audio automáticamente (por defecto: False) |
| `prompt_extend` | BOOLEAN | No | - | Si se debe mejorar el texto descriptivo con asistencia de IA (por defecto: True) |
| `watermark` | BOOLEAN | No | - | Si se debe agregar una marca de agua "AI generated" al resultado (por defecto: True) |

**Restricciones:**
- Se requiere exactamente una imagen de entrada para la generación de video
- El parámetro de duración solo acepta valores de 5 o 10 segundos
- Cuando se proporciona audio, debe tener una duración entre 3.0 y 29.0 segundos

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | Video generado basado en la imagen de entrada y el texto descriptivo |