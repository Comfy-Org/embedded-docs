Aquí tienes la traducción al español de la documentación, siguiendo todas las reglas establecidas:

## Resumen

Este nodo carga un modelo MediaPipe Face Landmarker v2, que puede detectar rostros y puntos de referencia faciales (como ojos, nariz y boca) en imágenes. Contiene dos variantes de detección (rango corto y rango completo) junto con datos de malla compartidos, formas de mezcla y geometría canónica para el análisis facial.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `model_name` | Modelo de detección facial de models/detection/. | STRING | Sí | Lista de modelos disponibles en el directorio `models/detection/` |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `FACE_DETECTION_MODEL` | Un objeto modelo FaceLandmarker cargado que contiene ambas variantes de detección (corto/completo), conjuntos de conexiones para la topología facial, datos canónicos y parches de modelo para la gestión de GPU. | FACE_DETECTION_MODEL |

**Nota:** La salida es un objeto complejo que puede ser utilizado por otros nodos para tareas de detección facial y extracción de puntos de referencia. Contiene dos variantes de detección: "short" para detección de rango cercano y "full" para detección de rango completo.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadMediaPipeFaceLandmarker/es.md)

---
**Source fingerprint (SHA-256):** `b30bf4d04aa06a227f3661c0e1346d3dab3ea1e25d6627fce5b6480198203c26`
