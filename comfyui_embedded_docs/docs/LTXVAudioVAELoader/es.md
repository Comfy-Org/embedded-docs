# Cargador de LTXV Audio VAE

El nodo **LTXV Audio VAE Loader** carga un modelo de Autoencoder Variacional de Audio (VAE) preentrenado desde un archivo de checkpoint. Lee el checkpoint especificado, carga sus pesos y metadatos, y prepara el modelo para su uso en flujos de trabajo de generación o procesamiento de audio dentro de ComfyUI.

## Entradas

| Parámetro | Descripción | Tipo de datos | ¿Requerido? | Rango |
| --- | --- | --- | --- | --- |
| `ckpt_name` | Checkpoint de VAE de audio a cargar. Esta es una lista desplegable poblada con todos los archivos encontrados en el directorio `checkpoints` de tu ComfyUI. | COMBO | Sí | Todos los archivos en la carpeta `checkpoints` (poblada dinámicamente).<br>*Ejemplo: `"audio_vae.safetensors"`* |

Nota: El nodo genera un error si el archivo de checkpoint seleccionado no se encuentra o no contiene un VAE de audio válido.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `Audio VAE` | El modelo de Autoencoder Variacional de Audio cargado, listo para ser conectado a otros nodos de procesamiento de audio. | VAE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAELoader/es.md)

---
**Source fingerprint (SHA-256):** `c91956645a9de0b8f56191f6c0c6bef43f13724ba59078ec9a885168bf2650e8`
