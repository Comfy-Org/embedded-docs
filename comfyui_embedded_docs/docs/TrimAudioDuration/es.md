> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrimAudioDuration/es.md)

El nodo TrimAudioDuration permite recortar un segmento de tiempo específico de un archivo de audio. Puedes especificar cuándo comenzar el recorte y cuánto debe durar el clip de audio resultante. El nodo funciona convirtiendo los valores de tiempo a posiciones de frames de audio y extrayendo la porción correspondiente de la forma de onda de audio.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | Sí | - | La entrada de audio que se va a recortar |
| `start_index` | FLOAT | Sí | -0xffffffffffffffff a 0xffffffffffffffff | Tiempo de inicio en segundos, puede ser negativo para contar desde el final (admite subsegundos). Por defecto: 0.0 |
| `duration` | FLOAT | Sí | 0.0 a 0xffffffffffffffff | Duración en segundos. Por defecto: 60.0 |

**Nota:** El tiempo de inicio debe ser menor que el tiempo final y estar dentro de la longitud del audio. Los valores de inicio negativos cuentan hacia atrás desde el final del audio.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `audio` | AUDIO | El segmento de audio recortado con el tiempo de inicio y duración especificados |
