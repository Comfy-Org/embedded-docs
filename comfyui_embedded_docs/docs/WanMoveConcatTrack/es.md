# WanMoveConcatTrack

El nodo WanMoveConcatTrack combina dos conjuntos de datos de seguimiento de movimiento en una única secuencia más larga. Funciona uniendo las rutas de seguimiento y las máscaras de visibilidad de las pistas de entrada a lo largo de sus respectivas dimensiones. Si solo se proporciona una pista de entrada, simplemente transmite esos datos sin cambios.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `pistas_1` | El primer conjunto de datos de seguimiento de movimiento que se concatenará. | TRACKS | Sí |  |
| `pistas_2` | Un segundo conjunto opcional de datos de seguimiento de movimiento. Si no se proporciona, `pistas_1` se pasa directamente a la salida. | TRACKS | No |  |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `tracks` | Los datos de seguimiento de movimiento concatenados, que contienen la combinación de `track_path` y `track_visibility` de las entradas. | TRACKS |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveConcatTrack/es.md)

---
**Source fingerprint (SHA-256):** `d9b4c00291c6fa8e17bf54ecdcd16f7f6874159fe8cebebe66568dc2a744868f`
