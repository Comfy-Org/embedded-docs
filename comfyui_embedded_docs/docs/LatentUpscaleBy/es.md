
El nodo LatentUpscaleBy está diseñado para ampliar las representaciones latentes de imágenes. Permite el ajuste del factor de escala y el método de ampliación, proporcionando flexibilidad en la mejora de la resolución de muestras latentes.

## Entradas

| Parámetro     | Data Type | Descripción |
|---------------|--------------|-------------|
| `samples`     | `LATENT`     | La representación latente de las imágenes a ampliar. Este parámetro es crucial para determinar los datos de entrada que se someterán al proceso de ampliación. |
| `upscale_method` | COMBO[STRING] | Especifica el método utilizado para ampliar las muestras latentes. La elección del método puede afectar significativamente la calidad y las características del resultado ampliado. |
| `scale_by`    | `FLOAT`      | Determina el factor por el cual se escalan las muestras latentes. Este parámetro influye directamente en la resolución del resultado, permitiendo un control preciso sobre el proceso de ampliación. |

## Salidas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La representación latente ampliada, lista para un procesamiento o tareas de generación adicionales. Esta salida es esencial para mejorar la resolución de imágenes generadas o para operaciones posteriores del modelo. |
