# Cargador de Parches de Modelo

El nodo ModelPatchLoader carga archivos de parche de modelo especializados desde la carpeta `model_patches`. Detecta automáticamente el tipo de parche a partir del contenido del archivo y carga la arquitectura de modelo correspondiente, para luego envolverlo en un ModelPatcher y usarlo en el flujo de trabajo. Este nodo admite diferentes tipos de parche, incluidos bloques de ControlNet, modelos de incrustación de características y otras arquitecturas especializadas.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `nombre` | El nombre del archivo del parche de modelo que se carga desde el directorio `model_patches`. | STRING | Sí | Todos los archivos de parche de modelo disponibles en la carpeta `model_patches`. |

Nota: Este nodo está marcado como experimental. El tipo de parche se detecta automáticamente a partir del contenido del archivo, por lo que no se requiere selección manual de tipo.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `MODEL_PATCH` | El parche de modelo cargado, envuelto en un ModelPatcher para usarlo en el flujo de trabajo. | MODEL_PATCH |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelPatchLoader/es.md)

---
**Source fingerprint (SHA-256):** `7f5225521b82b39b85183ccc7957fc4172e64aed9289f66d53969ea4a2e81b7f`
