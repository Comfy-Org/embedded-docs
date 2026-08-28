# Pixal3DConditioning

Este nodo prepara el condicionamiento de imagen para el pipeline de generación 3D Trellis2. Extrae características visuales de la imagen de entrada con un modelo de visión DINOv3 a dos resoluciones, las organiza en mapas de características por etapa (opcionalmente mejorados con un modelo NAF) y las combina con datos de cámara derivados del campo de visión horizontal. Produce un par de condicionamiento positivo y negativo, donde el negativo utiliza características a cero para la guía sin clasificador.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `clip_vision_model` | DINOv3 ViT-L/16 ClipVision. | CLIP_VISION | Sí | — |
| `imagen` | Imagen preprocesada de ImageCropToMask (pad_factor=1.1 para Pixal3D). | IMAGE | Sí | — |
| `camera_angle_x` | FOV horizontal en grados (nombre para mostrar: fov). Conecta un MoGeGeometryToFOV (axis='horizontal', unit='degrees') para un FoV por imagen (coincide con el valor predeterminado de upstream). Predeterminado: 49.13. | FLOAT | Sí | 1.0 – 170.0 |

Nota: El valor de `camera_angle_x` se convierte a radianes internamente y se utiliza para calcular la distancia de cámara para la matriz de transformación de proyección. Cuando el modelo de visión proporcionado incluye un componente NAF, el nodo produce además mapas de características de alta resolución para las etapas de forma y textura.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `positivo` | Condicionamiento positivo que contiene los mapas de características derivados de la imagen y los datos de proyección para la generación Trellis2. | CONDITIONING |
| `negativo` | Condicionamiento negativo con tensores de características a cero, utilizado para la guía sin clasificador. | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pixal3DConditioning/es.md)

---
**Source fingerprint (SHA-256):** `3eba711620f6c56a21bbf7df89f8d406ce6f90908298b1a295a1dbbddd042472`
