
El nodo RebatchLatents está diseñado para reorganizar un lote de representaciones latentes en una nueva configuración de lote, basado en un tamaño de lote especificado. Asegura que las muestras latentes se agrupen adecuadamente, manejando variaciones en dimensiones y tamaños, para facilitar un procesamiento o inferencia de modelo adicional.

## Entradas

| Parámetro    | Data Type | Descripción |
|--------------|-------------|-------------|
| `latents`    | `LATENT`    | El parámetro 'latents' representa las representaciones latentes de entrada a reorganizar. Es crucial para determinar la estructura y el contenido del lote de salida. |
| `batch_size` | `INT`      | El parámetro 'batch_size' especifica el número deseado de muestras por lote en la salida. Influye directamente en la agrupación y división de los latentes de entrada en nuevos lotes. |

## Salidas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La salida es un lote reorganizado de representaciones latentes, ajustado según el tamaño de lote especificado. Facilita un procesamiento o análisis adicional. |
