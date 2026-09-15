# ZImageFunControlnet

ZImageFunControlnet aplica un parche de red de control a un modelo base para que pueda guiar el proceso de generación o edición de imágenes. Combina un modelo, un parche de modelo y un VAE, y te permite controlar con qué intensidad el efecto de control influye en el resultado. Las entradas opcionales de imagen, imagen de inpainting y máscara permiten ediciones más específicas.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo base utilizado para el proceso de generación. | MODEL | Sí | - |
| `parche_de_modelo` | Un modelo de parche especializado que aplica la guía de la red de control. | MODEL_PATCH | Sí | - |
| `vae` | El Autoencoder Variacional usado para codificar y decodificar imágenes. | VAE | Sí | - |
| `fuerza` | La fuerza de la influencia de la red de control. Los valores positivos aplican el efecto, mientras que los valores negativos pueden invertirlo (predeterminado: 1.0). | FLOAT | Sí | -10.0 a 10.0 (paso 0.01) |
| `imagen` | Una imagen base opcional para guiar el proceso de generación. | IMAGE | No | - |
| `imagen_relleno` | Una imagen opcional usada específicamente para inpainting en áreas definidas por una máscara. | IMAGE | No | - |
| `máscara` | Una máscara opcional que define qué áreas de una imagen deben editarse o someterse a inpainting. | MASK | No | - |

**Nota:** El parámetro `inpaint_image` se suele usar junto con una `mask` para especificar el contenido para inpainting. El comportamiento del nodo puede cambiar según qué entradas opcionales se proporcionen (p. ej., usar `image` como guía o usar `image`, `mask` e `inpaint_image` para inpainting).

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | El modelo con el parche de red de control aplicado, listo para usarse en un pipeline de muestreo. | MODEL |
| `positive` | El condicionamiento positivo, potencialmente modificado por las entradas de la red de control. | CONDITIONING |
| `negative` | El condicionamiento negativo, potencialmente modificado por las entradas de la red de control. | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ZImageFunControlnet/es.md)

---
**Source fingerprint (SHA-256):** `e1946190a06c52dd951078d9cb753962081957cb6c38accdea26eb4129a51793`
