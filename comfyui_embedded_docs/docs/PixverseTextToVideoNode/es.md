# PixVerse Texto a Video

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

Genera videos basados en un prompt de texto y varios parámetros de generación. Este nodo crea contenido de video utilizando la API de PixVerse, permitiendo controlar la relación de aspecto, calidad, duración, estilo de movimiento y más.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt para la generación del video (predeterminado: "") | STRING | Sí | - |
| `relación_de_aspecto` | Relación de aspecto para el video generado | COMBO | Sí | Opciones de PixverseAspectRatio |
| `calidad` | Configuración de calidad del video (predeterminado: PixverseQuality.res_540p) | COMBO | Sí | Opciones de PixverseQuality |
| `duración_segundos` | Duración del video generado en segundos | COMBO | Sí | Opciones de PixverseDuration |
| `modo_de_movimiento` | Estilo de movimiento para la generación del video | COMBO | Sí | Opciones de PixverseMotionMode |
| `semilla` | Semilla para la generación del video (predeterminado: 0) | INT | Sí | 0 a 2147483647 |
| `prompt_negativo` | Una descripción textual opcional de elementos no deseados en una imagen (predeterminado: "") | STRING | No | - |
| `plantilla_pixverse` | Una plantilla opcional para influir en el estilo de generación, creada por el nodo PixVerse Template | CUSTOM | No | - |

**Nota:** Al usar calidad 1080p, el modo de movimiento se establece automáticamente en normal y la duración se limita a 5 segundos. Para duraciones distintas a 5 segundos, el modo de movimiento también se establece automáticamente en normal.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | El archivo de video generado | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTextToVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `ab9264668f48533cb139abfb322e9a6e425a2ad7280da103a7fe0a7704158762`
