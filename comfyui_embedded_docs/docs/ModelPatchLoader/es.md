# Cargador de Parches de Modelo

El nodo ModelPatchLoader carga parches de modelo especializados desde la carpeta model_patches. Detecta automáticamente el tipo de archivo de parche y carga la arquitectura de modelo adecuada, luego lo envuelve en un ModelPatcher para usarlo en el flujo de trabajo. Este nodo admite diferentes tipos de parches, incluyendo bloques de controlnet, modelos de incrustación de características y otras arquitecturas especializadas.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `name` | El nombre del archivo del parche de modelo para cargar desde el directorio model_patches | STRING | Sí | Todos los archivos de parche de modelo disponibles en la carpeta model_patches |

Nota: Este nodo está marcado como experimental en ComfyUI. El tipo de parche se detecta automáticamente a partir del contenido del archivo, por lo que un solo nodo puede manejar varios tipos de parches.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `MODEL_PATCH` | El parche de modelo cargado envuelto en un ModelPatcher para usarlo en el flujo de trabajo | MODEL_PATCH |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelPatchLoader/es.md)

---
**Source fingerprint (SHA-256):** `7f5225521b82b39b85183ccc7957fc4172e64aed9289f66d53969ea4a2e81b7f`
