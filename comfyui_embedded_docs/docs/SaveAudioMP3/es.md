# Guardar Audio (MP3)

El nodo SaveAudioMP3 guarda los datos de audio como un archivo MP3. Toma una entrada de audio y la exporta al directorio de salida con configuración de nombre de archivo y calidad personalizables, manejando automáticamente la nomenclatura del archivo y la conversión al formato MP3. **Este nodo está obsoleto y puede eliminarse en versiones futuras.**

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `audio` | Los datos de audio que se guardarán como un archivo MP3 | AUDIO | Sí | - |
| `prefijo_nombre_archivo` | El prefijo para el nombre del archivo de salida (por defecto: "audio/ComfyUI") | STRING | No | - |
| `calidad` | La configuración de calidad de audio para el archivo MP3 (por defecto: "V0") | COMBO | No | `"V0"`<br>`"128k"`<br>`"320k"` |
| `prompt` | Datos internos del prompt, proporcionados automáticamente por el sistema | PROMPT | No | - |
| `extra_pnginfo` | Información adicional de PNG, proporcionada automáticamente por el sistema | EXTRA_PNGINFO | No | - |

**Nota:** Si la entrada `audio` es None (por ejemplo, cuando el video de origen no tiene pista de audio), el nodo genera un ValueError.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `audio` | Los datos de audio que se guardaron en un archivo MP3 | AUDIO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioMP3/es.md)

---
**Source fingerprint (SHA-256):** `7d3b439dfd7cb211dd6568f6b5124bb225909dcf0ae150addc4ca226d947a4f0`
