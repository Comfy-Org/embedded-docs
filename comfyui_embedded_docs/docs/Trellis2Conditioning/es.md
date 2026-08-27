# Trellis2Conditioning

Trellis2Conditioning convierte una imagen de entrada en datos de acondicionamiento para el modelo TRELLIS.2. Utiliza un modelo de visión CLIP para codificar la imagen en dos conjuntos de características (a escalas de 512 y 1024) y los empaqueta como un par de condicionamiento positivo, a la vez que crea un par de condicionamiento negativo relleno de ceros que sirve como referencia vacía.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `clip_vision_model` | El modelo de visión CLIP utilizado para codificar la imagen en características de acondicionamiento. | CLIP_VISION | Sí | Cualquier modelo de visión CLIP disponible |
| `image` | Imagen preprocesada de ImageCropToMask (pad_factor=1.0 para TRELLIS.2). | IMAGE | Sí | Cualquier imagen |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `positive` | Acondicionamiento que contiene las características de la imagen codificadas a escalas de 512 y 1024, utilizado como condicionamiento positivo para el modelo TRELLIS.2. | CONDITIONING |
| `negative` | Acondicionamiento relleno de ceros con la misma forma que el condicionamiento positivo, utilizado como referencia negativa vacía. | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2Conditioning/es.md)

---
**Source fingerprint (SHA-256):** `467698e58558ceca9ac633d63aacf360a1eb674ac4ebd47de7423f85e62c0fe6`
