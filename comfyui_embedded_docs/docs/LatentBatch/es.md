> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentBatch/es.md)

El nodo LatentBatch está diseñado para fusionar dos conjuntos de muestras latentes en un solo lote, redimensionando potencialmente un conjunto para que coincida con las dimensiones del otro antes de la concatenación. Esta operación facilita la combinación de diferentes representaciones latentes para tareas de procesamiento o generación posteriores.

## Entradas

| Parámetro    | Tipo de Dato | Descripción |
|--------------|-------------|-------------|
| `samples1`   | `LATENT`    | El primer conjunto de muestras latentes que se fusionarán. Desempeña un papel crucial en la determinación de la forma final del lote fusionado. |
| `samples2`   | `LATENT`    | El segundo conjunto de muestras latentes que se fusionarán. Si sus dimensiones difieren del primer conjunto, se redimensiona para garantizar la compatibilidad antes de la fusión. |

## Salidas

| Parámetro | Tipo de Dato | Descripción |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | El conjunto fusionado de muestras latentes, ahora combinado en un solo lote para su posterior procesamiento. |