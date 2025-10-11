> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetImageSize/es.md)

El nodo GetImageSize extrae las dimensiones e información de lote de una imagen de entrada. Devuelve el ancho, alto y tamaño del lote de la imagen, mientras también muestra esta información como texto de progreso en la interfaz del nodo. Los datos originales de la imagen pasan sin cambios.

## Entradas

| Parámetro | Tipo de Datos | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen de entrada de la cual extraer la información de tamaño |
| `unique_id` | UNIQUE_ID | No | - | Identificador interno utilizado para mostrar información de progreso |

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|-------------|-----------|-------------|
| `width` | INT | El ancho de la imagen de entrada en píxeles |
| `height` | INT | La altura de la imagen de entrada en píxeles |
| `batch_size` | INT | El número de imágenes en el lote |