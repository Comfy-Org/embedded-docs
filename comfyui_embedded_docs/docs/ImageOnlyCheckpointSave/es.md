# GuardarPuntoDeControlSoloDeImagen

El nodo `ImageOnlyCheckpointSave` guarda un archivo de checkpoint que contiene un modelo, un codificador de visión CLIP y un VAE. Crea un archivo safetensors con el prefijo de nombre especificado y lo almacena en el directorio de salida. Este nodo está diseñado específicamente para guardar componentes de modelo relacionados con imágenes en un único archivo de checkpoint.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo que se guardará en el checkpoint | MODEL | Sí | - |
| `clip_vision` | El codificador de visión CLIP que se guardará en el checkpoint | CLIP_VISION | Sí | - |
| `vae` | El VAE (Autoencoder Variacional) que se guardará en el checkpoint | VAE | Sí | - |
| `prefijo_nombre_archivo` | El prefijo para el nombre del archivo de salida (predeterminado: "checkpoints/ComfyUI") | STRING | Sí | - |
| `prompt` | Parámetro oculto para los datos de prompt del flujo de trabajo | PROMPT | No | - |
| `extra_pnginfo` | Metadatos PNG adicionales | EXTRA_PNGINFO | No | - |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| - | Este nodo no devuelve ninguna salida | - |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointSave/es.md)

---
**Source fingerprint (SHA-256):** `8ff4b3a78d8da523eaa5f784f847e954ba73b4d6037e748dcce592b447fcdee9`
