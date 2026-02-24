> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MakeTrainingDataset/es.md)

Este nodo prepara datos para entrenamiento codificando imágenes y texto. Toma una lista de imágenes y una lista correspondiente de descripciones de texto, luego utiliza un modelo VAE para convertir las imágenes en representaciones latentes y un modelo CLIP para convertir el texto en datos de condicionamiento. Los latentes y condicionamientos emparejados resultantes se emiten como listas, listos para usar en flujos de trabajo de entrenamiento.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Sí | N/A | Lista de imágenes a codificar. |
| `vae` | VAE | Sí | N/A | Modelo VAE para codificar imágenes a latentes. |
| `clip` | CLIP | Sí | N/A | Modelo CLIP para codificar texto a condicionamiento. |
| `texts` | STRING | No | N/A | Lista de descripciones de texto. Puede tener longitud n (igualando imágenes), 1 (repetida para todas), u omitirse (usa cadena vacía). |

**Restricciones de Parámetros:**

* El número de elementos en la lista `texts` debe ser 0, 1, o coincidir exactamente con el número de elementos en la lista `images`. Si es 0, se usa una cadena vacía para todas las imágenes. Si es 1, ese texto único se repite para todas las imágenes.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `latents` | LATENT | Lista de diccionarios latentes. |
| `conditioning` | CONDITIONING | Lista de listas de condicionamiento. |
