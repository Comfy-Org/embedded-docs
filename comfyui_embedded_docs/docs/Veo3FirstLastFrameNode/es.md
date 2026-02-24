> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Veo3FirstLastFrameNode/es.md)

El nodo Veo3FirstLastFrameNode utiliza el modelo Veo 3 de Google para generar un vídeo. Crea un vídeo basado en un texto descriptivo, utilizando una primera y última imagen proporcionadas para guiar el inicio y el final de la secuencia.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | N/A | Descripción textual del vídeo (valor por defecto: cadena vacía). |
| `negative_prompt` | STRING | No | N/A | Texto negativo para guiar qué evitar en el vídeo (valor por defecto: cadena vacía). |
| `resolution` | COMBO | Sí | `"720p"`<br>`"1080p"` | La resolución del vídeo de salida. |
| `aspect_ratio` | COMBO | No | `"16:9"`<br>`"9:16"` | Relación de aspecto del vídeo de salida (valor por defecto: "16:9"). |
| `duration` | INT | No | 4 a 8 | Duración del vídeo de salida en segundos (valor por defecto: 8). |
| `seed` | INT | No | 0 a 4294967295 | Semilla para la generación del vídeo (valor por defecto: 0). |
| `first_frame` | IMAGE | Sí | N/A | La imagen de inicio para el vídeo. |
| `last_frame` | IMAGE | Sí | N/A | La imagen final para el vídeo. |
| `model` | COMBO | No | `"veo-3.1-generate"`<br>`"veo-3.1-fast-generate"` | El modelo específico de Veo 3 a utilizar para la generación (valor por defecto: "veo-3.1-fast-generate"). |
| `generate_audio` | BOOLEAN | No | N/A | Generar audio para el vídeo (valor por defecto: True). |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El archivo de vídeo generado. |
