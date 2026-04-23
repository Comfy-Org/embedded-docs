> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseKeypointExtractor/es.md)

El nodo SDPoseKeypointExtractor detecta puntos clave de postura humana en imágenes de entrada utilizando el modelo SDPose. Puede procesar imágenes completas o regiones específicas definidas por cuadros delimitadores y genera los puntos clave detectados en formato OpenPose, que incluye las coordenadas para cada persona y una puntuación de confianza para cada punto clave.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo SDPose utilizado para la detección de puntos clave. Debe ser un modelo con un atributo `heatmap_head`, específicamente del repositorio SDPose. |
| `vae` | VAE | Sí | - | El modelo VAE utilizado para codificar las imágenes de entrada en el espacio latente para su procesamiento. |
| `image` | IMAGE | Sí | - | La imagen de entrada o lote de imágenes de las cuales extraer los puntos clave de postura. |
| `batch_size` | INT | No | 1 a 10000 | El número de imágenes a procesar simultáneamente cuando se ejecuta en modo de imagen completa (es decir, cuando no se proporciona `bboxes`). Esto puede acelerar el procesamiento. (predeterminado: 16) |
| `bboxes` | BOUNDINGBOX | No | - | Cuadros delimitadores opcionales para detecciones más precisas. Requerido para la detección de múltiples personas. Si se proporciona, el nodo extraerá los puntos clave de cada región especificada. |

**Restricciones de Parámetros:**
*   La entrada `model` debe ser un modelo SDPose específico. Si el modelo proporcionado no tiene un atributo `heatmap_head`, el nodo generará un error.
*   El nodo opera en dos modos distintos según la entrada `bboxes`:
    1.  **Modo Cuadro Delimitador:** Cuando se proporciona `bboxes`, procesa cada región especificada individualmente. Esto es necesario para detectar múltiples personas en una sola imagen.
    2.  **Modo Imagen Completa:** Cuando no se proporciona `bboxes`, procesa toda la imagen como un lote. El parámetro `batch_size` solo se aplica en este modo.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `keypoints` | POSE_KEYPOINT | Puntos clave en formato de cuadro OpenPose (canvas_width, canvas_height, people). La salida contiene las personas detectadas, cada una con un arreglo de coordenadas de puntos clave (x, y) y sus puntuaciones de confianza correspondientes. |