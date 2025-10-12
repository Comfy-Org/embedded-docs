
Este nodo está diseñado para integrar las salidas de visión CLIP en el proceso de condicionamiento, ajustando la influencia de estas salidas según los parámetros de fuerza y aumento de ruido especificados. Enriquece el condicionamiento con contexto visual, mejorando el proceso de generación.

## Entradas

| Parámetro              | Comfy dtype            | Descripción |
|------------------------|------------------------|-------------|
| `acondicionamiento`         | `CONDITIONING`         | Los datos base de condicionamiento a los que se añadirán las salidas de visión CLIP, sirviendo como base para futuras modificaciones. |
| `salida_vision_clip`   | `CLIP_VISION_OUTPUT`   | La salida de un modelo de visión CLIP, proporcionando contexto visual que se integra en el condicionamiento. |
| `fuerza`             | `FLOAT`                | Determina la intensidad de la influencia de la salida de visión CLIP en el condicionamiento. |
| `aumento_ruido`   | `FLOAT`                | Especifica el nivel de aumento de ruido a aplicar a la salida de visión CLIP antes de integrarla en el condicionamiento. |

## Salidas

| Parámetro             | Comfy dtype            | Descripción |
|-----------------------|------------------------|-------------|
| `acondicionamiento`         | `CONDITIONING`         | Los datos de condicionamiento enriquecidos, que ahora contienen salidas de visión CLIP integradas con fuerza aplicada y aumento de ruido. |
