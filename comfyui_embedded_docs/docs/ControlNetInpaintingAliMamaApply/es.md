# ControlNetInpaintingAliMamaApply

El nodo ControlNetInpaintingAliMamaApply aplica el condicionamiento ControlNet para tareas de inpainting combinando el condicionamiento positivo y negativo con una imagen de control y una máscara. Procesa la imagen y la máscara de entrada para crear un condicionamiento modificado que guía el proceso de generación, permitiendo un control preciso sobre qué áreas de la imagen se rellenan (inpainting). El nodo admite ajustes de intensidad y controles de temporización para afinar la influencia del ControlNet durante diferentes etapas del proceso de generación.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `positivo` | El condicionamiento positivo que guía la generación hacia el contenido deseado | CONDITIONING | Sí | - |
| `negativo` | El condicionamiento negativo que guía la generación para evitar contenido no deseado | CONDITIONING | Sí | - |
| `control_net` | El modelo ControlNet que proporciona control adicional sobre la generación | CONTROL_NET | Sí | - |
| `vae` | El VAE (autoencoder variacional) utilizado para codificar y decodificar imágenes | VAE | Sí | - |
| `imagen` | La imagen de entrada que sirve como guía de control para el ControlNet | IMAGE | Sí | - |
| `máscara` | La máscara que define qué áreas de la imagen deben ser rellenadas (inpainting) | MASK | Sí | - |
| `fuerza` | La intensidad del efecto ControlNet (por defecto: 1.0, paso: 0.01) | FLOAT | Sí | 0.0 a 10.0 |
| `porcentaje_inicio` | Parámetro avanzado. El punto de inicio (como porcentaje) en el que la influencia del ControlNet comienza durante la generación (por defecto: 0.0, paso: 0.001) | FLOAT | Sí | 0.0 a 1.0 |
| `porcentaje_final` | Parámetro avanzado. El punto final (como porcentaje) en el que la influencia del ControlNet se detiene durante la generación (por defecto: 1.0, paso: 0.001) | FLOAT | Sí | 0.0 a 1.0 |

**Nota:** Cuando el ControlNet tiene `concat_mask` habilitado, la máscara se invierte y se aplica a la imagen antes del procesamiento, y la máscara invertida se incluye en los datos de concatenación adicionales enviados al ControlNet.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `positivo` | El condicionamiento positivo modificado con ControlNet aplicado para inpainting | CONDITIONING |
| `negativo` | El condicionamiento negativo modificado con ControlNet aplicado para inpainting | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetInpaintingAliMamaApply/es.md)

---
**Source fingerprint (SHA-256):** `307b55c7b4936826b9e4424c172248fa4b41921c2362de724e5cfa2f1c25de68`
