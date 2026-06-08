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

El nodo Kling Start-End Frame to Video crea una secuencia de video que realiza una transición entre las imágenes de inicio y fin proporcionadas. Genera todos los fotogramas intermedios para producir una transformación suave desde el primer fotograma hasta el último. Este nodo utiliza la API de imagen a video, pero solo admite las opciones de entrada que funcionan con el campo de solicitud `image_tail`.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `start_frame` | Imagen de referencia - URL o cadena codificada en Base64, no puede superar los 10MB, resolución no inferior a 300*300px, relación de aspecto entre 1:2.5 y 2.5:1. Base64 no debe incluir el prefijo data:image. | IMAGE | Sí | - |
| `end_frame` | Imagen de referencia - Control del fotograma final. URL o cadena codificada en Base64, no puede superar los 10MB, resolución no inferior a 300*300px. Base64 no debe incluir el prefijo data:image. | IMAGE | Sí | - |
| `prompt` | Prompt de texto positivo | STRING | Sí | - |
| `negative_prompt` | Prompt de texto negativo | STRING | Sí | - |
| `cfg_scale` | Controla la fuerza de la guía del prompt (predeterminado: 0.5) | FLOAT | No | 0.0-1.0 |
| `aspect_ratio` | La relación de aspecto para el video generado (predeterminado: "16:9") | COMBO | No | "16:9"<br>"9:16"<br>"1:1" |
| `mode` | La configuración a utilizar para la generación de video siguiendo el formato: modo / duración / nombre_del_modelo. (predeterminado: la séptima opción de los modos disponibles) | COMBO | No | Múltiples opciones disponibles |

**Restricciones de las imágenes:**

- Tanto `start_frame` como `end_frame` deben proporcionarse y no pueden superar un tamaño de archivo de 10MB
- Resolución mínima: 300×300 píxeles para ambas imágenes
- La relación de aspecto de `start_frame` debe estar entre 1:2.5 y 2.5:1
- Las imágenes codificadas en Base64 no deben incluir el prefijo "data:image"

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `video_id` | La secuencia de video generada | VIDEO |
| `duration` | Identificador único para el video generado | STRING |
| `duration` | Duración del video generado | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingStartEndFrameNode/es.md)

---
**Source fingerprint (SHA-256):** `1df5820b4f41ccd5afec8e2701888d90c940f164c433c7f81397b41e8fc333c6`
