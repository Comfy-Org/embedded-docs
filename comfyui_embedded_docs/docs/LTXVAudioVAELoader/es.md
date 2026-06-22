# Cargador de LTXV Audio VAE

El nodo Cargador de VAE de Audio LTXV carga un modelo de Autoencoder Variacional (VAE) de audio preentrenado desde un archivo de punto de control. Lee el punto de control especificado, carga sus pesos y metadatos, y prepara el modelo para su uso en flujos de trabajo de generación o procesamiento de audio dentro de ComfyUI.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `ckpt_name` | Punto de control de VAE de audio a cargar. Esta es una lista desplegable que se completa con todos los archivos encontrados en tu directorio `checkpoints` de ComfyUI. | STRING | Sí | Todos los archivos en la carpeta `checkpoints`.<br>*Ejemplo: `"audio_vae.safetensors"`* |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `Audio VAE` | El modelo de Autoencoder Variacional de audio cargado, listo para conectarse a otros nodos de procesamiento de audio. | VAE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAELoader/es.md)

---
**Source fingerprint (SHA-256):** `44e79f694eed796a83f3ac25c56946baaa12b016568bd8824eb179bf79e50588`
