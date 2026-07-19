# ZImageFunControlnet

El nodo ZImageFunControlnet aplica una red de control especializada para influir en el proceso de generación o edición de imágenes. Utiliza un modelo base, un parche de modelo y un VAE, permitiéndote ajustar la intensidad del efecto de control. Este nodo puede funcionar con una imagen base, una imagen para inpainting y una máscara para ediciones más específicas.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo base utilizado para el proceso de generación. | MODEL | Sí | - |
| `parche_de_modelo` | Un modelo de parche especializado que aplica la guía de la red de control. | MODEL_PATCH | Sí | - |
| `vae` | El Autoencoder Variacional utilizado para codificar y decodificar imágenes. | VAE | Sí | - |
| `fuerza` | La intensidad de la influencia de la red de control. Los valores positivos aplican el efecto, mientras que los valores negativos pueden invertirlo (valor predeterminado: 1.0). | FLOAT | Sí | -10.0 a 10.0 |
| `imagen` | Una imagen base opcional para guiar el proceso de generación. | IMAGE | No | - |
| `imagen_relleno` | Una imagen opcional utilizada específicamente para el inpainting de áreas definidas por una máscara. | IMAGE | No | - |
| `máscara` | Una máscara opcional que define qué áreas de una imagen deben editarse o repararse mediante inpainting. | MASK | No | - |

**Nota:** El parámetro `inpaint_image` se utiliza típicamente junto con una `mask` para especificar el contenido del inpainting. El comportamiento del nodo puede cambiar según las entradas opcionales proporcionadas (por ejemplo, usando `image` como guía o usando `image`, `mask` e `inpaint_image` para inpainting).

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `modelo` | El modelo con el parche de red de control aplicado, listo para usar en un pipeline de muestreo. | MODEL |
| `positive` | El condicionamiento positivo, potencialmente modificado por las entradas de la red de control. | CONDITIONING |
| `negative` | El condicionamiento negativo, potencialmente modificado por las entradas de la red de control. | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ZImageFunControlnet/es.md)

---
**Source fingerprint (SHA-256):** `465f9eb0dd60af23e6cdc2031579e404b4fed021738e592ee6acbb6ee57e83a0`
