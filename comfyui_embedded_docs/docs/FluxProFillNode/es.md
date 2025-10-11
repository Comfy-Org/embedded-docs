> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProFillNode/es.md)

Rellena áreas de una imagen basándose en una máscara y un texto descriptivo. Este nodo utiliza el modelo Flux.1 para rellenar las áreas enmascaradas de una imagen de acuerdo con la descripción de texto proporcionada, generando nuevo contenido que coincide con la imagen circundante.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen de entrada que se va a rellenar |
| `mask` | MASK | Sí | - | La máscara que define qué áreas de la imagen deben ser rellenadas |
| `prompt` | STRING | No | - | Texto descriptivo para la generación de la imagen (valor por defecto: cadena vacía) |
| `prompt_upsampling` | BOOLEAN | No | - | Si se debe realizar un remuestreo superior (upsampling) en el texto descriptivo. Si está activo, modifica automáticamente el texto para una generación más creativa, pero los resultados son no deterministas (la misma semilla no producirá exactamente el mismo resultado). (valor por defecto: false) |
| `guidance` | FLOAT | No | 1.5-100 | Intensidad de guía para el proceso de generación de la imagen (valor por defecto: 60) |
| `steps` | INT | No | 15-50 | Número de pasos para el proceso de generación de la imagen (valor por defecto: 50) |
| `seed` | INT | No | 0-18446744073709551615 | La semilla aleatoria utilizada para crear el ruido. (valor por defecto: 0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output_image` | IMAGE | La imagen generada con las áreas enmascaradas rellenadas de acuerdo con el texto descriptivo |