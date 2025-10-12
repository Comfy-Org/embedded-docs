> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLatent/es.md)

El nodo SaveLatent guarda tensores latentes en el disco como archivos para su uso posterior o compartir. Toma muestras latentes y las guarda en el directorio de salida con metadatos opcionales que incluyen información del prompt. El nodo maneja automáticamente la nomenclatura y organización de archivos mientras preserva la estructura de datos latentes.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `muestras` | LATENT | Sí | - | Las muestras latentes que se guardarán en el disco |
| `prefijo_nombre_archivo` | STRING | No | - | El prefijo para el nombre del archivo de salida (por defecto: "latents/ComfyUI") |
| `prompt` | PROMPT | No | - | Información del prompt para incluir en los metadatos (parámetro oculto) |
| `extra_pnginfo` | EXTRA_PNGINFO | No | - | Información PNG adicional para incluir en los metadatos (parámetro oculto) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `ui` | UI | Proporciona información de ubicación del archivo para el latente guardado en la interfaz de ComfyUI |
