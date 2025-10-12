> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaReferenceNode/es.md)

Este nodo contiene una imagen y un valor de peso para usar con el nodo Luma Generate Image. Crea una cadena de referencia que puede pasarse a otros nodos Luma para influir en la generación de imágenes. El nodo puede iniciar una nueva cadena de referencia o agregarse a una existente.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `imagen` | IMAGE | Sí | - | Imagen a utilizar como referencia. |
| `peso` | FLOAT | Sí | 0.0 - 1.0 | Peso de la referencia de imagen (valor por defecto: 1.0). |
| `luma_ref` | LUMA_REF | No | - | Cadena de referencia Luma existente opcional a la cual agregarse. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `luma_ref` | LUMA_REF | La cadena de referencia Luma que contiene la imagen y el peso. |
