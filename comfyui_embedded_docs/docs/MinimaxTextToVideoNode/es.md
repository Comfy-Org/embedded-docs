> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxTextToVideoNode/es.md)

Genera videos de forma síncrona basándose en un prompt y parámetros opcionales utilizando la API de MiniMax. Este nodo crea contenido de video a partir de descripciones de texto conectándose al servicio de texto a video de MiniMax.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `texto_de_indicación` | STRING | Sí | - | Prompt de texto para guiar la generación del video |
| `modelo` | COMBO | No | "T2V-01"<br>"T2V-01-Director" | Modelo a utilizar para la generación de video (por defecto: "T2V-01") |
| `semilla` | INT | No | 0 a 18446744073709551615 | La semilla aleatoria utilizada para crear el ruido (por defecto: 0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El video generado basado en el prompt de entrada |
