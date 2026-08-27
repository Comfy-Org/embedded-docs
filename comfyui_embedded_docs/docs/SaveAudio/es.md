# GuardarAudio

Este nodo guarda datos de audio en un archivo en formato FLAC. Toma una entrada de audio y la escribe en el directorio de salida utilizando el prefijo de nombre de archivo especificado. Este nodo está obsoleto y debe reemplazarse con el nodo Save Audio actual.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `audio` | Los datos de audio que se guardarán | AUDIO | Sí | - |
| `prefijo_nombre_archivo` | El prefijo para el nombre del archivo de salida (por defecto: "audio/ComfyUI") | STRING | No | - |

*Nota: Los parámetros `prompt` y `extra_pnginfo` están ocultos y son manejados automáticamente por el sistema.*

Si la entrada `audio` no recibe datos (por ejemplo, cuando el video de origen no tiene pista de audio), el nodo genera un error y no se guarda ningún archivo.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `audio` | Los datos de audio que se proporcionaron a la entrada, transferidos después de que el archivo se guarda | AUDIO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudio/es.md)

---
**Source fingerprint (SHA-256):** `6ac62d315f14213091cd179a05f0bbd51f1b1a5056bb5c06ca137d2b574d6017`
