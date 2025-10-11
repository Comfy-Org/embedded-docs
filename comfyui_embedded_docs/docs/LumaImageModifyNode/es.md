> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageModifyNode/es.md)

Modifica imágenes de forma síncrona basándose en el prompt y la relación de aspecto. Este nodo toma una imagen de entrada y la transforma de acuerdo con el prompt de texto proporcionado, manteniendo la relación de aspecto original de la imagen.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen de entrada que será modificada |
| `prompt` | STRING | Sí | - | Prompt para la generación de la imagen (valor por defecto: "") |
| `image_weight` | FLOAT | No | 0.0-0.98 | Peso de la imagen; cuanto más cercano a 1.0, menos se modificará la imagen (valor por defecto: 0.1) |
| `model` | MODEL | Sí | Múltiples opciones disponibles | El modelo Luma a utilizar para la modificación de la imagen |
| `seed` | INT | No | 0-18446744073709551615 | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales son no deterministas independientemente de la semilla (valor por defecto: 0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `image` | IMAGE | La imagen modificada generada por el modelo Luma |