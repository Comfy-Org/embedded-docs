> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageSetFromFolderNode/es.md)

El LoadImageSetFromFolderNode carga múltiples imágenes desde una carpeta específica para fines de entrenamiento. Detecta automáticamente formatos de imagen comunes y puede opcionalmente redimensionar las imágenes usando diferentes métodos antes de devolverlas como un lote.

## Entradas

| Parámetro | Tipo de Datos | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `folder` | STRING | Sí | Múltiples opciones disponibles | La carpeta desde la cual cargar las imágenes. |
| `resize_method` | STRING | No | "None"<br>"Stretch"<br>"Crop"<br>"Pad" | El método a utilizar para redimensionar las imágenes (por defecto: "None"). |

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | El lote de imágenes cargadas como un solo tensor. |
