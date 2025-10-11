> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaTextToVideoNode2_2/es.md)

El nodo Pika Text2Video v2.2 envía un mensaje de texto a la API de Pika versión 2.2 para generar un video. Convierte tu descripción de texto en un video utilizando el servicio de generación de video con IA de Pika. El nodo te permite personalizar varios aspectos del proceso de generación de video, incluida la relación de aspecto, la duración y la resolución.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt_text` | STRING | Sí | - | La descripción de texto principal que describe lo que quieres generar en el video |
| `negative_prompt` | STRING | Sí | - | Texto que describe lo que no quieres que aparezca en el video generado |
| `seed` | INT | Sí | - | Un número que controla la aleatoriedad de la generación para resultados reproducibles |
| `resolution` | STRING | Sí | - | La configuración de resolución para el video de salida |
| `duration` | INT | Sí | - | La longitud del video en segundos |
| `aspect_ratio` | FLOAT | No | 0.4 - 2.5 | Relación de aspecto (ancho / alto) (por defecto: 1.7777777777777777) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El archivo de video generado devuelto por la API de Pika |