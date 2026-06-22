# SDPoseDrawKeypoints

El nodo SDPoseDrawKeypoints toma datos de estimación de pose (puntos clave) y los dibuja como un esqueleto visual sobre un lienzo en blanco. Permite dibujar selectivamente diferentes partes de la pose, como el cuerpo, las manos, el rostro y los pies, con anchos de línea y tamaños de punto personalizables. La imagen resultante puede utilizarse para visualización o como entrada para otros nodos que requieran una imagen de pose.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `puntos clave` | Los datos de puntos clave de la pose que se dibujarán. Estos datos provienen típicamente de un nodo de detección de pose. | POSE_KEYPOINT | Sí | - |
| `dibujar cuerpo` | Controla si se dibuja el esqueleto principal del cuerpo (predeterminado: True). | BOOLEAN | No | - |
| `dibujar manos` | Controla si se dibujan los puntos clave de las manos (predeterminado: True). | BOOLEAN | No | - |
| `dibujar rostro` | Controla si se dibujan los puntos clave del rostro (predeterminado: True). | BOOLEAN | No | - |
| `dibujar pies` | Controla si se dibujan los puntos clave de los pies (predeterminado: False). | BOOLEAN | No | - |
| `ancho de línea` | El ancho de las líneas utilizadas para dibujar el esqueleto del cuerpo (predeterminado: 4). | INT | No | 1 a 10 |
| `tamaño de punto facial` | El tamaño de los puntos utilizados para dibujar los puntos clave del rostro (predeterminado: 3). | INT | No | 1 a 10 |
| `umbral de puntuación` | La puntuación de confianza mínima que debe tener un punto clave para ser dibujado. Los puntos clave con puntuaciones por debajo de este valor se ignoran (predeterminado: 0.3). | FLOAT | No | 0.0 a 1.0 |

**Nota:** Si la entrada `keypoints` está vacía o es `None`, el nodo generará una imagen en blanco de 64x64.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | Una imagen con los puntos clave de la pose dibujados. Las dimensiones de la imagen coinciden con `canvas_height` y `canvas_width` especificados en los datos de puntos clave de entrada. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseDrawKeypoints/es.md)

---
**Source fingerprint (SHA-256):** `c01397ed3608b65b737b60c2ae50919e0217cfe63b3695b68f176c2d69faa9c1`
