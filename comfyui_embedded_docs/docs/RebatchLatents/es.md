> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RebatchLatents/es.md)

El nodo RebatchLatents está diseñado para reorganizar un lote de representaciones latentes en una nueva configuración de lote, basada en un tamaño de lote especificado. Garantiza que las muestras latentes se agrupen adecuadamente, manejando variaciones en dimensiones y tamaños, para facilitar el procesamiento posterior o la inferencia del modelo.

## Entradas

| Parámetro    | Tipo de Dato | Descripción |
|--------------|-------------|-------------|
| `latentes`    | `LATENT`    | El parámetro 'latents' representa las representaciones latentes de entrada que se reorganizarán en lotes. Es crucial para determinar la estructura y el contenido del lote de salida. |
| `tamaño_lote` | `INT`      | El parámetro 'batch_size' especifica la cantidad deseada de muestras por lote en la salida. Influye directamente en la agrupación y división de las latentes de entrada en nuevos lotes. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | La salida es un lote reorganizado de representaciones latentes, ajustado según el tamaño de lote especificado. Facilita el procesamiento o análisis posterior. |