> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaConceptsNode/es.md)

Almacena uno o más Conceptos de Cámara para usar con los nodos Luma Text to Video y Luma Image to Video. Este nodo permite seleccionar hasta cuatro conceptos de cámara y opcionalmente combinarlos con cadenas de conceptos existentes.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `concept1` | STRING | Sí | Múltiples opciones disponibles<br>Incluye opción "None" | Primera selección de concepto de cámara de los conceptos Luma disponibles |
| `concept2` | STRING | Sí | Múltiples opciones disponibles<br>Incluye opción "None" | Segunda selección de concepto de cámara de los conceptos Luma disponibles |
| `concept3` | STRING | Sí | Múltiples opciones disponibles<br>Incluye opción "None" | Tercera selección de concepto de cámara de los conceptos Luma disponibles |
| `concept4` | STRING | Sí | Múltiples opciones disponibles<br>Incluye opción "None" | Cuarta selección de concepto de cámara de los conceptos Luma disponibles |
| `luma_concepts` | LUMA_CONCEPTS | No | N/A | Conceptos de Cámara opcionales para agregar a los seleccionados aquí |

**Nota:** Todos los parámetros de concepto (`concept1` a `concept4`) pueden establecerse en "None" si no desea utilizar las cuatro ranuras de concepto. El nodo fusionará cualquier `luma_concepts` proporcionado con los conceptos seleccionados para crear una cadena de conceptos combinada.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `luma_concepts` | LUMA_CONCEPTS | Cadena de conceptos de cámara combinada que contiene todos los conceptos seleccionados |