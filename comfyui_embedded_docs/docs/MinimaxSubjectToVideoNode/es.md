> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxSubjectToVideoNode/es.md)

Genera videos de forma síncrona basándose en una imagen, un texto descriptivo y parámetros opcionales utilizando la API de MiniMax. Este nodo toma una imagen de sujeto y una descripción textual para crear un video utilizando el servicio de generación de video de MiniMax.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `subject` | IMAGE | Sí | - | Imagen del sujeto a utilizar como referencia para la generación del video |
| `prompt_text` | STRING | Sí | - | Texto descriptivo que guía la generación del video (valor por defecto: cadena vacía) |
| `model` | COMBO | No | "S2V-01"<br> | Modelo a utilizar para la generación del video (valor por defecto: "S2V-01") |
| `seed` | INT | No | 0 a 18446744073709551615 | Semilla aleatoria utilizada para crear el ruido (valor por defecto: 0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El video generado basado en la imagen de sujeto y el texto descriptivo de entrada |