> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ImageToVideoApi/es.md)

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

El nodo Wan 2.7 Image to Video genera un video a partir de una imagen de primer fotograma. Opcionalmente, puedes proporcionar una imagen de último fotograma para crear una transición entre ambos, o un archivo de audio para guiar el movimiento y la sincronización del video. El nodo utiliza un modelo de IA para animar la escena basándose en tu descripción textual.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `modelo` | COMBO | Sí | `"wan2.7-i2v"` | El modelo de IA a utilizar para la generación de video. |
| `model.prompt` | STRING | Sí | - | Una descripción textual de los elementos y características visuales que deseas en el video. Admite inglés y chino. |
| `model.negative_prompt` | STRING | Sí | - | Una descripción textual de elementos o características que deseas que el modelo evite. |
| `model.resolution` | COMBO | Sí | `"720P"`<br>`"1080P"` | La resolución del video de salida. |
| `model.duration` | INT | Sí | 2 a 15 | La duración del video generado en segundos (predeterminado: 5). |
| `primer_fotograma` | IMAGE | Sí | - | La imagen que se usará como primer fotograma del video. La relación de aspecto del video de salida se deriva de esta imagen. |
| `último_fotograma` | IMAGE | No | - | Una imagen opcional para usar como último fotograma. Al proporcionarla, el modelo genera un video que realiza una transición desde el primer fotograma hasta este último. |
| `audio` | AUDIO | No | - | Un archivo de audio opcional para guiar la generación del video, útil para sincronización labial o movimiento sincronizado con el ritmo. La duración debe estar entre 2 y 30 segundos. Si no se proporciona, el modelo generará música de fondo o efectos de sonido acordes. |
| `semilla` | INT | Sí | 0 a 2147483647 | Un valor de semilla para controlar la aleatoriedad de la generación (predeterminado: 0). |
| `extender_prompt` | BOOLEAN | Sí | - | Cuando está habilitado, el nodo utilizará asistencia de IA para mejorar tu prompt de texto (predeterminado: True). Esta es una configuración avanzada. |
| `marca_de_agua` | BOOLEAN | Sí | - | Cuando está habilitado, se añadirá una marca de agua generada por IA al video final (predeterminado: False). Esta es una configuración avanzada. |

**Nota:** La entrada `audio` tiene una restricción de duración. Si se proporciona, el archivo de audio debe tener una duración de entre 2 y 30 segundos.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | VIDEO | El archivo de video generado. |

---
**Source fingerprint (SHA-256):** `ccd18dca3b191f2cbe64b6c2b941a7efcf281e4f327329d932cec27fd8234133`
