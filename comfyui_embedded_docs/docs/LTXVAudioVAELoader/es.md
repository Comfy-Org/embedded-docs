> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAELoader/es.md)

El nodo LTXV Audio VAE Loader carga un modelo preentrenado de Autoencoder Variacional (VAE) para audio desde un archivo de checkpoint. Lee el checkpoint especificado, carga sus pesos y metadatos, y prepara el modelo para su uso en flujos de trabajo de generación o procesamiento de audio dentro de ComfyUI.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `ckpt_name` | STRING | Sí | Todos los archivos en la carpeta `checkpoints`.<br>*Ejemplo: `"audio_vae.safetensors"`* | Checkpoint del VAE de audio a cargar. Es una lista desplegable poblada con todos los archivos encontrados en tu directorio `checkpoints` de ComfyUI. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `Audio VAE` | VAE | El modelo de Autoencoder Variacional para audio cargado, listo para ser conectado a otros nodos de procesamiento de audio. |
