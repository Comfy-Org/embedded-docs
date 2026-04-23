> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseDrawKeypoints/es.md)

El nodo SDPoseDrawKeypoints toma datos de estimación de pose (puntos clave) y los dibuja como un esqueleto visual sobre un lienzo en blanco. Permite dibujar selectivamente diferentes partes de la pose, como el cuerpo, las manos, la cara y los pies, con anchos de línea y tamaños de punto personalizables. La imagen resultante puede usarse para visualización o como entrada para otros nodos que requieran una imagen de pose.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `keypoints` | POSE_KEYPOINT | Sí | - | Los datos de puntos clave de la pose que se dibujarán. Estos datos suelen provenir de un nodo de detección de pose. |
| `draw_body` | BOOLEAN | No | - | Controla si se dibuja el esqueleto principal del cuerpo (valor por defecto: True). |
| `draw_hands` | BOOLEAN | No | - | Controla si se dibujan los puntos clave de las manos (valor por defecto: True). |
| `draw_face` | BOOLEAN | No | - | Controla si se dibujan los puntos clave de la cara (valor por defecto: True). |
| `draw_feet` | BOOLEAN | No | - | Controla si se dibujan los puntos clave de los pies (valor por defecto: False). |
| `stick_width` | INT | No | 1 a 10 | El ancho de las líneas utilizadas para dibujar el esqueleto del cuerpo (valor por defecto: 4). |
| `face_point_size` | INT | No | 1 a 10 | El tamaño de los puntos utilizados para dibujar los puntos clave de la cara (valor por defecto: 3). |
| `score_threshold` | FLOAT | No | 0.0 a 1.0 | La puntuación de confianza mínima que debe tener un punto clave para ser dibujado. Los puntos clave con puntuaciones inferiores a este valor se ignoran (valor por defecto: 0.3). |

**Nota:** Si la entrada `keypoints` está vacía o es `None`, el nodo generará una imagen en blanco de 64x64.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | IMAGE | Una imagen con los puntos clave de la pose dibujados. Las dimensiones de la imagen coinciden con `canvas_height` y `canvas_width` especificados en los datos de puntos clave de entrada. |