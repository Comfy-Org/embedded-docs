# VideoTrim

Este nodo recorta un video a una ventana de tiempo elegida al establecer un tiempo de inicio y una duración. También ofrece un modo estricto que genera un error cuando la duración solicitada no puede lograrse.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `video` | El video a recortar. | VIDEO | Sí | — |
| `trim` | Ventana de recorte que usa fotogramas de inicio/fin. La ventana se convierte en un tiempo de inicio (en segundos desde el comienzo del video) y una duración (en segundos). Cuando tanto el tiempo de inicio como la duración son 0, el video se devuelve sin ningún recorte. | VIDEO_EDIT | Sí | start_time: >= 0, por defecto 0<br>duration: >= 0, por defecto 0 |
| `strict_duration` | Si es True, cuando la duración especificada no es posible, se generará un error. (por defecto: False) | BOOLEAN | No | true<br>false |

Nota: La duración del recorte debe ser >= 0; los valores negativos generan un error. La ventana de recorte solicitada debe caber dentro del video de origen. Si el recorte no puede aplicarse, se genera un error que informa de la duración del origen, el tiempo de inicio y la duración objetivo.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `video` | El video recortado. Cuando la ventana de recorte está vacía (tiempo de inicio y duración ambos en 0), el video original se devuelve sin cambios. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTrim/es.md)

---
**Source fingerprint (SHA-256):** `ba8f8ccbae7e8aebda553810b81ccaa427d45523142bd00746c4e2f4e5b41a1b`
