> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SoniloTextToMusic/es.md)

El nodo Sonilo Text to Music genera música a partir de una descripción de texto utilizando el modelo de IA de Sonilo. Proporcionas un *prompt* que describe la música que deseas, y el nodo envía una solicitud al servicio de Sonilo para crear un archivo de audio. Puedes especificar una duración objetivo o dejar que el modelo la infiera a partir de tu *prompt*.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | N/A | *Prompt* de texto que describe la música a generar. Este es un campo obligatorio. |
| `duration` | INT | No | 0 a 360 | Duración objetivo en segundos. Establecer en 0 para que el modelo infiera la duración a partir del *prompt*. Máximo: 6 minutos (360 segundos). Por defecto: 0. |
| `seed` | INT | No | 0 a 18446744073709551615 | Semilla para reproducibilidad. Actualmente es ignorada por el servicio de Sonilo, pero se mantiene para la consistencia del grafo. Por defecto: 0. |

**Nota:** La entrada `seed` se proporciona para la consistencia del flujo de trabajo, pero actualmente no afecta la salida del servicio de Sonilo.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `audio` | AUDIO | La música generada como un archivo de audio. |