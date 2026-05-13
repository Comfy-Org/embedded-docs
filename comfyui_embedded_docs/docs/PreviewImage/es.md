> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewImage/es.md)

El nodo PreviewImage está diseñado para crear imágenes de vista previa temporales. Genera automáticamente un nombre de archivo temporal único para cada imagen, comprime la imagen a un nivel especificado y la guarda en un directorio temporal. Esta funcionalidad es particularmente útil para generar vistas previas de imágenes durante el procesamiento sin afectar los archivos originales.

## Entradas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `images`  | `IMAGE`     | La entrada 'images' especifica las imágenes que se procesarán y guardarán como imágenes de vista previa temporales. Esta es la entrada principal del nodo, que determina qué imágenes se someterán al proceso de generación de vista previa. |

## Salidas

El nodo no tiene tipos de salida.