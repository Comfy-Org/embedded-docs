> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscale/es.md)

El nodo LatentUpscale está diseñado para escalar representaciones latentes de imágenes. Permite ajustar las dimensiones de la imagen de salida y el método de escalado, ofreciendo flexibilidad para mejorar la resolución de imágenes latentes.

## Entradas

| Parámetro | Tipo de dato | Descripción |
|-----------|-------------|-------------|
| `samples` | `LATENT`    | La representación latente de una imagen que se va a escalar. Este parámetro es crucial para determinar el punto de partida del proceso de escalado. |
| `upscale_method` | COMBO[STRING] | Especifica el método utilizado para escalar la imagen latente. Diferentes métodos pueden afectar la calidad y las características de la imagen escalada. |
| `width`   | `INT`       | El ancho deseado de la imagen escalada. Si se establece en 0, se calculará en función de la altura para mantener la relación de aspecto. |
| `height`  | `INT`       | La altura deseada de la imagen escalada. Si se establece en 0, se calculará en función del ancho para mantener la relación de aspecto. |
| `crop`    | COMBO[STRING] | Determina cómo se debe recortar la imagen escalada, afectando la apariencia final y las dimensiones de la salida. |

## Salidas

| Parámetro | Tipo de dato | Descripción |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La representación latente escalada de la imagen, lista para su posterior procesamiento o generación. |