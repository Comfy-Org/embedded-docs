> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProImageNode/es.md)

Genera imágenes de forma síncrona basándose en un prompt y una resolución. Este nodo crea imágenes utilizando el modelo Flux 1.1 Pro mediante el envío de solicitudes a un endpoint de API y espera la respuesta completa antes de devolver la imagen generada.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | - | Prompt para la generación de la imagen (valor por defecto: cadena vacía) |
| `prompt_upsampling` | BOOLEAN | Sí | - | Si se debe realizar un remuestreo superior (upsampling) en el prompt. Si está activo, modifica automáticamente el prompt para una generación más creativa, pero los resultados son no deterministas (la misma semilla no producirá exactamente el mismo resultado). (valor por defecto: False) |
| `width` | INT | Sí | 256-1440 | Ancho de la imagen en píxeles (valor por defecto: 1024, paso: 32) |
| `height` | INT | Sí | 256-1440 | Alto de la imagen en píxeles (valor por defecto: 768, paso: 32) |
| `seed` | INT | Sí | 0-18446744073709551615 | La semilla aleatoria utilizada para crear el ruido. (valor por defecto: 0) |
| `image_prompt` | IMAGE | No | - | Imagen de referencia opcional para guiar la generación |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | IMAGE | La imagen generada devuelta por la API |