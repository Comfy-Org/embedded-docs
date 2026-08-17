# Corte de Video

El nodo Video Slice permite extraer un segmento específico de un video. Puedes definir un tiempo de inicio y una duración para recortar el video, o simplemente omitir los primeros fotogramas. Si la duración solicitada es mayor que el video restante, el nodo puede devolver lo que esté disponible o generar un error.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `video` | El video de entrada que se va a cortar. | VIDEO | Sí | - |
| `start_time` | Tiempo de inicio en segundos (predeterminado: 0.0). | FLOAT | No | -1e5 a 1e5 |
| `duration` | Duración en segundos, o 0 para duración ilimitada (predeterminado: 0.0). | FLOAT | No | 0.0 y superior |
| `strict_duration` | Si es True, cuando la duración especificada no sea posible, se generará un error (predeterminado: False). | BOOLEAN | No | - |

Nota: Cuando `duration` es 0, el nodo corta desde `start_time` hasta el final del video. Si el segmento solicitado no se puede crear — por ejemplo, porque `start_time` está más allá del final del video — el nodo genera un error.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `video` | El segmento de video recortado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Video Slice/es.md)

---
**Source fingerprint (SHA-256):** `439b76528742c1fbe230eee9502e945847ae99a58a9bd81a7a7dc3b20e15d450`
