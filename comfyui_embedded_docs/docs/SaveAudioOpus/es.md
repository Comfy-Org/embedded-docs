> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioOpus/es.md)

El nodo SaveAudioOpus guarda datos de audio en un archivo en formato Opus. Toma una entrada de audio y la exporta como un archivo Opus comprimido con configuraciones de calidad ajustables. El nodo maneja automáticamente la nomenclatura de archivos y guarda la salida en el directorio de salida designado.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Sí | - | Los datos de audio que se guardarán como archivo Opus |
| `filename_prefix` | STRING | No | - | El prefijo para el nombre del archivo de salida (por defecto: "audio/ComfyUI") |
| `quality` | COMBO | No | "64k"<br>"96k"<br>"128k"<br>"192k"<br>"320k" | La configuración de calidad de audio para el archivo Opus (por defecto: "128k") |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| - | - | Este nodo no devuelve ningún valor de salida. Su función principal es guardar el archivo de audio en el disco. |
