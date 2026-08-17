# QwenImageDiffsynthControlnet

El nodo QwenImageDiffsynthControlnet aplica un parche de red de control de síntesis por difusión para modificar el comportamiento de un modelo base. Utiliza una imagen de entrada y una máscara opcional para guiar el proceso de generación del modelo con una intensidad ajustable, creando un modelo parcheado que incorpora la influencia de la red de control para una síntesis de imágenes más controlada.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo base que se parcheará con la red de control | MODEL | Sí | - |
| `model_patch` | El modelo de parche de red de control que se aplica al modelo base | MODEL_PATCH | Sí | - |
| `vae` | El VAE (autoencoder variacional) utilizado en el proceso de difusión | VAE | Sí | - |
| `image` | La imagen de entrada utilizada para guiar la red de control (solo se usan los canales RGB) | IMAGE | Sí | - |
| `strength` | La fuerza de la influencia de la red de control (por defecto: 1.0) | FLOAT | Sí | de -10.0 a 10.0 (paso: 0.01) |
| `mask` | Máscara opcional que define las áreas donde se debe aplicar la red de control (se invierte internamente) | MASK | No | - |

**Nota:** Cuando se proporciona una máscara, esta se invierte automáticamente (1.0 - mask) y se reajusta para coincidir con las dimensiones esperadas por el procesamiento de la red de control. Cuando el parche de modelo es de tipo ZImage Control, el parche se aplica tanto al refinador de ruido como a los bloques dobles; para una red de control DiffSynth estándar, solo se aplica el parche del bloque doble.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | El modelo modificado con el parche de red de control de síntesis por difusión aplicado | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageDiffsynthControlnet/es.md)

---
**Source fingerprint (SHA-256):** `56739c098933cb70d3bcb8d6b251da33e7879b464b2e8a7296da085aefc15698`
