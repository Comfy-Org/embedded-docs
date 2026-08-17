# Empty Qwen Image Layered Latent

El nodo Empty Qwen Image Layered Latent prepara el lienzo en blanco sobre el que pinta el modelo Qwen-Image-Layered. Puede imaginarse como una pila de hojas de calco limpias, sujetas juntas en orden: el modelo rellena la primera hoja con la imagen completa y cada hoja posterior con una parte de esa imagen. Este nodo determina el tamaño de las hojas y cuántas hay, pero no dibuja nada por sí mismo.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `width` | La anchura de la imagen latente que se va a crear. El valor debe ser divisible por 16. (predeterminado: 640) | INT | Sí | 16 a MAX_RESOLUTION (paso 16) |
| `height` | La altura de la imagen latente que se va a crear. El valor debe ser divisible por 16. (predeterminado: 640) | INT | Sí | 16 a MAX_RESOLUTION (paso 16) |
| `layers` | En cuántas capas se divide la imagen. Siempre se reserva una hoja adicional para la imagen completa, por lo que se obtienen `layers + 1` imágenes, no `layers`. Si se establece en 2, se obtiene la imagen completa más 2 capas. Si se establece en 0, se obtiene la imagen completa por sí sola. (predeterminado: 3) | INT | Sí | 0 a MAX_RESOLUTION (paso 1) |
| `batch_size` | El número de muestras latentes que se generan en un lote. (predeterminado: 1) | INT | Sí | 1 a 4096 |

**Nota:** Los parámetros `width` y `height` se dividen internamente por 8 para determinar las dimensiones espaciales del tensor latente de salida.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `samples` | Un tensor latente relleno de ceros. Su forma es `[batch_size, 16, layers + 1, height // 8, width // 8]`. | LATENT |

## Por qué se obtiene una imagen más de la solicitada

Qwen-Image-Layered no solo separa una imagen en partes. También vuelve a pintar la imagen completa, en su propia hoja, junto con las capas. Por eso la pila siempre tiene una hoja más que el número de capas solicitado.

- **La primera imagen es la imagen completa, no una capa.** Es la misma imagen que ya se tiene, así que puede descartarse si solo se desean las capas.
- **Si se vuelven a apilar todas las capas unas sobre otras, se obtiene de nuevo la imagen completa.** Si no suman hasta reconstruir esa primera imagen, la separación no ha funcionado como se quería; por tanto, esta es una forma rápida de comprobar el resultado.
- **Las hojas deben mantenerse en orden.** La pila es el único registro de qué capa está encima de cuál. No hay ninguna anotación en las hojas que indique dónde van, así que reordenarlas o eliminar imágenes equivale a reordenar o perder capas.
- **Las capas se obtienen con transparencia**, por lo que pueden apilarse sin que las inferiores queden ocultas tras un fondo opaco.

## Sugerencias de uso

La salida se envía al muestreador del mismo modo que se haría con un latente vacío normal y, a continuación, se coloca LatentCutToBatch con `dim` establecido en `t` antes de VAE Decode. Ese es el paso que separa la pila en imágenes individuales, en orden, empezando por la imagen completa.

Se recomienda empezar con el valor predeterminado de 3 capas. Pedir más implica una generación más larga y una separación más fina, y no merece la pena aumentarlo hasta haber visto lo que el modelo hace con un número pequeño.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyQwenImageLayeredLatentImage/es.md)

---
**Source fingerprint (SHA-256):** `5ccac979fcbcefb65f28867a89401c095cb330e09c13270008c32feeeafb1287`
