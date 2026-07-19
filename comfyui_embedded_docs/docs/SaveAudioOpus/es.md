# Guardar audio (Opus)

El nodo SaveAudioOpus guarda datos de audio en un archivo en formato Opus. Toma una entrada de audio y la exporta como un archivo Opus comprimido con ajustes de calidad configurables. El nodo maneja automáticamente el nombre del archivo y guarda la salida en el directorio de salida designado.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `audio` | Los datos de audio que se guardarán como archivo Opus | AUDIO | Sí | - |
| `prefijo_nombre_archivo` | El prefijo para el nombre del archivo de salida (predeterminado: "audio/ComfyUI") | STRING | No | - |
| `calidad` | El ajuste de calidad de audio para el archivo Opus (predeterminado: "128k") | COMBO | No | "64k"<br>"96k"<br>"128k"<br>"192k"<br>"320k" |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| - | Este nodo no devuelve ningún valor de salida. Su función principal es guardar el archivo de audio en el disco. | - |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioOpus/es.md)

---
**Source fingerprint (SHA-256):** `87c3b1b85ca51b79d43c8486eeb2de7b074faa11c4da2bff7b8931a3049560e2`
