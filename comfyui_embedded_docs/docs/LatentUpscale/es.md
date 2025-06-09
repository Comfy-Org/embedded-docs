
El nodo LatentUpscale está diseñado para ampliar las representaciones latentes de imágenes. Permite ajustar las dimensiones de la imagen de salida y el método de ampliación, proporcionando flexibilidad en la mejora de la resolución de imágenes latentes.

## Entradas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `samples` | `LATENT`    | La representación latente de una imagen a ampliar. Este parámetro es crucial para determinar el punto de partida del proceso de ampliación. |
| `upscale_method` | COMBO[STRING] | Especifica el método utilizado para ampliar la imagen latente. Diferentes métodos pueden afectar la calidad y las características de la imagen ampliada. |
| `width`   | `INT`       | El ancho deseado de la imagen ampliada. Si se establece en 0, se calculará en función de la altura para mantener la relación de aspecto. |
| `height`  | `INT`       | La altura deseada de la imagen ampliada. Si se establece en 0, se calculará en función del ancho para mantener la relación de aspecto. |
| `crop`    | COMBO[STRING] | Determina cómo se debe recortar la imagen ampliada, afectando la apariencia final y las dimensiones de la salida. |

## Salidas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La representación latente ampliada de la imagen, lista para un procesamiento o generación adicional. |
