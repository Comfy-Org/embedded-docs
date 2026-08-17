# ControlNetInpaintingAliMamaApply

Este nodo aplica el acondicionamiento de ControlNet para tareas de *inpainting*, combinando el acondicionamiento positivo y negativo con una imagen de control y una máscara. Procesa la imagen y la máscara para crear un acondicionamiento modificado que guía el proceso de generación, permitiendo un control preciso sobre qué áreas se inpaint. El nodo también admite controles de fuerza y temporización para ajustar la influencia de ControlNet durante la generación.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `positive` | El acondicionamiento positivo que guía la generación hacia el contenido deseado. | CONDITIONING | Sí | - |
| `negative` | El acondicionamiento negativo que guía la generación para alejarla del contenido no deseado. | CONDITIONING | Sí | - |
| `control_net` | El modelo ControlNet que proporciona control adicional sobre la generación. | CONTROL_NET | Sí | - |
| `vae` | El VAE utilizado para codificar y decodificar imágenes. | VAE | Sí | - |
| `image` | La imagen de entrada utilizada como guía de control para el ControlNet. | IMAGE | Sí | - |
| `mask` | La máscara que define qué áreas de la imagen deben ser inpaint. | MASK | Sí | - |
| `strength` | La fuerza del efecto de ControlNet (por defecto: 1.0). | FLOAT | Sí | 0.0 a 10.0 |
| `start_percent` | Opción avanzada. La fracción del proceso de generación en la que comienza la influencia de ControlNet (por defecto: 0.0). | FLOAT | Sí | 0.0 a 1.0 |
| `end_percent` | Opción avanzada. La fracción del proceso de generación en la que termina la influencia de ControlNet (por defecto: 1.0). | FLOAT | Sí | 0.0 a 1.0 |

**Nota:** Cuando el ControlNet seleccionado tiene `concat_mask` habilitado, los valores de la máscara se invierten (1 - máscara), se aplica una versión redimensionada de la máscara invertida a la imagen, y la máscara invertida se incluye en los datos de concatenación adicionales pasados al ControlNet. Si `concat_mask` está deshabilitado, la entrada `mask` no se utiliza.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `positive` | El acondicionamiento positivo modificado con ControlNet aplicado para *inpainting*. | CONDITIONING |
| `negative` | El acondicionamiento negativo modificado con ControlNet aplicado para *inpainting*. | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetInpaintingAliMamaApply/es.md)

---
**Source fingerprint (SHA-256):** `307b55c7b4936826b9e4424c172248fa4b41921c2362de724e5cfa2f1c25de68`
