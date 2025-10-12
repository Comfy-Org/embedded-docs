> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxDisableGuidance/es.md)

Este nodo desactiva completamente la funcionalidad de incrustación de guía para Flux y modelos similares. Toma datos de condicionamiento como entrada y elimina el componente de guía estableciéndolo en None, desactivando efectivamente el condicionamiento basado en guía para el proceso de generación.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `acondicionamiento` | CONDITIONING | Sí | - | Los datos de condicionamiento a procesar y de los cuales eliminar la guía |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `acondicionamiento` | CONDITIONING | Los datos de condicionamiento modificados con la guía desactivada |
