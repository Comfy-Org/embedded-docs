> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioMP3/es.md)

El nodo SaveAudioMP3 guarda datos de audio como un archivo MP3. Toma una entrada de audio y la exporta al directorio de salida especificado con opciones personalizables de nombre de archivo y calidad. El nodo maneja automáticamente la asignación de nombres de archivo y la conversión de formato para crear un archivo MP3 reproducible.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `audio` | AUDIO | Sí | - | Los datos de audio que se guardarán como archivo MP3 |
| `prefijo_nombre_archivo` | STRING | No | - | El prefijo para el nombre del archivo de salida (predeterminado: "audio/ComfyUI") |
| `calidad` | STRING | No | "V0"<br>"128k"<br>"320k" | La configuración de calidad de audio para el archivo MP3 (predeterminado: "V0") |
| `prompt` | PROMPT | No | - | Datos internos de la instrucción (proporcionados automáticamente por el sistema) |
| `extra_pnginfo` | EXTRA_PNGINFO | No | - | Información adicional PNG (proporcionada automáticamente por el sistema) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| *Ninguno* | - | Este nodo no devuelve ningún dato de salida, pero guarda el archivo de audio en el directorio de salida |

---
**Source fingerprint (SHA-256):** `70b960cc9c86ad9a4c98e643f40e6caaafdeb9840ac72a5f8e59533fd6120e3e`
