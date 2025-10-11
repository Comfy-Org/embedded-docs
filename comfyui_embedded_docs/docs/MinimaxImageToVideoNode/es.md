> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxImageToVideoNode/es.md)

Genera videos de forma síncrona basándose en una imagen, un texto descriptivo y parámetros opcionales utilizando la API de MiniMax. Este nodo toma una imagen de entrada y una descripción textual para crear una secuencia de video, con varias opciones de modelo y configuraciones disponibles.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sí | - | Imagen a utilizar como primer fotograma para la generación del video |
| `prompt_text` | STRING | Sí | - | Texto descriptivo para guiar la generación del video (valor por defecto: cadena vacía) |
| `model` | COMBO | Sí | "I2V-01-Director"<br>"I2V-01"<br>"I2V-01-live" | Modelo a utilizar para la generación del video (valor por defecto: "I2V-01") |
| `seed` | INT | No | 0 a 18446744073709551615 | Semilla aleatoria utilizada para crear el ruido (valor por defecto: 0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | La salida de video generada |