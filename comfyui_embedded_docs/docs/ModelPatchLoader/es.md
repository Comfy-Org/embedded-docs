> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelPatchLoader/es.md)

El nodo ModelPatchLoader carga parches de modelos especializados desde la carpeta model_patches. Detecta automáticamente el tipo de archivo de parche y carga la arquitectura de modelo correspondiente, luego lo envuelve en un ModelPatcher para su uso en el flujo de trabajo. Este nodo admite diferentes tipos de parches, incluyendo bloques controlnet y modelos de incrustación de características.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `name` | STRING | Sí | Todos los archivos de parches de modelo disponibles desde la carpeta model_patches | El nombre de archivo del parche de modelo a cargar desde el directorio model_patches |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `MODEL_PATCH` | MODEL_PATCH | El parche de modelo cargado envuelto en un ModelPatcher para su uso en el flujo de trabajo |