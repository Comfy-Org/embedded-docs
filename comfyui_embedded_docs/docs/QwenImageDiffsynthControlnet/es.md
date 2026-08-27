# QwenImageDiffsynthControlnet

QwenImageDiffsynthControlnet aplica un parche de red de control de síntesis de difusión a un modelo base. Utiliza una imagen de entrada y una máscara opcional para guiar el proceso de generación del modelo con una fuerza ajustable, produciendo un modelo parcheado que incorpora la influencia de la red de control para una síntesis de imágenes más controlada.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo base que se parcheará con la red de control | MODEL | Sí | - |
| `parche_del_modelo` | El modelo de parche de la red de control que se aplicará al modelo base | MODEL_PATCH | Sí | - |
| `vae` | El VAE (Autoencoder Variacional) utilizado en el proceso de difusión | VAE | Sí | - |
| `imagen` | La imagen de entrada utilizada para guiar la red de control. Solo se utilizan los primeros tres canales de color (RGB); cualquier canal adicional se descarta | IMAGE | Sí | - |
| `intensidad` | La fuerza de la influencia de la red de control (por defecto: 1.0) | FLOAT | Sí | -10.0 a 10.0 |
| `máscara` | Máscara opcional que define las áreas donde se debe aplicar la red de control. La máscara se invierte internamente antes de su uso | MASK | No | - |

**Nota:** Cuando se proporciona una máscara, se invierte automáticamente (1.0 - máscara) y se reforma para que coincida con las dimensiones esperadas para el procesamiento de la red de control. El nodo utiliza diferentes métodos de procesamiento interno dependiendo de si el parche del modelo es de tipo ZImage Control o una red de control DiffSynth estándar. Este nodo está marcado como experimental.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `model` | El modelo modificado con el parche de red de control de síntesis de difusión aplicado | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageDiffsynthControlnet/es.md)

---
**Source fingerprint (SHA-256):** `56739c098933cb70d3bcb8d6b251da33e7879b464b2e8a7296da085aefc15698`
