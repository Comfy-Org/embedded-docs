Este nodo está diseñado para modificar el comportamiento de un modelo CLIP al establecer una capa específica como la última en ejecutarse. Permite la personalización de la profundidad de procesamiento dentro del modelo CLIP, lo que puede afectar la salida del modelo al limitar la cantidad de información procesada.

## Entradas

| Parámetro            | Data Type | Descripción |
|---------------------|--------------|-------------|
| `clip`               | `CLIP`      | El modelo CLIP que se va a modificar. Este parámetro permite que el nodo interactúe directamente y altere la estructura del modelo CLIP. |
| `stop_at_clip_layer` | `INT`       | Especifica la capa en la que el modelo CLIP debe dejar de procesar. Esto permite controlar la profundidad de cálculo y se puede utilizar para ajustar el comportamiento o rendimiento del modelo. |

## Salidas

| Parámetro | Data Type | Descripción |
|-----------|-------------|-------------|
| `clip`    | CLIP      | El modelo CLIP modificado con la capa especificada establecida como la última. Esta salida permite un uso o análisis adicional del modelo ajustado.
