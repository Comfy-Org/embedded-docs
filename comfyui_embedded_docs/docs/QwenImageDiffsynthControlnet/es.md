> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageDiffsynthControlnet/es.md)

El nodo QwenImageDiffsynthControlnet aplica un parche de red de control de síntesis por difusión para modificar el comportamiento de un modelo base. Utiliza una imagen de entrada y una máscara opcional para guiar el proceso de generación del modelo con fuerza ajustable, creando un modelo parcheado que incorpora la influencia de la red de control para una síntesis de imagen más controlada.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo base que será parcheado con la red de control |
| `model_patch` | MODEL_PATCH | Sí | - | El modelo de parche de red de control a aplicar al modelo base |
| `vae` | VAE | Sí | - | El VAE (Autoencoder Variacional) utilizado en el proceso de difusión |
| `image` | IMAGE | Sí | - | La imagen de entrada utilizada para guiar la red de control (solo se utilizan los canales RGB) |
| `strength` | FLOAT | Sí | -10.0 a 10.0 | La fuerza de la influencia de la red de control (valor por defecto: 1.0) |
| `mask` | MASK | No | - | Máscara opcional que define las áreas donde se debe aplicar la red de control (se invierte internamente) |

**Nota:** Cuando se proporciona una máscara, esta se invierte automáticamente (1.0 - máscara) y se redimensiona para que coincida con las dimensiones esperadas para el procesamiento de la red de control.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | El modelo modificado con el parche de red de control de síntesis por difusión aplicado |