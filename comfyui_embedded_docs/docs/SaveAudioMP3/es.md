# Guardar Audio (MP3)

El nodo SaveAudioMP3 guarda datos de audio como un archivo MP3. Recibe una entrada de audio y la escribe en el directorio de salida con un prefijo de nombre de archivo personalizable y una configuración de calidad. Este nodo está obsoleto y puede eliminarse en versiones futuras.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `audio` | Los datos de audio que se guardarán como archivo MP3 | AUDIO | Sí | - |
| `filename_prefix` | El prefijo para el nombre de archivo de salida (predeterminado: "audio/ComfyUI") | STRING | No | - |
| `quality` | La configuración de calidad de codificación MP3 (predeterminado: "V0"). V0 utiliza bitrate variable para alta calidad; 128k y 320k utilizan bitrates fijos de 128 y 320 kbps | COMBO | No | `"V0"`<br>`"128k"`<br>`"320k"` |
| `prompt` | Datos internos del prompt, proporcionados automáticamente por el sistema | PROMPT | No | - |
| `extra_pnginfo` | Información adicional de PNG, proporcionada automáticamente por el sistema | EXTRA_PNGINFO | No | - |

**Nota:** Si la entrada `audio` es None (por ejemplo, cuando el video de origen no tiene pista de audio), el nodo lanza un ValueError.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `audio` | Los datos de audio que se guardaron como archivo MP3 | AUDIO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioMP3/es.md)

---
**Source fingerprint (SHA-256):** `7d3b439dfd7cb211dd6568f6b5124bb225909dcf0ae150addc4ca226d947a4f0`
