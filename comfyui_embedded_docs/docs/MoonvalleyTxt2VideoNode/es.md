> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoonvalleyTxt2VideoNode/es.md)

El nodo Moonvalley Marey Text to Video genera contenido de vídeo a partir de descripciones de texto utilizando la API de Moonvalley. Toma un texto de entrada y lo convierte en un vídeo con configuraciones personalizables para resolución, calidad y estilo. El nodo maneja todo el proceso, desde enviar la solicitud de generación hasta descargar el vídeo final.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | - | Descripción textual del contenido de vídeo a generar |
| `negative_prompt` | STRING | No | - | Texto del prompt negativo (valor por defecto: lista extensa de elementos excluidos como contenido sintético, corte de escena, artefactos, ruido, etc.) |
| `resolution` | STRING | No | "16:9 (1920 x 1080)"<br>"9:16 (1080 x 1920)"<br>"1:1 (1152 x 1152)"<br>"4:3 (1536 x 1152)"<br>"3:4 (1152 x 1536)"<br>"21:9 (2560 x 1080)" | Resolución del vídeo de salida (valor por defecto: "16:9 (1920 x 1080)") |
| `prompt_adherence` | FLOAT | No | 1.0-20.0 | Escala de guía para el control de la generación (valor por defecto: 4.0) |
| `seed` | INT | No | 0-4294967295 | Valor de semilla aleatoria (valor por defecto: 9) |
| `steps` | INT | No | 1-100 | Pasos de inferencia (valor por defecto: 33) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `video` | VIDEO | La salida de vídeo generada basada en el texto de entrada |