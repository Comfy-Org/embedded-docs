# SDPoseDrawKeypoints

El nodo SDPoseDrawKeypoints toma datos de estimación de pose (puntos clave) y los dibuja como un esqueleto visual sobre un lienzo en blanco. Permite dibujar selectivamente diferentes partes de la pose, como el cuerpo, la cabeza, las manos, la cara y los pies, con grosores de línea y tamaños de punto personalizables. La imagen resultante se puede utilizar para visualización o como entrada para otros nodos que requieran una imagen de pose.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `keypoints` | Los datos de puntos clave de pose que se van a dibujar. Estos datos normalmente provienen de un nodo de detección de pose. | POSE_KEYPOINT | Sí | - |
| `draw_body` | Controla si se dibuja el esqueleto principal del cuerpo (valor predeterminado: True). | BOOLEAN | No | - |
| `draw_hands` | Controla si se dibujan los puntos clave de las manos (valor predeterminado: True). | BOOLEAN | No | - |
| `draw_face` | Controla si se dibujan los puntos clave de la cara (valor predeterminado: True). | BOOLEAN | No | - |
| `draw_feet` | Controla si se dibujan los puntos clave de los pies (valor predeterminado: False). | BOOLEAN | No | - |
| `stick_width` | El grosor de las líneas utilizadas para dibujar el esqueleto del cuerpo (valor predeterminado: 4). | INT | No | 1 a 10 |
| `face_point_size` | El tamaño de los puntos utilizados para dibujar los puntos clave de la cara (valor predeterminado: 3). | INT | No | 1 a 10 |
| `score_threshold` | La puntuación de confianza mínima que debe tener un punto clave para ser dibujado. Los puntos clave con puntuaciones por debajo de este valor se ignoran (valor predeterminado: 0.3). | FLOAT | No | 0.0 a 1.0 |
| `draw_head` | Controla si se dibujan los puntos clave de la cabeza (nariz, ojos, oídos) y las conexiones de la cabeza (valor predeterminado: True). | BOOLEAN | No | - |

**Nota:** Si la entrada `keypoints` está vacía o es `None`, el nodo generará una imagen en blanco de 64x64.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `output` | Una imagen con los puntos clave de pose dibujados. Las dimensiones de la imagen coinciden con el `canvas_height` y `canvas_width` especificados en los datos de puntos clave de entrada. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseDrawKeypoints/es.md)

---
**Source fingerprint (SHA-256):** `2b2b9530b55c56e278666bd5d139bb6a1bb503b75b948a89266b9982b5a295e4`
