> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAudio/es.md)

El nodo PreviewAudio genera un archivo de vista previa de audio temporal que puede mostrarse en la interfaz. Hereda de SaveAudio pero guarda los archivos en un directorio temporal con un prefijo de nombre de archivo aleatorio. Esto permite a los usuarios previsualizar rápidamente las salidas de audio sin crear archivos permanentes.

## Entradas

| Parámetro | Tipo de Datos | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Sí | - | Los datos de audio para previsualizar |
| `prompt` | PROMPT | No | - | Parámetro oculto para uso interno |
| `extra_pnginfo` | EXTRA_PNGINFO | No | - | Parámetro oculto para uso interno |

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|-------------|-----------|-------------|
| `ui` | UI | Muestra la vista previa del audio en la interfaz |
