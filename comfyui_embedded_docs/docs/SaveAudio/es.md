> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudio/es.md)

El nodo SaveAudio guarda datos de audio en un archivo en formato FLAC. Toma una entrada de audio y la escribe en el directorio de salida especificado con el prefijo de nombre de archivo indicado. El nodo maneja automáticamente la nomenclatura de archivos y garantiza que el audio se guarde correctamente para su uso posterior.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `audio` | AUDIO | Sí | - | Los datos de audio que se guardarán |
| `filename_prefix` | STRING | No | - | El prefijo para el nombre del archivo de salida (predeterminado: "audio/ComfyUI") |

*Nota: Los parámetros `prompt` y `extra_pnginfo` están ocultos y son manejados automáticamente por el sistema.*

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| *Ninguno* | - | Este nodo no devuelve ningún dato de salida, pero guarda el archivo de audio en el directorio de salida |

---
**Source fingerprint (SHA-256):** `16242dfc45d0f2808a5615e9c1bfe4de4d19e2f5f6b28370f631439021dc72e5`
