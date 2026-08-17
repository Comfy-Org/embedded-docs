# Guardar audio (Opus)

El nodo SaveAudioOpus guarda datos de audio en un archivo con formato Opus. Toma una entrada de audio y la exporta como un archivo Opus comprimido con ajustes de calidad configurables. Este nodo está obsoleto y podría eliminarse en versiones futuras.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `audio` | Los datos de audio que se guardarán como archivo Opus. El nodo genera un error si no se proporciona audio (por ejemplo, cuando el video de origen no tiene pista de audio). | AUDIO | Sí | - |
| `filename_prefix` | El prefijo para el nombre del archivo de salida (predeterminado: "audio/ComfyUI") | STRING | No | - |
| `quality` | El ajuste de calidad de audio (tasa de bits) para el archivo Opus (predeterminado: "128k") | COMBO | No | "64k"<br>"96k"<br>"128k"<br>"192k"<br>"320k" |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `audio` | Los datos de audio de entrada, devueltos después de que el archivo Opus se guarda en el disco. | AUDIO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioOpus/es.md)

---
**Source fingerprint (SHA-256):** `a2f585f45299759738fa85f6b73f51680d4e86da57d3fc9c2236e66114fa3d6c`
