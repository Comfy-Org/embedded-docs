# Cargar modelo de escalado Latent

El nodo LatentUpscaleModelLoader carga un modelo especializado en ampliar la escala de representaciones latentes desde un archivo almacenado en la carpeta `latent_upscale_models` de ComfyUI. Detecta automáticamente el tipo de modelo (720p, 1080p u otro upsampler latente) a partir del contenido del archivo y configura la arquitectura interna correspondiente, dejando el modelo cargado listo para ser utilizado por otros nodos.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model_name` | El nombre del archivo de modelo de upscaling latente a cargar. Las opciones disponibles se completan dinámicamente a partir de los archivos presentes en el directorio `latent_upscale_models` de ComfyUI. | COMBO | Sí | Todos los archivos en la carpeta `latent_upscale_models` |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | El modelo de upscaling latente cargado, configurado y listo para usar. | LATENT_UPSCALE_MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscaleModelLoader/es.md)

---
**Source fingerprint (SHA-256):** `7e23214b1b1fc11be84910a5a209c7990a5199120cb0e6b6c61302a442dcf153`
