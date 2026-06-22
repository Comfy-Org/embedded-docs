# GuardarModelo

El nodo ModelSave guarda modelos entrenados o modificados en el almacenamiento de tu computadora. Toma un modelo como entrada y lo escribe en un archivo con el nombre de archivo que especifiques. Esto te permite conservar tu trabajo y reutilizar modelos en proyectos futuros.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo que se guardará en el disco | MODEL | Sí | - |
| `prefijo_nombre_archivo` | Prefijo de nombre de archivo y ruta para el archivo del modelo guardado (predeterminado: "diffusion_models/ComfyUI") | STRING | Sí | - |
| `prompt` | Información de la solicitud del flujo de trabajo (se proporciona automáticamente) | PROMPT | No | - |
| `extra_pnginfo` | Metadatos adicionales del flujo de trabajo (se proporcionan automáticamente) | EXTRA_PNGINFO | No | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| *Ninguno* | Este nodo no devuelve ningún valor de salida | - |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSave/es.md)

---
**Source fingerprint (SHA-256):** `1dda8a6d85aa19b739c1fe3e6e7f816e05011044fc8b0b91b23fa303f71d8b19`
