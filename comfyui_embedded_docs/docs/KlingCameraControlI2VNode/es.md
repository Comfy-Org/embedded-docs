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

El nodo de Control de Cámara Kling de Imagen a Video transforma imágenes fijas en videos cinematográficos con movimientos de cámara profesionales. Este nodo especializado de imagen a video te permite controlar acciones virtuales de cámara, incluyendo zoom, rotación, paneo, inclinación y vista en primera persona, manteniendo el enfoque en tu imagen original. El control de cámara solo es compatible actualmente en modo profesional con el modelo kling-v1-5 a una duración de 5 segundos.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `start_frame` | Imagen de Referencia - URL o cadena codificada en Base64, no puede exceder 10MB, resolución no menor a 300x300px, relación de aspecto entre 1:2.5 y 2.5:1. Base64 no debe incluir el prefijo data:image. | IMAGE | Sí | - |
| `prompt` | Prompt de texto positivo que describe el contenido deseado del video | STRING | Sí | - |
| `negative_prompt` | Prompt de texto negativo que describe lo que se debe evitar en el video generado | STRING | Sí | - |
| `cfg_scale` | Controla la fuerza de la guía de texto. Valores más altos hacen que la salida siga más fielmente el prompt (predeterminado: 0.75) | FLOAT | No | 0.0 a 1.0 |
| `aspect_ratio` | La relación de aspecto del video generado (predeterminado: "16:9") | COMBO | No | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `camera_control` | Se puede crear usando el nodo Controles de Cámara Kling. Controla el movimiento y desplazamiento de la cámara durante la generación del video. | CAMERA_CONTROL | Sí | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `video_id` | La salida de video generada | VIDEO |
| `duration` | Identificador único para el video generado | STRING |
| `duration` | Duración del video generado | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControlI2VNode/es.md)

---
**Source fingerprint (SHA-256):** `a2965975cd484768298f4c7e504423f782ea032dfb5ef304579715be9c27cb79`
