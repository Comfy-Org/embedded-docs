> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudio/es.md)

El nodo SaveAudio guarda datos de audio en un archivo en formato FLAC. Toma una entrada de audio y la escribe en el directorio de salida especificado con el prefijo de nombre de archivo dado. El nodo maneja automáticamente la nomenclatura de archivos y asegura que el audio se guarde correctamente para su uso posterior.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Sí | - | Los datos de audio que se van a guardar |
| `prefijo_nombre_archivo` | STRING | No | - | El prefijo para el nombre del archivo de salida (por defecto: "audio/ComfyUI") |

*Nota: Los parámetros `prompt` y `extra_pnginfo` están ocultos y son manejados automáticamente por el sistema.*

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| *Ninguno* | - | Este nodo no devuelve ningún dato de salida, pero guarda el archivo de audio en el directorio de salida |