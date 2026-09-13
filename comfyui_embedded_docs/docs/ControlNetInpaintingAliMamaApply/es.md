# ControlNetInpaintingAliMamaApply

El nodo ControlNetInpaintingAliMamaApply aplica condicionamiento ControlNet para tareas de inpainting combinando condicionamiento positivo y negativo con una imagen de control y una máscara. Procesa la imagen de entrada y la máscara para crear un condicionamiento modificado que guía el proceso de generación, permitiendo controlar qué áreas de la imagen reciben inpainting. El nodo admite ajuste de intensidad y controles de temporización para ajustar con precisión la influencia del ControlNet durante diferentes etapas del proceso de generación.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `positive` | El condicionamiento positivo que guía la generación hacia el contenido deseado | CONDITIONING | Sí | - |
| `negative` | El condicionamiento negativo que guía la generación alejándola del contenido no deseado | CONDITIONING | Sí | - |
| `control_net` | El modelo ControlNet que proporciona control adicional sobre la generación | CONTROL_NET | Sí | - |
| `vae` | El VAE (autoencoder variacional) utilizado para codificar y decodificar imágenes | VAE | Sí | - |
| `image` | La imagen de entrada que sirve como guía de control para el ControlNet | IMAGE | Sí | - |
| `mask` | La máscara que define qué áreas de la imagen deben recibir inpainting | MASK | Sí | - |
| `strength` | La intensidad del efecto de ControlNet (predeterminado: 1.0, paso: 0.01) | FLOAT | Sí | 0.0 a 10.0 |
| `start_percent` | Parámetro avanzado. El punto de inicio (como porcentaje) en el que comienza la influencia de ControlNet durante la generación (predeterminado: 0.0, paso: 0.001) | FLOAT | Sí | 0.0 a 1.0 |
| `end_percent` | Parámetro avanzado. El punto final (como porcentaje) en el que se detiene la influencia de ControlNet durante la generación (predeterminado: 1.0, paso: 0.001) | FLOAT | Sí | 0.0 a 1.0 |

**Nota:** Cuando el ControlNet tiene `concat_mask` habilitado, la máscara se invierte y se aplica a la imagen antes del procesamiento, y la máscara invertida se incluye en los datos de concatenación adicionales enviados al ControlNet.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `positive` | El condicionamiento positivo modificado con ControlNet aplicado para inpainting | CONDITIONING |
| `negative` | El condicionamiento negativo modificado con ControlNet aplicado para inpainting | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetInpaintingAliMamaApply/es.md)

---
**Source fingerprint (SHA-256):** `307b55c7b4936826b9e4424c172248fa4b41921c2362de724e5cfa2f1c25de68`
