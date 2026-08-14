# Empty Qwen Image Layered Latent

El nodo Empty Qwen Image Layered Latent prepara el lienzo en blanco sobre el que pinta el modelo Qwen-Image-Layered. Piense en él como una pila de hojas de papel de calcar limpias sujetas en orden: el modelo rellena la primera hoja con la imagen completa y cada hoja posterior con una parte de esa imagen. Este nodo decide el tamaño y la cantidad de las hojas. No dibuja nada por sí mismo.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `ancho` | El ancho de la imagen latente a crear. El valor debe ser divisible entre 16. (predeterminado: 640) | INT | Sí | 16 a MAX_RESOLUTION |
| `alto` | La altura de la imagen latente a crear. El valor debe ser divisible entre 16. (predeterminado: 640) | INT | Sí | 16 a MAX_RESOLUTION |
| `capas` | En cuántas capas dividir la imagen. Siempre se reserva una hoja extra para la imagen completa, por lo que obtiene `layers + 1` imágenes, no `capas`. Si lo establece en 2, obtiene la imagen completa más 2 capas. Si lo establece en 0, obtiene solo la imagen completa. (predeterminado: 3) | INT | Sí | 0 a MAX_RESOLUTION |
| `tamaño_lote` | El número de muestras latentes a generar en un lote. (predeterminado: 1) | INT | No | 1 a 4096 |

**Nota:** Los parámetros `width` y `height` se dividen internamente entre 8 para determinar las dimensiones espaciales del tensor latente de salida.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `samples` | Un tensor latente lleno de ceros. Su forma es `[batch_size, 16, layers + 1, height // 8, width // 8]`. | LATENT |

## Por qué obtiene una imagen más de las que pidió

Qwen-Image-Layered no solo descompone una imagen. También vuelve a pintar la imagen completa, en su propia hoja, junto con las capas. Por eso la pila siempre es una hoja más alta que el número de capas que pidió.

- **La primera imagen es la imagen completa, no una capa.** Es la misma imagen que ya tiene, así que deséchela cuando solo quiera las capas.
- **Si apila todas las capas unas sobre otras, vuelve a obtener la imagen completa.** Si no suman esa primera imagen, la separación no funcionó como quería, por lo que esta es una forma rápida de comprobar el resultado.
- **Mantenga las hojas en orden.** La pila es el único registro de qué capa está sobre cuál. No hay nada escrito en las hojas que indique dónde van, así que reordenar o descartar imágenes significa reordenar o perder capas.
- **Las capas salen con transparencia**, por lo que se pueden apilar sin que las inferiores queden ocultas tras un fondo opaco.

## Sugerencias de uso

Envíe la salida al muestreador como lo haría con un latente vacío normal y, a continuación, coloque LatentCutToBatch con `dim` establecido en `t` antes de la decodificación VAE. Ese es el paso que separa la pila en imágenes individuales, en orden, empezando por la imagen completa.

Empiece con el valor predeterminado de 3 capas. Pedir más significa una generación más larga y una separación más fina, y no merece la pena aumentarlo hasta que haya visto lo que el modelo hace con un número pequeño.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyQwenImageLayeredLatentImage/es.md)

---
**Source fingerprint (SHA-256):** `fe97966663c534dd347aa49a908a8026f2c34716631f1d17be97d74eacc3574e`
