> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointSave/es.md)

El nodo ImageOnlyCheckpointSave guarda un archivo de checkpoint que contiene un modelo, codificador CLIP de visión y VAE. Crea un archivo safetensors con el prefijo de nombre de archivo especificado y lo almacena en el directorio de salida. Este nodo está diseñado específicamente para guardar componentes de modelo relacionados con imágenes juntos en un único archivo de checkpoint.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `modelo` | MODEL | Sí | - | El modelo que se guardará en el checkpoint |
| `clip_vision` | CLIP_VISION | Sí | - | El codificador CLIP de visión que se guardará en el checkpoint |
| `vae` | VAE | Sí | - | El VAE (Autoencoder Variacional) que se guardará en el checkpoint |
| `prefijo_nombre_archivo` | STRING | Sí | - | El prefijo para el nombre del archivo de salida (predeterminado: "checkpoints/ComfyUI") |
| `prompt` | PROMPT | No | - | Parámetro oculto para datos de prompt del flujo de trabajo |
| `extra_pnginfo` | EXTRA_PNGINFO | No | - | Parámetro oculto para metadatos PNG adicionales |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| - | - | Este nodo no devuelve ninguna salida |

---
**Source fingerprint (SHA-256):** `d2a26933f0e2fcccf3c57f50038fb40ef5b23d00ccdd2e1d215b3cb78203b9fd`
