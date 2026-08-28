# Crear Conjunto de Datos de Entrenamiento

Este nodo prepara datos para el entrenamiento codificando imágenes y texto. Toma una lista de imágenes y una lista correspondiente de descripciones de texto, y luego utiliza un modelo VAE para convertir las imágenes en representaciones latentes y un modelo CLIP para convertir el texto en datos de condicionamiento. Los resultados son listas de latentes y condicionamientos emparejados, listos para usarse en flujos de trabajo de entrenamiento.

## Entradas

| Parámetro | Descripción | Tipo de datos | ¿Requerido? | Rango |
| --- | --- | --- | --- | --- |
| `imágenes` | Lista de imágenes a codificar. | IMAGE | Sí | N/D |
| `vae` | Modelo VAE para codificar imágenes a latentes. | VAE | Sí | N/D |
| `clip` | Modelo CLIP para codificar texto a condicionamiento. | CLIP | Sí | N/D |
| `textos` | Lista de descripciones de texto. Puede tener una longitud de n (coincidiendo con las imágenes), 1 (repetida para todas), u omitirse (se usa una cadena vacía). | STRING | No | 0, 1 o n elementos (n = número de imágenes) |

**Restricciones de parámetros:**

* El número de elementos en la lista `texts` debe ser 0, 1 o coincidir exactamente con el número de elementos en la lista `images`. Si es 0, se usa una cadena vacía para todas las imágenes. Si es 1, ese único texto se repite para todas las imágenes. Cualquier otra longitud genera un error.
* Las listas de salida `latents` y `conditioning` siempre contienen el mismo número de elementos que la lista `images`, por lo que cada latente se empareja con el condicionamiento de su descripción correspondiente.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `latentes` | Lista de diccionarios latentes. | LATENT |
| `acondicionamiento` | Lista de listas de condicionamiento. | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MakeTrainingDataset/es.md)

---
**Source fingerprint (SHA-256):** `244adc98810a874cfe42f834e89f96da300d883faeb5791dff19607c13d0c0db`
