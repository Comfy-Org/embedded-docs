El nodo LatentBatch está diseñado para fusionar dos conjuntos de muestras latentes en un solo lote, potencialmente redimensionando un conjunto para que coincida con las dimensiones del otro antes de la concatenación. Esta operación facilita la combinación de diferentes representaciones latentes para tareas de procesamiento o generación adicionales.

## Entradas

| Parámetro    | Data Type | Descripción |
|--------------|-------------|-------------|
| `samples1`   | `LATENT`    | El primer conjunto de muestras latentes a fusionar. Juega un papel crucial en la determinación de la forma final del lote fusionado. |
| `samples2`   | `LATENT`    | El segundo conjunto de muestras latentes a fusionar. Si sus dimensiones difieren del primer conjunto, se redimensiona para asegurar la compatibilidad antes de la fusión. |

## Salidas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | El conjunto fusionado de muestras latentes, ahora combinado en un solo lote para un procesamiento adicional. |
