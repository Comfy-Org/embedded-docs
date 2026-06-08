El nodo Video Slice permite extraer un segmento específico de un video. Puedes definir un tiempo de inicio y una duración para recortar el video, o simplemente saltar los fotogramas iniciales. Si la duración solicitada es mayor que el video restante, el nodo puede devolver lo disponible o generar un error.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `video` | El video de entrada que se va a segmentar. | VIDEO | Sí | - |
| `hora de inicio` | Tiempo de inicio en segundos (predeterminado: 0.0). | FLOAT | No | -1e5 a 1e5 |
| `duración` | Duración en segundos, o 0 para duración ilimitada (predeterminado: 0.0). | FLOAT | No | 0.0 y superior |
| `duración estricta` | Si es Verdadero, cuando no sea posible cumplir con la duración especificada, se generará un error (predeterminado: Falso). | BOOLEAN | No | - |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `video` | El segmento de video recortado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Video Slice/es.md)

---
**Source fingerprint (SHA-256):** `5e3e3e69931a25183eb01b7b87ec12cbf9f5a748781993dcbeec7a6d5f7260c1`
