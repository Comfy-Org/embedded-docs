# Guardar audio (Opus)

El nodo SaveAudioOpus guarda datos de audio en un archivo en formato Opus. Toma una entrada de audio y la exporta como un archivo Opus comprimido con ajustes de calidad configurables. Este nodo está obsoleto y puede eliminarse en versiones futuras.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `audio` | Los datos de audio que se guardarán como archivo Opus. Se genera un ValueError si esto es None (por ejemplo, cuando el video de origen no tiene pista de audio). | AUDIO | Sí | - |
| `prefijo_nombre_archivo` | El prefijo para el nombre del archivo de salida (predeterminado: "audio/ComfyUI") | STRING | No | - |
| `calidad` | La tasa de bits utilizada para codificar el archivo Opus; los valores más altos producen mejor calidad pero archivos más grandes (predeterminado: "128k") | COMBO | No | "64k"<br>"96k"<br>"128k"<br>"192k"<br>"320k" |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `audio` | Los datos de audio que se guardaron en el archivo Opus | AUDIO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioOpus/es.md)

---
**Source fingerprint (SHA-256):** `a2f585f45299759738fa85f6b73f51680d4e86da57d3fc9c2236e66114fa3d6c`
