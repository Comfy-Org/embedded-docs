# Cargador de LTXV Audio VAE

El nodo LTXV Audio VAE Loader carga un modelo de Autoencoder Variacional de Audio (VAE) preentrenado desde un archivo de checkpoint. Lee el checkpoint especificado, carga sus pesos y metadatos, y prepara el modelo para su uso en flujos de trabajo de generación o procesamiento de audio en ComfyUI.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `ckpt_name` | Checkpoint de VAE de audio a cargar. Esta es una lista desplegable completada con todos los archivos encontrados en tu directorio `checkpoints` de ComfyUI. | COMBO | Sí | Todos los archivos en la carpeta `checkpoints`. La lista se genera en tiempo de ejecución. |

El archivo seleccionado debe ser un checkpoint de VAE de audio LTXV válido. El nodo conserva únicamente los pesos del VAE de audio y del vocoder del archivo, y genera un error si el modelo cargado no es un VAE válido.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `Audio VAE` | El modelo de Autoencoder Variacional de Audio cargado, listo para conectarse a otros nodos de procesamiento de audio. | VAE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAELoader/es.md)

---
**Source fingerprint (SHA-256):** `c91956645a9de0b8f56191f6c0c6bef43f13724ba59078ec9a885168bf2650e8`
