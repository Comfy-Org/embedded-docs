> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNode/es.md)

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

El nodo ByteDance Seedance 2.0 Reference to Video utiliza el modelo de IA Seedance 2.0 para crear, editar o extender videos basándose en tu indicación de texto y los materiales de referencia proporcionados. Puede usar imágenes, videos y audio como referencias para guiar el proceso de generación, admitiendo tareas como edición y extensión de video.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `modelo` | COMBO | Sí | `"Seedance 2.0"`<br>`"Seedance 2.0 Fast"` | El modelo de IA a utilizar. Seedance 2.0 es para máxima calidad, mientras que Seedance 2.0 Fast está optimizado para velocidad. Al seleccionar un modelo, se revelan entradas adicionales obligatorias para `prompt`, `resolution`, `duration`, `ratio`, `generate_audio`, y entradas opcionales para `reference_images`, `reference_videos`, `reference_audios`, `reference_assets` y `auto_downscale`. |
| `semilla` | INT | No | 0 a 2147483647 | Número utilizado para controlar si el nodo debe reejecutarse. Los resultados no son deterministas independientemente del valor de la semilla (predeterminado: 0). |
| `marca_de_agua` | BOOLEAN | No | `True` / `False` | Indica si se debe añadir una marca de agua al video generado (predeterminado: False). |

**Restricciones importantes:**
*   Se requiere al menos una imagen o video de referencia (proporcionados a través de las entradas `reference_images`, `reference_videos` o `reference_assets`) para que el nodo funcione.
*   Se puede usar un máximo de 9 imágenes de referencia en total (incluyendo aquellas de `reference_images` y `reference_assets`).
*   Se puede usar un máximo de 3 videos de referencia en total (incluyendo aquellos de `reference_videos` y `reference_assets`).
*   Se puede usar un máximo de 3 clips de audio de referencia en total (incluyendo aquellos de `reference_audios` y `reference_assets`).
*   Cada video de referencia debe tener al menos 1.8 segundos de duración. La duración combinada de todos los videos de referencia no puede exceder los 15.1 segundos.
*   Cada clip de audio de referencia debe tener al menos 1.8 segundos de duración. La duración combinada de todo el audio de referencia no puede exceder los 15.1 segundos.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `video` | VIDEO | El archivo de video generado. |

---
**Source fingerprint (SHA-256):** `72c8a2f821b9fb9853a4d0428785c432d0852ae562080292817f8a7d52967c7f`
