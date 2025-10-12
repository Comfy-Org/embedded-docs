> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveWEBM/es.md)

El nodo SaveWEBM guarda una secuencia de imágenes como un archivo de video WEBM. Toma múltiples imágenes de entrada y las codifica en un video utilizando códec VP9 o AV1 con configuraciones de calidad y velocidad de cuadros ajustables. El archivo de video resultante se guarda en el directorio de salida con metadatos que incluyen información del prompt.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `imágenes` | IMAGE | Sí | - | Secuencia de imágenes de entrada para codificar como cuadros de video |
| `prefijo_nombre_archivo` | STRING | No | - | Prefijo para el nombre del archivo de salida (predeterminado: "ComfyUI") |
| `códec` | COMBO | Sí | "vp9"<br>"av1" | Códec de video a utilizar para la codificación |
| `fps` | FLOAT | No | 0.01-1000.0 | Velocidad de cuadros para el video de salida (predeterminado: 24.0) |
| `crf` | FLOAT | No | 0-63.0 | Configuración de calidad donde un crf más alto significa menor calidad con tamaño de archivo más pequeño, y un crf más bajo significa mayor calidad con tamaño de archivo más grande (predeterminado: 32.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `ui` | PREVIEW | Vista previa del video que muestra el archivo WEBM guardado |