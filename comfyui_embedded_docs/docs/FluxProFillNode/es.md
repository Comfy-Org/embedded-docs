> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProFillNode/es.md)

Pinta imágenes basándose en una máscara y un mensaje de texto. Este nodo utiliza el modelo Flux.1 para rellenar las áreas enmascaradas de una imagen según la descripción de texto proporcionada, generando nuevo contenido que coincida con la imagen circundante.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `imagen` | IMAGE | Sí | - | La imagen de entrada que se va a pintar |
| `mask` | MASK | Sí | - | La máscara que define qué áreas de la imagen deben rellenarse |
| `prompt` | STRING | No | - | Mensaje de texto para la generación de la imagen (predeterminado: cadena vacía) |
| `re-muestreo de prompt` | BOOLEAN | No | - | Si se debe realizar un sobremuestreo en el mensaje de texto. Si está activo, modifica automáticamente el mensaje para una generación más creativa, pero los resultados no son deterministas (la misma semilla no producirá exactamente el mismo resultado). (predeterminado: false) |
| `guía` | FLOAT | No | 1.5-100 | Intensidad de guía para el proceso de generación de la imagen (predeterminado: 60) |
| `pasos` | INT | No | 15-50 | Número de pasos para el proceso de generación de la imagen (predeterminado: 50) |
| `semilla` | INT | No | 0-18446744073709551615 | La semilla aleatoria utilizada para crear el ruido. (predeterminado: 0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output_image` | IMAGE | La imagen generada con las áreas enmascaradas rellenadas según el mensaje de texto |

---
**Source fingerprint (SHA-256):** `ae2708d9e4b99ecb142fca0693c3973957c5677e8121eb5e34d30f872d7102c0`
