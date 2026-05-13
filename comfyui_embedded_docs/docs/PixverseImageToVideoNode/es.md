> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseImageToVideoNode/es.md)

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

Genera videos basados en una imagen de entrada y un texto de instrucción. Este nodo toma una imagen y crea un video animado aplicando la configuración de movimiento y calidad especificada para transformar la imagen estática en una secuencia en movimiento.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|--------------|-----------|-------|-------------|
| `image` | IMAGE | Sí | - | Imagen de entrada para transformar en video |
| `prompt` | STRING | Sí | - | Instrucción para la generación del video |
| `quality` | COMBO | Sí | `res_540p`<br>`res_1080p` | Configuración de calidad del video (predeterminado: res_540p) |
| `duration_seconds` | COMBO | Sí | `dur_2`<br>`dur_5`<br>`dur_10` | Duración del video generado en segundos |
| `motion_mode` | COMBO | Sí | `normal`<br>`fast`<br>`slow`<br>`zoom_in`<br>`zoom_out`<br>`pan_left`<br>`pan_right`<br>`pan_up`<br>`pan_down`<br>`tilt_up`<br>`tilt_down`<br>`roll_clockwise`<br>`roll_counterclockwise` | Estilo de movimiento aplicado a la generación del video |
| `seed` | INT | Sí | 0-2147483647 | Semilla para la generación del video (predeterminado: 0) |
| `negative_prompt` | STRING | No | - | Una descripción textual opcional de elementos no deseados en una imagen |
| `pixverse_template` | CUSTOM | No | - | Una plantilla opcional para influir en el estilo de generación, creada por el nodo Plantilla PixVerse |

**Nota:** Al usar calidad 1080p, el modo de movimiento se establece automáticamente en normal y la duración se limita a 5 segundos. Para duraciones distintas a 5 segundos, el modo de movimiento también se establece automáticamente en normal.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | VIDEO | Video generado basado en la imagen de entrada y los parámetros |

---
**Source fingerprint (SHA-256):** `7630c662a2506fb0c8be0cb9c6bfdfcf0fc06d2b6f16b8636664d587affededc`
