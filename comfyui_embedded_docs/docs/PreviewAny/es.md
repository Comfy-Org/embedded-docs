> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAny/es.md)

El nodo PreviewAny muestra una vista previa de cualquier tipo de dato de entrada en formato de texto. Acepta cualquier tipo de dato como entrada y lo convierte a una representación de cadena legible para su visualización. El nodo maneja automáticamente diferentes tipos de datos incluyendo cadenas, números, booleanos y objetos complejos intentando serializarlos a formato JSON.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `fuente` | ANY | Sí | Cualquier tipo de dato | Acepta cualquier tipo de dato de entrada para mostrar en la vista previa |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| Visualización de Texto en UI | TEXT | Muestra los datos de entrada convertidos a formato texto en la interfaz de usuario |
