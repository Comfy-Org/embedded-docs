> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelComputeDtype/es.md)

El nodo ModelComputeDtype permite cambiar el tipo de datos computacional utilizado por un modelo durante la inferencia. Crea una copia del modelo de entrada y aplica la configuración de tipo de datos especificada, lo que puede ayudar a optimizar el uso de memoria y el rendimiento según las capacidades de su hardware. Esto es particularmente útil para depuración y pruebas de diferentes configuraciones de precisión.

## Entradas

| Parámetro | Tipo de Datos | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `modelo` | MODEL | Sí | - | El modelo de entrada a modificar con un nuevo tipo de datos computacional |
| `dtype` | STRING | Sí | "default"<br>"fp32"<br>"fp16"<br>"bf16" | El tipo de datos computacional a aplicar al modelo |

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|-------------|-----------|-------------|
| `modelo` | MODEL | El modelo modificado con el nuevo tipo de datos computacional aplicado |