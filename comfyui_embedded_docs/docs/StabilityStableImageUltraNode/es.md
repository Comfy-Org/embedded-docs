> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityStableImageUltraNode/es.md)

Genera imágenes de forma síncrona basándose en el prompt y la resolución. Este nodo crea imágenes utilizando el modelo Stable Image Ultra de Stability AI, procesando tu prompt de texto y generando una imagen correspondiente con la relación de aspecto y estilo especificados.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | - | Lo que deseas ver en la imagen de salida. Un prompt fuerte y descriptivo que defina claramente elementos, colores y temas conducirá a mejores resultados. Para controlar el peso de una palabra específica, utiliza el formato `(palabra:peso)`, donde `palabra` es la palabra cuyo peso deseas controlar y `peso` es un valor entre 0 y 1. Por ejemplo: `El cielo era un (azul:0.3) y (verde:0.8)` representaría un cielo azul y verde, pero más verde que azul. |
| `aspect_ratio` | COMBO | Sí | Múltiples opciones disponibles | Relación de aspecto de la imagen generada. |
| `style_preset` | COMBO | No | Múltiples opciones disponibles | Estilo opcional deseado para la imagen generada. |
| `seed` | INT | Sí | 0-4294967294 | La semilla aleatoria utilizada para crear el ruido. |
| `image` | IMAGE | No | - | Imagen de entrada opcional. |
| `negative_prompt` | STRING | No | - | Un fragmento de texto que describe lo que no deseas ver en la imagen de salida. Esta es una función avanzada. |
| `image_denoise` | FLOAT | No | 0.0-1.0 | Nivel de eliminación de ruido de la imagen de entrada; 0.0 produce una imagen idéntica a la entrada, 1.0 es como si no se proporcionara ninguna imagen. Por defecto: 0.5 |

**Nota:** Cuando no se proporciona una imagen de entrada, el parámetro `image_denoise` se desactiva automáticamente.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | IMAGE | La imagen generada basada en los parámetros de entrada. |
