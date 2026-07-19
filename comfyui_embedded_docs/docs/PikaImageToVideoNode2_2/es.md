# PikaImageToVideoNode2_2

El nodo Pika Image to Video envía una imagen y un texto de instrucción a la API de Pika versión 2.2 para generar un video. Convierte la imagen de entrada en formato de video según la descripción y la configuración proporcionadas. El nodo gestiona la comunicación con la API y devuelve el video generado como salida.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `image` | La imagen que se convertirá en video | IMAGE | Sí | - |
| `prompt_text` | La descripción textual que guía la generación del video | STRING | Sí | - |
| `negative_prompt` | Texto que describe lo que se debe evitar en el video | STRING | Sí | - |
| `seed` | Valor de semilla aleatoria para obtener resultados reproducibles | INT | Sí | - |
| `resolution` | Configuración de resolución del video de salida | STRING | Sí | - |
| `duration` | Duración del video generado en segundos | INT | Sí | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | El archivo de video generado | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaImageToVideoNode2_2/es.md)

---
**Source fingerprint (SHA-256):** `aaa8dc49b94f0fae2010a3b61a3fb41e212fa9d2946a934a1a7c651fdced81b3`
