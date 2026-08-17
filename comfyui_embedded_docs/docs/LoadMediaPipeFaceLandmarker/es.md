# Cargar MediaPipe Face Landmarker

Este nodo carga un modelo MediaPipe Face Landmarker v2, que puede detectar rostros y puntos de referencia faciales (como ojos, nariz y boca) en imágenes. El modelo cargado contiene dos variantes de detección (corta y completa), junto con datos de malla compartidos, blendshapes y geometría canónica para el análisis facial.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `model_name` | Modelo de detección facial de models/detection/. | COMBO | Sí | Lista de modelos disponibles en el directorio `models/detection/` |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `FACE_DETECTION_MODEL` | Un objeto de modelo MediaPipe Face Landmarker cargado que contiene ambas variantes de detección (corta/completa), datos de malla y blendshapes compartidos, geometría canónica, conjuntos de conexiones de topología facial y parches de modelo para la gestión de GPU. | FACE_DETECTION_MODEL |

**Nota:** La salida es un objeto complejo que puede ser utilizado por otros nodos para tareas de detección facial y extracción de puntos de referencia. Contiene dos variantes de detección: "short" para detección de corto alcance y "full" para detección de rango completo.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadMediaPipeFaceLandmarker/es.md)

---
**Source fingerprint (SHA-256):** `33dda845b572ccffc1bd4b64fb9c338ce4313783b092fe311d89741a211f18c9`
