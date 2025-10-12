> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNode/es.md)

El TripoTextureNode genera modelos 3D texturizados utilizando la API de Tripo. Toma un ID de tarea de modelo y aplica generación de texturas con varias opciones que incluyen materiales PBR, configuraciones de calidad de textura y métodos de alineación. El nodo se comunica con la API de Tripo para procesar la solicitud de generación de texturas y devuelve el archivo de modelo resultante y el ID de tarea.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model_task_id` | MODEL_TASK_ID | Sí | - | El ID de tarea del modelo al que aplicar texturas |
| `texture` | BOOLEAN | No | - | Si generar texturas (valor predeterminado: True) |
| `pbr` | BOOLEAN | No | - | Si generar materiales PBR (Renderizado Basado en Física) (valor predeterminado: True) |
| `texture_seed` | INT | No | - | Semilla aleatoria para la generación de texturas (valor predeterminado: 42) |
| `texture_quality` | COMBO | No | "standard"<br>"detailed" | Nivel de calidad para la generación de texturas (valor predeterminado: "standard") |
| `texture_alignment` | COMBO | No | "original_image"<br>"geometry" | Método para alinear texturas (valor predeterminado: "original_image") |

*Nota: Este nodo requiere tokens de autenticación y claves API que son manejados automáticamente por el sistema.*

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model_file` | STRING | El archivo de modelo generado con texturas aplicadas |
| `model task_id` | MODEL_TASK_ID | El ID de tarea para rastrear el proceso de generación de texturas |
