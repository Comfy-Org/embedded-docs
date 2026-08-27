# Cargar MediaPipe Face Landmarker

Load Face Detection Model (MediaPipe)

## Resumen

Este nodo carga un modelo MediaPipe Face Landmarker v2, que puede detectar caras y puntos de referencia faciales (como ojos, nariz y boca) en imágenes. Contiene dos variantes de detección (de corto alcance y de alcance completo) junto con datos de malla compartidos, blendshapes y geometría canónica para el análisis facial.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `model_name` | Modelo de detección facial de models/detection/. | COMBO | Sí | Lista de modelos disponibles en el directorio `models/detection/` |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `FACE_DETECTION_MODEL` | Un objeto de modelo FaceLandmarker cargado que contiene ambas variantes de detección (corta/completa), conjuntos de conexiones para la topología facial, datos canónicos y parches de modelo para la gestión de GPU. | FACE_DETECTION_MODEL |

**Nota:** La salida es un objeto complejo que puede ser utilizado por otros nodos para tareas de detección facial y extracción de puntos de referencia. Contiene dos variantes de detección: «short» para detección de corto alcance y «full» para detección de alcance completo.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadMediaPipeFaceLandmarker/es.md)

---
**Source fingerprint (SHA-256):** `33dda845b572ccffc1bd4b64fb9c338ce4313783b092fe311d89741a211f18c9`
