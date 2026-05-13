> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTextToVideoApi/es.md)

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

El nodo Wan Text to Video genera contenido de video basado en descripciones textuales. Utiliza modelos de IA para crear videos a partir de indicaciones y admite varios tamaños de video, duraciones y entradas de audio opcionales. El nodo puede generar audio automáticamente cuando sea necesario y proporciona opciones para mejorar las indicaciones y agregar marcas de agua.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `modelo` | COMBO | Sí | "wan2.5-t2v-preview"<br>"wan2.6-t2v" | Modelo a utilizar (predeterminado: "wan2.6-t2v") |
| `texto_descriptivo` | STRING | Sí | - | Indicación que describe los elementos y características visuales. Admite inglés y chino (predeterminado: "") |
| `texto_negativo` | STRING | No | - | Indicación negativa que describe lo que se debe evitar (predeterminado: "") |
| `tamaño` | COMBO | No | "480p: 1:1 (624x624)"<br>"480p: 16:9 (832x480)"<br>"480p: 9:16 (480x832)"<br>"720p: 1:1 (960x960)"<br>"720p: 16:9 (1280x720)"<br>"720p: 9:16 (720x1280)"<br>"720p: 4:3 (1088x832)"<br>"720p: 3:4 (832x1088)"<br>"1080p: 1:1 (1440x1440)"<br>"1080p: 16:9 (1920x1080)"<br>"1080p: 9:16 (1080x1920)"<br>"1080p: 4:3 (1632x1248)"<br>"1080p: 3:4 (1248x1632)" | Resolución y relación de aspecto del video (predeterminado: "720p: 1:1 (960x960)") |
| `duración` | INT | No | 5-15 (en incrementos de 5) | Duración del video en segundos. Una duración de 15 segundos solo está disponible para el modelo Wan 2.6 (predeterminado: 5) |
| `audio` | AUDIO | No | - | El audio debe contener una voz clara y fuerte, sin ruidos extraños ni música de fondo |
| `semilla` | INT | No | 0-2147483647 | Semilla a utilizar para la generación (predeterminado: 0) |
| `generar_audio` | BOOLEAN | No | - | Si no se proporciona entrada de audio, generar audio automáticamente (predeterminado: False) |
| `extender_texto` | BOOLEAN | No | - | Si se debe mejorar la indicación con asistencia de IA (predeterminado: True) |
| `marca_de_agua` | BOOLEAN | No | - | Si se debe agregar una marca de agua generada por IA al resultado (predeterminado: False) |
| `tipo_de_toma` | COMBO | No | "single"<br>"multi" | Especifica el tipo de toma para el video generado, es decir, si el video es una sola toma continua o múltiples tomas con cortes. Este parámetro solo tiene efecto cuando prompt_extend es True (predeterminado: "single") |

**Nota:** El modelo Wan 2.6 no admite resoluciones 480p. Una duración de 15 segundos solo es compatible con el modelo Wan 2.6. Al proporcionar entrada de audio, esta debe tener una duración entre 3.0 y 29.0 segundos y contener voz clara sin ruido de fondo ni música.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | VIDEO | El video generado basado en los parámetros de entrada |

---
**Source fingerprint (SHA-256):** `e978f384365060a6d71899e4e2e22b2c6f4268fb0da988c8902e4876d8597a96`
