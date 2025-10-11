> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TorchCompileModel/es.md)

El nodo TorchCompileModel aplica la compilación de PyTorch a un modelo para optimizar su rendimiento. Crea una copia del modelo de entrada y lo envuelve con la funcionalidad de compilación de PyTorch utilizando el backend especificado. Esto puede mejorar la velocidad de ejecución del modelo durante la inferencia.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo que será compilado y optimizado |
| `backend` | STRING | Sí | "inductor"<br>"cudagraphs" | El backend de compilación de PyTorch que se utilizará para la optimización |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | El modelo compilado con la compilación de PyTorch aplicada |