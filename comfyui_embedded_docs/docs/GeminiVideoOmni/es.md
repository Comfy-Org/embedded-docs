# Google Gemini Omni (Video)

Genera un video con audio a partir de un prompt de texto utilizando el modelo Gemini Omni Flash de Google. Opcionalmente, proporciona imágenes y/o videos de referencia para guiar o editar el resultado. Describe la duración deseada (3-10s) y la relación de aspecto (16:9 o 9:16) directamente en el prompt.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `model` | El modelo de video Gemini utilizado para generar el video. | COMBO | Sí | "Omni Flash" |
| `seed` | La semilla controla si el nodo debe volver a ejecutarse; los resultados no son deterministas independientemente de la semilla (por defecto: 42). | INT | Sí | 0 a 2147483647 |
| `prompt` | El prompt de texto que describe el video a generar. Debe contener al menos un carácter que no sea espacio en blanco después de eliminar los espacios iniciales y finales. | STRING | Sí | Mínimo 1 carácter después de eliminar espacios |
| `images` | Imágenes de referencia opcionales para guiar la generación del video. Máximo de 14 imágenes en total. | IMAGE | No | Múltiples imágenes permitidas (máx. 14) |
| `videos` | Videos de referencia opcionales para guiar o editar la generación del video. Máximo de 3 videos, cada uno de hasta 10 segundos. | VIDEO | No | Múltiples videos permitidos (máx. 3, cada uno máx. 10s) |
| `temperature` | Controla la aleatoriedad en la generación (por defecto: 1.0). | FLOAT | No | 0.0 a 2.0 |
| `top_p` | Parámetro de muestreo de núcleo (por defecto: 0.95). | FLOAT | No | 0.0 a 1.0 |

Notas:
- Si una entrada de imagen contiene varios fotogramas, cada fotograma cuenta para el máximo de 14 imágenes.
- Cuando se proporcionan `images` o `videos`, el tamaño combinado de los medios codificados debe mantenerse por debajo de aproximadamente 90 MB; de lo contrario, el nodo genera un error.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `VIDEO` | El video generado con audio del modelo Gemini. | VIDEO |
| `STRING` | Cualquier respuesta de texto del modelo, como razonamiento o explicaciones. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiVideoOmni/es.md)

---
**Source fingerprint (SHA-256):** `1b7ca51d07cfb6a166cfed2a7e7174fd62f3290abcc1bdfdce94369dda242d3f`
