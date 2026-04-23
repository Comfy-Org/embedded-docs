> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNode/es.md)

El nodo ByteDance Seedance 2.0 Reference to Video utiliza el modelo de IA Seedance 2.0 para crear, editar o extender videos basándose en su indicación de texto y los materiales de referencia proporcionados. Puede usar imágenes, videos y audio como referencias para guiar el proceso de generación, admitiendo tareas como edición y extensión de video.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sí | `"Seedance 2.0"`<br>`"Seedance 2.0 Fast"` | El modelo de IA a utilizar. Seedance 2.0 es para la máxima calidad, mientras que Seedance 2.0 Fast está optimizado para velocidad. Seleccionar un modelo revela entradas adicionales obligatorias para `prompt`, `resolution`, `duration`, `ratio`, `generate_audio`, y entradas opcionales para `reference_images`, `reference_videos`, `reference_audios`, `reference_assets` y `auto_downscale`. |
| `seed` | INT | No | 0 a 2147483647 | Un número utilizado para controlar si el nodo debe volver a ejecutarse. Los resultados son no deterministas independientemente del valor de la semilla (predeterminado: 0). |
| `watermark` | BOOLEAN | No | `True` / `False` | Indica si se debe agregar una marca de agua al video generado (predeterminado: False). |

**Restricciones importantes:**
*   Se requiere al menos una imagen o video de referencia (proporcionado a través de las entradas `reference_images`, `reference_videos` o `reference_assets`) para que el nodo funcione.
*   Cada video de referencia debe tener una duración de al menos 1.8 segundos. La duración combinada de todos los videos de referencia no puede exceder los 15.1 segundos.
*   Cada clip de audio de referencia debe tener una duración de al menos 1.8 segundos. La duración combinada de todo el audio de referencia no puede exceder los 15.1 segundos.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `video` | VIDEO | El archivo de video generado. |