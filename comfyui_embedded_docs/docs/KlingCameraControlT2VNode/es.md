> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControlT2VNode/es.md)

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

El nodo de Control de Cámara para Video de Texto a Video de Kling transforma texto en videos cinematográficos con movimientos de cámara profesionales que simulan la cinematografía del mundo real. Este nodo permite controlar acciones de cámara virtual, incluyendo zoom, rotación, paneo, inclinación y vista en primera persona, manteniendo el enfoque en tu texto original. La duración, el modo y el nombre del modelo están codificados porque el control de cámara solo es compatible en modo profesional con el modelo kling-v1-5 a una duración de 5 segundos.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | - | Prompt de texto positivo |
| `negative_prompt` | STRING | Sí | - | Prompt de texto negativo |
| `cfg_scale` | FLOAT | No | 0.0-1.0 | Controla qué tan fielmente la salida sigue el prompt (predeterminado: 0.75) |
| `aspect_ratio` | COMBO | No | "16:9"<br>"9:16"<br>"1:1"<br>"21:9"<br>"3:4"<br>"4:3" | La relación de aspecto para el video generado (predeterminado: "16:9") |
| `camera_control` | CAMERA_CONTROL | No | - | Se puede crear usando el nodo Controles de Cámara de Kling. Controla el movimiento y desplazamiento de la cámara durante la generación del video. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El video generado con efectos de control de cámara |
| `video_id` | STRING | El identificador único para el video generado |
| `duration` | STRING | La duración del video generado |

---
**Source fingerprint (SHA-256):** `4ebdd6af31f9e5c0816c4bcba886179b3f7d2b5030ff4fa3ddad6df25c528af7`
