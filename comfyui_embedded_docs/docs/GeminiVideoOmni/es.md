# Google Gemini Omni (Video)

Este nodo genera un video con audio a partir de una instrucción de texto utilizando el modelo Google Gemini Omni Flash. Opcionalmente, puedes proporcionar imágenes o videos de referencia para guiar o editar el resultado.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `model` | El modelo de video Gemini utilizado para generar el video. | COMBO | Sí | `"Omni Flash"` |
| `seed` | La semilla controla si el nodo debe reejecutarse; los resultados no son deterministas independientemente de la semilla. (predeterminado: 42) | INT | Sí | 0 a 2147483647 |

**Nota:** El parámetro `model` es un combo dinámico que se expande para incluir entradas adicionales cuando se selecciona "Omni Flash". Estas entradas adicionales incluyen:
- `prompt` (STRING, requerido): La instrucción de texto que describe el video deseado. Describe la duración deseada (3-10 segundos) y la relación de aspecto (16:9 o 9:16) directamente en la instrucción.
- `images` (IMAGE, opcional): Imágenes de referencia para guiar la generación del video. Máximo de 14 imágenes.
- `videos` (VIDEO, opcional): Videos de referencia para guiar la generación del video. Máximo de 3 videos, cada uno con una duración máxima de 10 segundos.
- `temperature` (FLOAT, opcional, predeterminado: 1.0): Controla la aleatoriedad en la generación.
- `top_p` (FLOAT, opcional, predeterminado: 0.95): Controla el muestreo de núcleo.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `video` | El video generado con audio. | VIDEO |
| `text` | La respuesta de texto del modelo, si la hay. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiVideoOmni/es.md)

---
**Source fingerprint (SHA-256):** `948eb712ca0ad3b7d3c7b3a9e1576f2c52a3575c07d8d52bb727bd9df717caa6`
