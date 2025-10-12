> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProUltraImageNode/es.md)

Genera imágenes utilizando Flux Pro 1.1 Ultra mediante API basándose en el prompt y la resolución. Este nodo se conecta a un servicio externo para crear imágenes de acuerdo con tu descripción de texto y las dimensiones especificadas.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | - | Prompt para la generación de imagen (valor por defecto: cadena vacía) |
| `prompt_upsampling` | BOOLEAN | No | - | Si realizar upsampling en el prompt. Si está activo, modifica automáticamente el prompt para una generación más creativa, pero los resultados son no determinísticos (la misma semilla no producirá exactamente el mismo resultado). (valor por defecto: False) |
| `seed` | INT | No | 0 a 18446744073709551615 | La semilla aleatoria utilizada para crear el ruido. (valor por defecto: 0) |
| `aspect_ratio` | STRING | No | - | Relación de aspecto de la imagen; debe estar entre 1:4 y 4:1. (valor por defecto: "16:9") |
| `raw` | BOOLEAN | No | - | Cuando es True, genera imágenes menos procesadas y de apariencia más natural. (valor por defecto: False) |
| `image_prompt` | IMAGE | No | - | Imagen de referencia opcional para guiar la generación |
| `image_prompt_strength` | FLOAT | No | 0.0 a 1.0 | Mezcla entre el prompt y el prompt de imagen. (valor por defecto: 0.1) |

**Nota:** El parámetro `aspect_ratio` debe estar entre 1:4 y 4:1. Cuando se proporciona `image_prompt`, `image_prompt_strength` se activa y controla cuánto influye la imagen de referencia en el resultado final.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output_image` | IMAGE | La imagen generada por Flux Pro 1.1 Ultra |
