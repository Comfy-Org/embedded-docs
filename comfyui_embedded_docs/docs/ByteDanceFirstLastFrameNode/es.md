> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceFirstLastFrameNode/es.md)

Eres un experto en traducción técnica especializado en documentación de nodos ComfyUI del inglés al español.

## Reglas de Traducción

1. **Contenido que NO debe traducirse:**
   - Nombres de parámetros entre comillas invertidas: `image`, `seed`, `model`
   - Tipos de datos en MAYÚSCULAS: IMAGE, STRING, INT, FLOAT, MODEL, CONDITIONING, etc.
   - Valores en columna Range: números, "auto", nombres de opciones
   - Código, rutas de archivos

2. **Contenido que SÍ debe traducirse:**
   - Títulos de secciones: ## Descripción general, ## Entradas, ## Salidas
   - Todo el texto descriptivo y explicativo
   - Descripciones de parámetros

3. **Calidad de traducción:**
   - Usar español estándar y neutral
   - Mantener tono profesional pero accesible
   - Asegurar precisión técnica
   - Usar terminología técnica estándar en español

4. **Formato:**
   - Mantener todo el formato Markdown
   - Preservar estructura de tablas
   - No agregar ninguna nota o enlace al inicio del documento (será agregado automáticamente)

Por favor traduce la siguiente documentación al español, sin incluir la nota inicial del documento:

Este nodo genera un video utilizando un prompt de texto junto con imágenes del primer y último fotograma. Toma tu descripción y los dos fotogramas clave para crear una secuencia de video completa que realiza la transición entre ellos. El nodo proporciona varias opciones para controlar la resolución, la relación de aspecto, la duración y otros parámetros de generación del video.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sí | `"seedance-1-5-pro-251215"`<br>`"seedance-1-0-pro-250528"`<br>`"seedance-1-0-lite-i2v-250428"` | El modelo a utilizar para la generación de video (predeterminado: `"seedance-1-0-lite-i2v-250428"`). |
| `prompt` | STRING | Sí | - | El prompt de texto utilizado para generar el video. |
| `first_frame` | IMAGE | Sí | - | Primer fotograma a utilizar para el video. Debe tener entre 300x300 y 6000x6000 píxeles, con una relación de aspecto entre 0.4 y 2.5. |
| `last_frame` | IMAGE | Sí | - | Último fotograma a utilizar para el video. Debe tener entre 300x300 y 6000x6000 píxeles, con una relación de aspecto entre 0.4 y 2.5. |
| `resolution` | COMBO | Sí | `"480p"`<br>`"720p"`<br>`"1080p"` | La resolución del video de salida. |
| `aspect_ratio` | COMBO | Sí | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` | La relación de aspecto del video de salida (predeterminado: `"adaptive"`). |
| `duration` | INT | Sí | 3 - 12 | La duración del video de salida en segundos (predeterminado: 5). Nota: Para el modelo `seedance-1-5-pro-251215`, la duración mínima compatible es de 4 segundos. |
| `seed` | INT | No | 0 - 2147483647 | Semilla a utilizar para la generación (predeterminado: 0). |
| `camera_fixed` | BOOLEAN | No | - | Especifica si se debe fijar la cámara. La plataforma añade una instrucción para fijar la cámara a tu prompt, pero no garantiza el efecto real (predeterminado: False). |
| `watermark` | BOOLEAN | No | - | Si se debe añadir una marca de agua "Generado por IA" al video (predeterminado: False). |
| `generate_audio` | BOOLEAN | No | - | Este parámetro se ignora para cualquier modelo excepto `seedance-1-5-pro-251215` (predeterminado: False). |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El archivo de video generado |

---
**Source fingerprint (SHA-256):** `2da7b8ad2bc818a21988c028155ba2b466452a1655ac506fcef01c143dda7450`
