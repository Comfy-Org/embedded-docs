# WanMoveConcatTrack

El nodo WanMoveConcatTrack combina dos conjuntos de datos de seguimiento de movimiento en una única secuencia más larga. Funciona uniendo las rutas de seguimiento y las máscaras de visibilidad de los seguimientos de entrada a lo largo de sus respectivas dimensiones. Si solo se proporciona un seguimiento de entrada, simplemente pasa esos datos sin cambios.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `pistas_1` | El primer conjunto de datos de seguimiento de movimiento que se concatenará. | TRACKS | Sí |  |
| `pistas_2` | Un segundo conjunto opcional de datos de seguimiento de movimiento. Si no se proporciona, `tracks_1` se pasa directamente a la salida. | TRACKS | No |  |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `tracks` | Los datos de seguimiento de movimiento concatenados, que contienen el `track_path` y `track_visibility` combinados de las entradas. | TRACKS |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveConcatTrack/es.md)

---
**Source fingerprint (SHA-256):** `0507c42dce5d481fe5dc5aa1116c9df279f236419f548ea3eff5d824d0d22653`
