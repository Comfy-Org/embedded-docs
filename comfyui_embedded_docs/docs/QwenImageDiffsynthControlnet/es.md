> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageDiffsynthControlnet/es.md)

El nodo QwenImageDiffsynthControlnet aplica un parche de red de control de síntesis por difusión para modificar el comportamiento de un modelo base. Utiliza una entrada de imagen y una máscara opcional para guiar el proceso de generación del modelo con una intensidad ajustable, creando un modelo parcheado que incorpora la influencia de la red de control para una síntesis de imágenes más controlada.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo base que se va a parchear con la red de control |
| `model_patch` | MODEL_PATCH | Sí | - | El modelo de parche de red de control que se aplicará al modelo base |
| `vae` | VAE | Sí | - | El VAE (Autoencoder Variacional) utilizado en el proceso de difusión |
| `image` | IMAGE | Sí | - | La imagen de entrada utilizada para guiar la red de control (solo se utilizan los canales RGB) |
| `strength` | FLOAT | Sí | -10.0 a 10.0 | La intensidad de la influencia de la red de control (predeterminado: 1.0) |
| `mask` | MASK | No | - | Máscara opcional que define las áreas donde se debe aplicar la red de control (invertida internamente) |

**Nota:** Cuando se proporciona una máscara, se invierte automáticamente (1.0 - máscara) y se redimensiona para que coincida con las dimensiones esperadas para el procesamiento de la red de control. El nodo utiliza diferentes métodos de procesamiento interno dependiendo de si el parche del modelo es de tipo ZImage Control o una red de control DiffSynth estándar.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `model` | MODEL | El modelo modificado con el parche de red de control de síntesis por difusión aplicado |

---
**Source fingerprint (SHA-256):** `61833984d0b92be65fae72a894806572c0588dea74a295e8289d1194dee611bb`
