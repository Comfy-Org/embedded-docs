> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageSetNode/es.md)

El LoadImageSetNode carga múltiples imágenes desde el directorio de entrada para procesamiento por lotes y fines de entrenamiento. Soporta varios formatos de imagen y puede opcionalmente redimensionar las imágenes usando diferentes métodos. Este nodo procesa todas las imágenes seleccionadas como un lote y las devuelve como un solo tensor.

## Entradas

| Parámetro | Tipo de Datos | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Sí | Múltiples archivos de imagen | Selecciona múltiples imágenes del directorio de entrada. Soporta formatos PNG, JPG, JPEG, WEBP, BMP, GIF, JPE, APNG, TIF y TIFF. Permite selección por lotes de imágenes. |
| `resize_method` | STRING | No | "None"<br>"Stretch"<br>"Crop"<br>"Pad" | Método opcional para redimensionar las imágenes cargadas (por defecto: "None"). Elige "None" para mantener tamaños originales, "Stretch" para forzar el redimensionado, "Crop" para mantener la relación de aspecto recortando, o "Pad" para mantener la relación de aspecto añadiendo relleno. |

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | Un tensor que contiene todas las imágenes cargadas como un lote para su posterior procesamiento. |
