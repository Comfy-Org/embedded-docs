# Google Gemini Omni (Video)

Genera un video con audio a partir de un mensaje de texto utilizando el modelo Gemini Omni Flash de Google. Opcionalmente, proporciona imágenes y/o videos de referencia para guiar o editar el resultado. Describe la duración deseada (3-10 s) y la relación de aspecto (16:9 o 9:16) directamente en el mensaje.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `model` | El modelo de video Gemini utilizado para generar el video. | MODEL | Sí | "Omni Flash" |
| `seed` | La semilla controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente de la semilla (predeterminado: 42). | INT | Sí | 0 a 2147483647 |
| `prompt` | El mensaje de texto que describe el video a generar. Debe contener al menos un carácter que no sea espacio en blanco después de eliminar espacios iniciales y finales. | STRING | Sí | Mínimo 1 carácter después de eliminar espacios |
| `images` | Imágenes de referencia opcionales para guiar la generación del video. Máximo de 14 imágenes en total. | IMAGE | No | Múltiples imágenes permitidas (máx. 14) |
| `videos` | Videos de referencia opcionales para guiar o editar la generación del video. Máximo de 3 videos, cada uno de hasta 10 segundos. | VIDEO | No | Múltiples videos permitidos (máx. 3, cada uno máx. 10 s) |
| `temperature` | Controla la aleatoriedad en la generación (predeterminado: 1.0). | FLOAT | No | 0.0 a 2.0 |
| `top_p` | Parámetro de muestreo de núcleo (predeterminado: 0.95). | FLOAT | No | 0.0 a 1.0 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `VIDEO` | El video generado con audio proveniente del modelo Gemini. | VIDEO |
| `STRING` | Cualquier respuesta de texto del modelo, como razonamientos o explicaciones. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiVideoOmni/es.md)

---
**Source fingerprint (SHA-256):** `046842b7ec736283bba355aaa038b02fcf2416020f5f7aee7b0150d2a05bcbe6`
