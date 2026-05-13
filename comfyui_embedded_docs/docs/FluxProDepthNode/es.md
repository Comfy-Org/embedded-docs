> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProDepthNode/es.md)

Este nodo genera imágenes utilizando una imagen de control de profundidad como guía. Toma una imagen de control y un prompt de texto, luego crea una nueva imagen que sigue tanto la información de profundidad de la imagen de control como la descripción del prompt. El nodo se conecta a una API externa para realizar el proceso de generación de imágenes.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `control_image` | IMAGE | Sí | - | La imagen de control de profundidad utilizada para guiar la generación de la imagen |
| `prompt` | STRING | No | - | Prompt para la generación de la imagen (predeterminado: cadena vacía) |
| `prompt_upsampling` | BOOLEAN | No | - | Si se debe realizar un sobremuestreo en el prompt. Si está activo, modifica automáticamente el prompt para una generación más creativa, pero los resultados no son deterministas (la misma semilla no producirá exactamente el mismo resultado). (predeterminado: False) |
| `skip_preprocessing` | BOOLEAN | No | - | Si se debe omitir el preprocesamiento; establecer en True si `control_image` ya tiene profundidad aplicada, False si es una imagen en bruto. (predeterminado: False) |
| `guidance` | FLOAT | No | 1-100 | Intensidad de guía para el proceso de generación de la imagen (predeterminado: 15) |
| `steps` | INT | No | 15-50 | Número de pasos para el proceso de generación de la imagen (predeterminado: 50) |
| `seed` | INT | No | 0-18446744073709551615 | La semilla aleatoria utilizada para crear el ruido. (predeterminado: 0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `output_image` | IMAGE | La imagen generada basada en la imagen de control de profundidad y el prompt |

---
**Source fingerprint (SHA-256):** `34b80d7d63158b7dc4ad02da6b3a573b713d77efd0955d3477409f776f964462`
