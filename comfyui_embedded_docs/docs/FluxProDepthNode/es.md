> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProDepthNode/es.md)

Este nodo genera imágenes utilizando una imagen de control de profundidad como guía. Toma una imagen de control y un texto descriptivo, luego crea una nueva imagen que sigue tanto la información de profundidad de la imagen de control como la descripción en el texto. El nodo se conecta a una API externa para realizar el proceso de generación de imágenes.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `control_image` | IMAGE | Sí | - | La imagen de control de profundidad utilizada para guiar la generación de la imagen |
| `prompt` | STRING | No | - | Texto descriptivo para la generación de la imagen (valor por defecto: cadena vacía) |
| `prompt_upsampling` | BOOLEAN | No | - | Si se debe realizar un remuestreo del texto descriptivo. Si está activo, modifica automáticamente el texto para una generación más creativa, pero los resultados son no deterministas (la misma semilla no producirá exactamente el mismo resultado). (valor por defecto: False) |
| `skip_preprocessing` | BOOLEAN | No | - | Si se debe omitir el preprocesamiento; establecer en True si control_image ya está procesada para profundidad, False si es una imagen sin procesar. (valor por defecto: False) |
| `guidance` | FLOAT | No | 1-100 | Intensidad de guía para el proceso de generación de imágenes (valor por defecto: 15) |
| `steps` | INT | No | 15-50 | Número de pasos para el proceso de generación de imágenes (valor por defecto: 50) |
| `seed` | INT | No | 0-18446744073709551615 | La semilla aleatoria utilizada para crear el ruido. (valor por defecto: 0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output_image` | IMAGE | La imagen generada basada en la imagen de control de profundidad y el texto descriptivo |
