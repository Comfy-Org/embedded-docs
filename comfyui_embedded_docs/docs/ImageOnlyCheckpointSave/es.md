El nodo ImageOnlyCheckpointSave guarda un archivo de checkpoint que contiene un modelo, codificador CLIP de visión y VAE. Crea un archivo safetensors con el prefijo de nombre de archivo especificado y lo almacena en el directorio de salida. Este nodo está diseñado específicamente para guardar componentes de modelo relacionados con imágenes juntos en un único archivo de checkpoint.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo que se guardará en el checkpoint | MODEL | Sí | - |
| `clip_vision` | El codificador CLIP de visión que se guardará en el checkpoint | CLIP_VISION | Sí | - |
| `vae` | El VAE (Autoencoder Variacional) que se guardará en el checkpoint | VAE | Sí | - |
| `prefijo_nombre_archivo` | El prefijo para el nombre del archivo de salida (predeterminado: "checkpoints/ComfyUI") | STRING | Sí | - |
| `prompt` | Parámetro oculto para datos de prompt del flujo de trabajo | PROMPT | No | - |
| `extra_pnginfo` | Parámetro oculto para metadatos PNG adicionales | EXTRA_PNGINFO | No | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| - | Este nodo no devuelve ninguna salida | - |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointSave/es.md)

---
**Source fingerprint (SHA-256):** `d2a26933f0e2fcccf3c57f50038fb40ef5b23d00ccdd2e1d215b3cb78203b9fd`
