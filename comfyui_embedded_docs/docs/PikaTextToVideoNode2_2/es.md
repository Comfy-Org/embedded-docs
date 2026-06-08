El nodo Pika Text2Video v2.2 envía un mensaje de texto a la API de Pika versión 2.2 para generar un video. Convierte tu descripción textual en un video utilizando el servicio de generación de video con IA de Pika. El nodo permite personalizar varios aspectos del proceso de generación de video, incluyendo la relación de aspecto, la duración y la resolución.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `prompt_text` | La descripción textual principal que describe lo que deseas generar en el video | STRING | Sí | - |
| `negative_prompt` | Texto que describe lo que no deseas que aparezca en el video generado | STRING | Sí | - |
| `seed` | Número que controla la aleatoriedad de la generación para obtener resultados reproducibles | INT | Sí | - |
| `resolution` | La configuración de resolución para el video de salida | STRING | Sí | - |
| `duration` | La duración del video en segundos | INT | Sí | - |
| `aspect_ratio` | Relación de aspecto (ancho / alto) (predeterminado: 1.7777777777777777) | FLOAT | No | 0.4 - 2.5 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | El archivo de video generado devuelto por la API de Pika | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaTextToVideoNode2_2/es.md)

---
**Source fingerprint (SHA-256):** `b4287519f5d4cc4a1077a58fb13aa99697e3be038a0b382c4b4c9b0e53a0d8a8`
