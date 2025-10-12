> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceLatent/es.md)

Este nodo establece el latente de referencia para un modelo de edición. Toma datos de condicionamiento y una entrada latente opcional, luego modifica el condicionamiento para incluir información latente de referencia. Si el modelo lo admite, puedes encadenar múltiples nodos ReferenceLatent para establecer múltiples imágenes de referencia.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `conditioning` | CONDITIONING | Sí | - | Los datos de condicionamiento que serán modificados con información latente de referencia |
| `latent` | LATENT | No | - | Datos latentes opcionales para usar como referencia para el modelo de edición |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | CONDITIONING | Los datos de condicionamiento modificados que contienen información latente de referencia |
