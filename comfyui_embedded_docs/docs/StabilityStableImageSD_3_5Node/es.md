> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityStableImageSD_3_5Node/es.md)

Este nodo genera imágenes de forma síncrona utilizando el modelo Stable Diffusion 3.5 de Stability AI. Crea imágenes basadas en indicaciones de texto y también puede modificar imágenes existentes cuando se proporcionan como entrada. El nodo admite varias relaciones de aspecto y preajustes de estilo para personalizar el resultado.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | - | Lo que deseas ver en la imagen resultante. Una indicación fuerte y descriptiva que defina claramente elementos, colores y temas conducirá a mejores resultados. (valor por defecto: cadena vacía) |
| `model` | COMBO | Sí | Múltiples opciones disponibles | El modelo Stable Diffusion 3.5 que se utilizará para la generación. |
| `aspect_ratio` | COMBO | Sí | Múltiples opciones disponibles | Relación de aspecto de la imagen generada. (valor por defecto: relación 1:1) |
| `style_preset` | COMBO | No | Múltiples opciones disponibles | Estilo deseado opcional de la imagen generada. |
| `cfg_scale` | FLOAT | Sí | 1.0 a 10.0 | Qué tan estrictamente sigue el proceso de difusión el texto de la indicación (valores más altos mantienen tu imagen más cerca de tu indicación). (valor por defecto: 4.0) |
| `seed` | INT | Sí | 0 a 4294967294 | La semilla aleatoria utilizada para crear el ruido. (valor por defecto: 0) |
| `image` | IMAGE | No | - | Imagen de entrada opcional para generación de imagen a imagen. |
| `negative_prompt` | STRING | No | - | Palabras clave de lo que no deseas ver en la imagen resultante. Esta es una función avanzada. (valor por defecto: cadena vacía) |
| `image_denoise` | FLOAT | No | 0.0 a 1.0 | Desenfoque de la imagen de entrada; 0.0 produce una imagen idéntica a la entrada, 1.0 es como si no se hubiera proporcionado ninguna imagen. (valor por defecto: 0.5) |

**Nota:** Cuando se proporciona una `image`, el nodo cambia al modo de generación de imagen a imagen y el parámetro `aspect_ratio` se determina automáticamente a partir de la imagen de entrada. Cuando no se proporciona una `image`, el parámetro `image_denoise` se ignora.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `image` | IMAGE | La imagen generada o modificada. |
