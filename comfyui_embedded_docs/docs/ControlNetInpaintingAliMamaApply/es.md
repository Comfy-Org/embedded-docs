> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetInpaintingAliMamaApply/es.md)

El nodo ControlNetInpaintingAliMamaApply aplica el acondicionamiento ControlNet para tareas de inpainting combinando el acondicionamiento positivo y negativo con una imagen de control y una máscara. Procesa la imagen de entrada y la máscara para crear un acondicionamiento modificado que guía el proceso de generación, permitiendo un control preciso sobre qué áreas de la imagen se rellenan. El nodo soporta ajustes de fuerza y controles de temporización para afinar la influencia del ControlNet durante las diferentes etapas del proceso de generación.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `positivo` | CONDITIONING | Sí | - | El acondicionamiento positivo que guía la generación hacia el contenido deseado |
| `negativo` | CONDITIONING | Sí | - | El acondicionamiento negativo que guía la generación lejos del contenido no deseado |
| `control_net` | CONTROL_NET | Sí | - | El modelo ControlNet que proporciona control adicional sobre la generación |
| `vae` | VAE | Sí | - | El VAE (Autoencoder Variacional) utilizado para codificar y decodificar imágenes |
| `imagen` | IMAGE | Sí | - | La imagen de entrada que sirve como guía de control para el ControlNet |
| `máscara` | MASK | Sí | - | La máscara que define qué áreas de la imagen deben ser rellenadas |
| `fuerza` | FLOAT | Sí | 0.0 a 10.0 | La fuerza del efecto ControlNet (valor por defecto: 1.0) |
| `porcentaje_inicio` | FLOAT | Sí | 0.0 a 1.0 | El punto de inicio (como porcentaje) de cuándo comienza la influencia del ControlNet durante la generación (valor por defecto: 0.0) |
| `porcentaje_final` | FLOAT | Sí | 0.0 a 1.0 | El punto final (como porcentaje) de cuándo se detiene la influencia del ControlNet durante la generación (valor por defecto: 1.0) |

**Nota:** Cuando el ControlNet tiene `concat_mask` habilitado, la máscara se invierte y se aplica a la imagen antes del procesamiento, y la máscara se incluye en los datos de concatenación adicionales enviados al ControlNet.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `negativo` | CONDITIONING | El acondicionamiento positivo modificado con ControlNet aplicado para inpainting |
| `negativo` | CONDITIONING | El acondicionamiento negativo modificado con ControlNet aplicado para inpainting |