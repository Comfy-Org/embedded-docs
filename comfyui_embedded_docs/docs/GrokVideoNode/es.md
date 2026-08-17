# Video Grok

El nodo Grok Video genera un video corto a partir de una descripción de texto. Puede crear un video desde cero usando un prompt, o animar una única imagen de entrada, opcionalmente guiada por un prompt. El nodo envía una solicitud a una API externa y devuelve el video generado.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `model` | El modelo a utilizar para la generación de video. | COMBO | Sí | "grok-imagine-video"<br>"grok-imagine-video-1.5" |
| `prompt` | Descripción de texto del video deseado. Opcional para grok-imagine-video-1.5 cuando se proporciona una imagen de entrada. | STRING | Sí | - |
| `resolution` | La resolución del video de salida. 1080p solo está disponible para grok-imagine-video-1.5. | COMBO | Sí | "480p"<br>"720p"<br>"1080p" |
| `aspect_ratio` | La relación de aspecto del video de salida (por defecto: "auto"). | COMBO | Sí | "auto"<br>"16:9"<br>"4:3"<br>"3:2"<br>"1:1"<br>"2:3"<br>"3:4"<br>"9:16" |
| `duration` | La duración del video de salida en segundos (por defecto: 6). | INT | Sí | 1 a 15 |
| `seed` | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales son no deterministas independientemente de la semilla (por defecto: 0). | INT | Sí | 0 a 2147483647 |
| `image` | Imagen inicial opcional. Si se omite, el video se genera únicamente a partir del prompt de texto. | IMAGE | No | - |

**Nota:**
- La resolución "1080p" solo está disponible con el modelo `grok-imagine-video-1.5`. Seleccionarla con `grok-imagine-video` genera un error.
- Solo se admite una imagen de entrada. Proporcionar varias imágenes genera un error.
- El parámetro `prompt` es obligatorio a menos que el modelo esté configurado como `grok-imagine-video-1.5` y se proporcione una imagen de entrada. Cuando es obligatorio, el prompt debe tener al menos 1 carácter después de eliminar los espacios en blanco.
- El parámetro `seed` solo determina si el nodo se vuelve a ejecutar; los resultados generados son no deterministas independientemente del valor de la semilla.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `output` | El video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `c708c8cd78749aa533db63e2bc5938ef14fa78cf95f8ba4628d0c586f8723297`
