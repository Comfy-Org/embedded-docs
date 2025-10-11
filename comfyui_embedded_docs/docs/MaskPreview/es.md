> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskPreview/es.md)

El nodo MaskPreview genera una vista previa visual de una máscara convirtiéndola a un formato de imagen de 3 canales y guardándola como un archivo temporal. Toma una máscara de entrada y la remodela a un formato adecuado para visualización de imágenes, luego guarda el resultado en el directorio temporal con un prefijo de nombre de archivo aleatorio. Esto permite a los usuarios inspeccionar visualmente los datos de máscara durante la ejecución del flujo de trabajo.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `mask` | MASK | Sí | - | Los datos de máscara que se previsualizarán y convertirán a formato de imagen |
| `filename_prefix` | STRING | No | - | Prefijo para el nombre del archivo de salida (por defecto: "ComfyUI") |
| `prompt` | PROMPT | No | - | Información del prompt para metadatos (proporcionada automáticamente) |
| `extra_pnginfo` | EXTRA_PNGINFO | No | - | Información PNG adicional para metadatos (proporcionada automáticamente) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `ui` | DICT | Contiene la información de la imagen de vista previa y los metadatos para visualización |