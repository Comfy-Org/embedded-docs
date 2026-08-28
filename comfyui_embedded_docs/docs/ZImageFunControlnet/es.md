# ZImageFunControlnet

ZImageFunControlnet aplica una red de control especializada para influir en el proceso de generación o edición de imágenes. Utiliza un modelo base, un parche de modelo y un VAE, lo que permite ajustar la intensidad del efecto de control. Este nodo puede trabajar con una imagen base, una imagen de inpainting y una máscara para realizar ediciones más específicas.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo base utilizado para el proceso de generación. | MODEL | Sí | - |
| `parche_de_modelo` | Un modelo de parche especializado que aplica la guía de la red de control. | MODEL_PATCH | Sí | - |
| `vae` | El Autoencoder Variacional (VAE) utilizado para codificar y decodificar imágenes. | VAE | Sí | - |
| `fuerza` | La intensidad de la influencia de la red de control. Los valores positivos aplican el efecto, mientras que los valores negativos pueden invertirlo (por defecto: 1.0). | FLOAT | Sí | -10.0 a 10.0 |
| `imagen` | Una imagen base opcional para guiar el proceso de generación. | IMAGE | No | - |
| `imagen_relleno` | Una imagen opcional utilizada específicamente para realizar inpainting en las áreas definidas por una máscara. | IMAGE | No | - |
| `máscara` | Una máscara opcional que define qué áreas de una imagen deben editarse o procesarse con inpainting. | MASK | No | - |

**Nota:** El parámetro `inpaint_image` se usa normalmente junto con una `mask` para especificar el contenido del inpainting. El comportamiento del nodo puede cambiar según las entradas opcionales proporcionadas (por ejemplo, usar `image` como guía o usar `image`, `mask` e `inpaint_image` para inpainting).

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | El modelo con el parche de red de control aplicado, listo para usarse en un pipeline de muestreo. | MODEL |
| `positive` | El condicionamiento positivo, potencialmente modificado por las entradas de la red de control. | CONDITIONING |
| `negative` | El condicionamiento negativo, potencialmente modificado por las entradas de la red de control. | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ZImageFunControlnet/es.md)

---
**Source fingerprint (SHA-256):** `e1946190a06c52dd951078d9cb753962081957cb6c38accdea26eb4129a51793`
