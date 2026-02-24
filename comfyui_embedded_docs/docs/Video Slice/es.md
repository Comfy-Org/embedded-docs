> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Video Slice/es.md)

El nodo Video Slice permite extraer un segmento específico de un vídeo. Puedes definir un tiempo de inicio y una duración para recortar el vídeo, o simplemente omitir los fotogramas iniciales. Si la duración solicitada es mayor que el vídeo restante, el nodo puede devolver lo que esté disponible o generar un error.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Sí | - | El vídeo de entrada que se va a segmentar. |
| `start_time` | FLOAT | No | -1e5 a 1e5 | El tiempo de inicio en segundos desde el cual comenzar el segmento. Un valor negativo omitirá fotogramas desde el principio del vídeo. (por defecto: 0.0) |
| `duration` | FLOAT | No | 0.0 y superior | La longitud del segmento en segundos. Un valor de 0.0 significa que el nodo devolverá todo el vídeo desde el tiempo de inicio hasta el final. (por defecto: 0.0) |
| `strict_duration` | BOOLEAN | No | - | Si se establece en True, el nodo generará un error si no se puede cumplir la duración solicitada (por ejemplo, si el segmento excedería el final del vídeo). Si es False, devolverá el vídeo disponible hasta el final. (por defecto: False) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `video` | VIDEO | El segmento de vídeo recortado. |