> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/unCLIPConditioning/es.md)

Este nodo está diseñado para integrar las salidas de visión CLIP en el proceso de condicionamiento, ajustando la influencia de estas salidas según parámetros específicos de intensidad y aumento de ruido. Enriquece el condicionamiento con contexto visual, mejorando el proceso de generación.

## Entradas

| Parámetro               | Tipo Comfy             | Descripción |
|-------------------------|------------------------|-------------|
| `conditioning`          | `CONDITIONING`         | Los datos de condicionamiento base a los que se agregarán las salidas de visión CLIP, sirviendo como base para modificaciones posteriores. |
| `clip_vision_output`    | `CLIP_VISION_OUTPUT`   | La salida de un modelo de visión CLIP, que proporciona contexto visual que se integra en el condicionamiento. |
| `strength`              | `FLOAT`                | Determina la intensidad de la influencia de la salida de visión CLIP sobre el condicionamiento. |
| `noise_augmentation`    | `FLOAT`                | Especifica el nivel de aumento de ruido que se aplicará a la salida de visión CLIP antes de integrarla en el condicionamiento. |

## Salidas

| Parámetro              | Tipo Comfy             | Descripción |
|------------------------|------------------------|-------------|
| `conditioning`          | `CONDITIONING`         | Los datos de condicionamiento enriquecidos, que ahora contienen las salidas de visión CLIP integradas con la intensidad y el aumento de ruido aplicados. |