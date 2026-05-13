> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseFaceBBoxes/es.md)

El nodo SDPoseFaceBBoxes procesa datos de puntos clave de pose para detectar y generar cuadros delimitadores alrededor de rostros humanos. Analiza los puntos clave faciales 2D de cada persona en un fotograma, calcula un cuadro delimitador basado en esos puntos y puede ajustar el tamaño y la forma del cuadro. Los cuadros delimitadores resultantes se formatean para ser compatibles con otros nodos en el flujo de trabajo SDPose, como el SDPoseKeypointExtractor.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|--------------|-----------|-------|-------------|
| `keypoints` | POSE_KEYPOINT | Sí | - | Datos de puntos clave de pose que contienen información sobre personas detectadas y sus puntos de referencia corporales/faciales por fotograma. |
| `scale` | FLOAT | No | 1.0 - 10.0 | Multiplicador del área del cuadro delimitador alrededor de cada rostro detectado. Un valor más grande crea un cuadro más grande. (predeterminado: 1.5) |
| `force_square` | BOOLEAN | No | - | Expande el eje más corto del cuadro delimitador para que la región de recorte sea siempre cuadrada. (predeterminado: True) |

**Nota:** La entrada `keypoints` debe estar en el formato específico producido por nodos como SDPoseKeypointExtractor, que contiene datos de `canvas_height`, `canvas_width` y `people` con `face_keypoints_2d` para cada persona.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `bboxes` | BOUNDINGBOX | Una lista de cuadros delimitadores faciales para cada fotograma. Cada cuadro delimitador se define por sus coordenadas de esquina superior izquierda (`x`, `y`), `width` (ancho) y `height` (alto). Esta salida es compatible con la entrada `bboxes` del nodo SDPoseKeypointExtractor. |

---
**Source fingerprint (SHA-256):** `bffbcddb882f6743a6cace6a4884fa5a257b746897c79ba9260c15260fab874e`
