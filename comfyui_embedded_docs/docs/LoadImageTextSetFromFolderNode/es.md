> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageTextSetFromFolderNode/es.md)

Carga un lote de imágenes y sus correspondientes textos descriptivos desde un directorio específico para fines de entrenamiento. El nodo busca automáticamente archivos de imagen y sus archivos de texto de descripción asociados, procesa las imágenes según la configuración de redimensionado especificada y codifica las descripciones utilizando el modelo CLIP proporcionado.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `folder` | STRING | Sí | - | La carpeta desde la cual cargar las imágenes. |
| `clip` | CLIP | Sí | - | El modelo CLIP utilizado para codificar el texto. |
| `resize_method` | COMBO | No | "None"<br>"Stretch"<br>"Crop"<br>"Pad" | El método utilizado para redimensionar las imágenes (valor por defecto: "None"). |
| `width` | INT | No | -1 a 10000 | El ancho al que redimensionar las imágenes. -1 significa usar el ancho original (valor por defecto: -1). |
| `height` | INT | No | -1 a 10000 | La altura a la que redimensionar las imágenes. -1 significa usar la altura original (valor por defecto: -1). |

**Nota:** La entrada CLIP debe ser válida y no puede ser None. Si el modelo CLIP proviene de un nodo cargador de checkpoint, asegúrese de que el checkpoint contenga un modelo CLIP o codificador de texto válido.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | El lote de imágenes cargadas y procesadas. |
| `CONDITIONING` | CONDITIONING | Los datos de condicionamiento codificados a partir de los textos descriptivos. |
