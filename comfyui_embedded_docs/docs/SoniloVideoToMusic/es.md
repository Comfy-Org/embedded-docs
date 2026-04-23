> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SoniloVideoToMusic/es.md)

Genera música a partir de video utilizando el modelo de IA de Sonilo. Este nodo analiza el contenido de un video de entrada y crea una pieza musical acorde. Utiliza un servicio externo de IA para procesar el video y generar el audio.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Sí | - | Video de entrada a partir del cual generar la música. Duración máxima: 6 minutos. |
| `prompt` | STRING | No | - | Sugerencia de texto opcional para guiar la generación musical. Déjalo vacío para obtener la mejor calidad: el modelo analizará completamente el contenido del video. (valor por defecto: cadena vacía) |
| `seed` | INT | No | 0 a 18446744073709551615 | Semilla para reproducibilidad. Actualmente es ignorada por el servicio Sonilo, pero se mantiene para la consistencia del grafo. (valor por defecto: 0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `audio` | AUDIO | La música generada como un archivo de audio. |