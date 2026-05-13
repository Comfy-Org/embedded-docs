> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLatent/es.md)

El nodo SaveLatent guarda tensores latentes en el disco como archivos para su uso posterior o para compartir. Toma muestras latentes y las guarda en el directorio de salida con metadatos opcionales que incluyen información de la indicación. El nodo maneja automáticamente la nomenclatura y organización de archivos, preservando la estructura de datos latentes.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|--------------|-----------|-------|-------------|
| `samples` | LATENT | Sí | - | Las muestras latentes que se guardarán en el disco |
| `filename_prefix` | STRING | No | - | El prefijo para el nombre del archivo de salida (predeterminado: "latents/ComfyUI") |
| `prompt` | PROMPT | No | - | Información de la indicación para incluir en los metadatos (parámetro oculto) |
| `extra_pnginfo` | EXTRA_PNGINFO | No | - | Información adicional PNG para incluir en los metadatos (parámetro oculto) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `ui` | UI | Proporciona información de ubicación del archivo para el latente guardado en la interfaz de ComfyUI |

---
**Source fingerprint (SHA-256):** `dc7fd101c8dd93e2bcc39de64e0c39abe8e056c9e5932587fc6ce80e2fd143e8`
