> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelPatchLoader/es.md)

El nodo ModelPatchLoader carga parches de modelo especializados desde la carpeta model_patches. Detecta automáticamente el tipo de archivo de parche y carga la arquitectura de modelo adecuada, luego lo envuelve en un ModelPatcher para su uso en el flujo de trabajo. Este nodo admite diferentes tipos de parches, incluidos bloques de controlnet, modelos de incrustación de características y otras arquitecturas especializadas.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `nombre` | STRING | Sí | Todos los archivos de parche de modelo disponibles en la carpeta model_patches | El nombre del archivo de parche de modelo a cargar desde el directorio model_patches |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `MODEL_PATCH` | MODEL_PATCH | El parche de modelo cargado, envuelto en un ModelPatcher para su uso en el flujo de trabajo |

---
**Source fingerprint (SHA-256):** `e394e165cf416019ed53d9fde42d97c3c9b9f9afd843b12371a624467a4841bf`
