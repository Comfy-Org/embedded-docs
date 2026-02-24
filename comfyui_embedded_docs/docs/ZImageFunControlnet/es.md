> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ZImageFunControlnet/es.md)

El nodo ZImageFunControlnet aplica una red de control especializada para influir en el proceso de generación o edición de imágenes. Utiliza un modelo base, un parche de modelo y un VAE, permitiéndote ajustar la intensidad del efecto de control. Este nodo puede trabajar con una imagen base, una imagen para inpainting y una máscara para ediciones más dirigidas.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo base utilizado para el proceso de generación. |
| `model_patch` | MODEL_PATCH | Sí | - | Un modelo de parche especializado que aplica la guía de la red de control. |
| `vae` | VAE | Sí | - | El Autoencoder Variacional utilizado para codificar y decodificar imágenes. |
| `strength` | FLOAT | Sí | -10.0 a 10.0 | La intensidad de la influencia de la red de control. Los valores positivos aplican el efecto, mientras que los negativos pueden invertirlo (valor por defecto: 1.0). |
| `image` | IMAGE | No | - | Una imagen base opcional para guiar el proceso de generación. |
| `inpaint_image` | IMAGE | No | - | Una imagen opcional utilizada específicamente para rellenar áreas definidas por una máscara (inpainting). |
| `mask` | MASK | No | - | Una máscara opcional que define qué áreas de una imagen deben ser editadas o rellenadas. |

**Nota:** El parámetro `inpaint_image` se utiliza típicamente junto con una `mask` para especificar el contenido para el inpainting. El comportamiento del nodo puede cambiar según qué entradas opcionales se proporcionen (por ejemplo, usar `image` para guiar o usar `image`, `mask` e `inpaint_image` para inpainting).

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | El modelo con el parche de la red de control aplicado, listo para usar en un pipeline de muestreo. |
| `positive` | CONDITIONING | El condicionamiento positivo, potencialmente modificado por las entradas de la red de control. |
| `negative` | CONDITIONING | El condicionamiento negativo, potencialmente modificado por las entradas de la red de control. |
