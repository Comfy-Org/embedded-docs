# GuardarAudio

El nodo SaveAudio guarda datos de audio en un archivo en formato FLAC. Toma una entrada de audio, la escribe en el directorio de salida utilizando el prefijo de nombre de archivo especificado y pasa el mismo audio como salida. Este nodo está obsoleto y debe reemplazarse con el nodo Save Audio actual.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `audio` | Los datos de audio que se van a guardar | AUDIO | Sí | - |
| `filename_prefix` | El prefijo para el nombre del archivo de salida (predeterminado: "audio/ComfyUI") | STRING | No | - |

El nodo genera un error si `audio` es None, lo que puede ocurrir cuando el video de origen no tiene pista de audio.

Los parámetros `prompt` y `extra_pnginfo` están ocultos y son manejados automáticamente por el sistema.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `audio` | Los mismos datos de audio que se guardaron en el archivo | AUDIO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudio/es.md)

---
**Source fingerprint (SHA-256):** `6ac62d315f14213091cd179a05f0bbd51f1b1a5056bb5c06ca137d2b574d6017`
