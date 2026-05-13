> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSave/es.md)

El nodo ModelSave guarda modelos entrenados o modificados en el almacenamiento de tu computadora. Toma un modelo como entrada y lo escribe en un archivo con el nombre de archivo que especifiques. Esto te permite conservar tu trabajo y reutilizar modelos en proyectos futuros.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `modelo` | MODEL | Sí | - | El modelo que se guardará en el disco |
| `prefijo_nombre_archivo` | STRING | Sí | - | Prefijo de nombre de archivo y ruta para el archivo del modelo guardado (predeterminado: "diffusion_models/ComfyUI") |
| `prompt` | PROMPT | No | - | Información de la solicitud del flujo de trabajo (se proporciona automáticamente) |
| `extra_pnginfo` | EXTRA_PNGINFO | No | - | Metadatos adicionales del flujo de trabajo (se proporcionan automáticamente) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| *Ninguno* | - | Este nodo no devuelve ningún valor de salida |

---
**Source fingerprint (SHA-256):** `1dda8a6d85aa19b739c1fe3e6e7f816e05011044fc8b0b91b23fa303f71d8b19`
