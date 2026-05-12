> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadBackgroundRemovalModel/es.md)

## Resumen

Carga un modelo de eliminación de fondo desde un archivo. Este nodo prepara el modelo para su uso en la eliminación de fondos de imágenes.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `bg_removal_name` | STRING | Sí | Lista de archivos de modelo disponibles | El modelo utilizado para eliminar fondos de imágenes. Selecciona de la lista de archivos de modelo de eliminación de fondo disponibles. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `bg_model` | BACKGROUND_REMOVAL | El modelo de eliminación de fondo cargado, listo para ser utilizado por otros nodos para procesar imágenes. |