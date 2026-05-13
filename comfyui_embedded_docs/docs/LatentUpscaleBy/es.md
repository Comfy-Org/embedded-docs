> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscaleBy/es.md)

El nodo LatentUpscaleBy está diseñado para escalar representaciones latentes de imágenes. Permite ajustar el factor de escala y el método de escalado, ofreciendo flexibilidad para mejorar la resolución de muestras latentes.

## Entradas

| Parámetro      | Tipo de Dato | Descripción |
|----------------|--------------|-------------|
| `muestras`      | `LATENT`     | La representación latente de las imágenes que se escalarán. Este parámetro es crucial para determinar los datos de entrada que se someterán al proceso de escalado. |
| `método_escala` | COMBO[STRING] | Especifica el método utilizado para escalar las muestras latentes. La elección del método puede afectar significativamente la calidad y las características del resultado escalado. |
| `escalar_por`     | `FLOAT`      | Determina el factor por el cual se escalan las muestras latentes. Este parámetro influye directamente en la resolución de la salida, permitiendo un control preciso sobre el proceso de escalado. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|--------------|-------------|
| `latent`  | `LATENT`     | La representación latente escalada, lista para procesos posteriores o tareas de generación. Esta salida es esencial para mejorar la resolución de imágenes generadas o para operaciones posteriores del modelo. |