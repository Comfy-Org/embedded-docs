> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MakeTrainingDataset/es.md)

Este nodo prepara datos para entrenamiento codificando imágenes y texto. Toma una lista de imágenes y una lista correspondiente de descripciones textuales, luego utiliza un modelo VAE para convertir las imágenes en representaciones latentes y un modelo CLIP para convertir el texto en datos de condicionamiento. Los pares resultantes de latentes y condicionamiento se emiten como listas, listas para su uso en flujos de trabajo de entrenamiento.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `images` | IMAGE | Sí | N/A | Lista de imágenes a codificar. |
| `vae` | VAE | Sí | N/A | Modelo VAE para codificar imágenes a latentes. |
| `clip` | CLIP | Sí | N/A | Modelo CLIP para codificar texto a condicionamiento. |
| `texts` | STRING | No | N/A | Lista de descripciones textuales. Puede tener longitud n (coincidiendo con las imágenes), 1 (repetida para todas), u omitirse (usa cadena vacía). |

**Restricciones de Parámetros:**

* La cantidad de elementos en la lista `texts` debe ser 0, 1, o coincidir exactamente con la cantidad de elementos en la lista `images`. Si es 0, se usa una cadena vacía para todas las imágenes. Si es 1, ese único texto se repite para todas las imágenes.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `latents` | LATENT | Lista de diccionarios latentes. |
| `conditioning` | CONDITIONING | Lista de listas de condicionamiento. |

---
**Source fingerprint (SHA-256):** `95947c03f140f527f3db54d0b0131d956646055542ddb546ae5eaa82e4e8cefa`
