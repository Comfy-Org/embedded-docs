> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaImageToVideoNode2_2/es.md)

El nodo Pika Image to Video envía una imagen y un texto de instrucción a la API de Pika versión 2.2 para generar un video. Convierte la imagen de entrada en formato de video según la descripción y la configuración proporcionadas. El nodo gestiona la comunicación con la API y devuelve el video generado como salida.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen que se convertirá en video |
| `prompt_text` | STRING | Sí | - | La descripción textual que guía la generación del video |
| `negative_prompt` | STRING | Sí | - | Texto que describe lo que se debe evitar en el video |
| `seed` | INT | Sí | - | Valor de semilla aleatoria para obtener resultados reproducibles |
| `resolution` | STRING | Sí | - | Configuración de resolución del video de salida |
| `duration` | INT | Sí | - | Duración del video generado en segundos |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | VIDEO | El archivo de video generado |

---
**Source fingerprint (SHA-256):** `aaa8dc49b94f0fae2010a3b61a3fb41e212fa9d2946a934a1a7c651fdced81b3`
