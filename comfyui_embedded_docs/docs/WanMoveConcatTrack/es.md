> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveConcatTrack/es.md)

El nodo WanMoveConcatTrack combina dos conjuntos de datos de seguimiento de movimiento en una única secuencia más larga. Funciona uniendo las trayectorias de seguimiento y las máscaras de visibilidad de las pistas de entrada a lo largo de sus respectivas dimensiones. Si solo se proporciona una entrada de seguimiento, simplemente pasa esos datos sin cambios.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `tracks_1` | TRACKS | Sí | | El primer conjunto de datos de seguimiento de movimiento a concatenar. |
| `tracks_2` | TRACKS | No | | Un segundo conjunto opcional de datos de seguimiento de movimiento. Si no se proporciona, `tracks_1` se pasa directamente a la salida. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `tracks` | TRACKS | Los datos de seguimiento de movimiento concatenados, que contienen la combinación de `track_path` y `track_visibility` de las entradas. |
