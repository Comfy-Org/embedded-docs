# GuardarLatente

El nodo SaveLatent guarda tensores latentes en el disco como archivos para su uso posterior o para compartir. Toma muestras latentes y las guarda en el directorio de salida con metadatos opcionales que incluyen información de la indicación. El nodo maneja automáticamente la nomenclatura y organización de archivos, preservando la estructura de datos latentes.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `muestras` | Las muestras latentes que se guardarán en el disco | LATENT | Sí | - |
| `prefijo_nombre_archivo` | El prefijo para el nombre del archivo de salida (predeterminado: "latents/ComfyUI") | STRING | No | - |
| `prompt` | Información de la indicación para incluir en los metadatos (parámetro oculto) | PROMPT | No | - |
| `extra_pnginfo` | Información adicional PNG para incluir en los metadatos (parámetro oculto) | EXTRA_PNGINFO | No | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `samples` | Proporciona información de ubicación del archivo para el latente guardado en la interfaz de ComfyUI | UI |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLatent/es.md)

---
**Source fingerprint (SHA-256):** `dc7fd101c8dd93e2bcc39de64e0c39abe8e056c9e5932587fc6ce80e2fd143e8`
