# PixVerse V6 de texto a vídeo

PixVerse V6 Text to Video genera un video a partir de un prompt de texto utilizando el modelo V6 de PixVerse. El nodo envía el prompt junto con la resolución, duración, relación de aspecto y otras configuraciones elegidas a PixVerse, espera a que finalice la generación y devuelve el video resultante, incluida una pista de audio nativa cuando la generación de audio está habilitada.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `modelo` | Configuración del modelo y de la generación. Seleccione el modelo y configure sus opciones de generación. | DYNAMIC_COMBO | Sí | "PixVerse V6" |

### Entradas de PixVerse V6

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `prompt` | Prompt para la generación del video. (por defecto: "") | STRING | Sí | 1–5000 caracteres |
| `aspect_ratio` | Relación de aspecto de salida. Seleccione una de las relaciones de aspecto compatibles con PixVerse V6. | COMBO | Sí | Múltiples opciones disponibles |
| `quality` | Resolución de salida. Define el borde largo: 360p es 640px, 540p 1024px, 720p 1280px, 1080p 1920px. (por defecto: "720p") | COMBO | Sí | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `duration_seconds` | Duración del video generado en segundos. (por defecto: 5) | INT | Sí | 1–15 |
| `generate_audio` | Generar una pista de audio nativa junto con el video. (por defecto: True) | BOOLEAN | Sí | True<br>False |
| `multi_clip` | Permite que el modelo divida el video en varias tomas en lugar de una única toma continua. (por defecto: False) | BOOLEAN | Sí | True<br>False |
| `seed` | Semilla para la generación del video. PixVerse la registra, pero no puede reproducir una ejecución a partir de ella. Permite la aleatorización después de la generación. (por defecto: 42) | INT | Sí | 0–2147483647 |
| `negative_prompt` | Una descripción de texto opcional de los elementos no deseados en el video. (por defecto: "") | STRING | No | 0–2048 caracteres |
| `style` | Un estilo visual opcional aplicado a todo el video. (por defecto: "none") | COMBO | No | Múltiples opciones disponibles |

**Nota:** El `prompt` es obligatorio y, después de recortar los espacios en blanco, no debe estar vacío; su longitud máxima es de 5000 caracteres. El `negative_prompt` está limitado a 2048 caracteres. Establecer `style` en "none" (el valor predeterminado) significa que no se aplica ningún estilo visual. La `seed` es registrada por PixVerse, pero no se puede utilizar para reproducir la misma ejecución. El nodo espera a que PixVerse termine de generar el video y luego lo descarga; si la solicitud falla — por ejemplo, porque PixVerse ya alcanzó su número máximo de generaciones simultáneas, la cuenta del proveedor no tiene créditos, o la moderación de contenido rechaza el prompt — el nodo devuelve un error.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `VIDEO` | El video generado. Si `generate_audio` está habilitado, el video incluye la pista de audio nativa. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseV6TextToVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `4c268be9720a4606e77a9347570ac26b489625fc6b9528b9d3cceb4497d8683b`
