> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTextToImageApi/es.md)

El nodo Wan Text to Image genera imágenes basadas en descripciones de texto. Utiliza modelos de IA para crear contenido visual a partir de indicaciones escritas, admitiendo tanto texto en inglés como en chino como entrada. El nodo proporciona varios controles para ajustar el tamaño, la calidad y las preferencias de estilo de la imagen de salida.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sí | "wan2.5-t2i-preview" | Modelo a utilizar (por defecto: "wan2.5-t2i-preview") |
| `prompt` | STRING | Sí | - | Indicación utilizada para describir los elementos y características visuales, admite inglés/chino (por defecto: vacío) |
| `negative_prompt` | STRING | No | - | Indicación de texto negativa para guiar lo que se debe evitar (por defecto: vacío) |
| `width` | INT | No | 768-1440 | Ancho de la imagen en píxeles (por defecto: 1024, paso: 32) |
| `height` | INT | No | 768-1440 | Alto de la imagen en píxeles (por defecto: 1024, paso: 32) |
| `seed` | INT | No | 0-2147483647 | Semilla a utilizar para la generación (por defecto: 0) |
| `prompt_extend` | BOOLEAN | No | - | Si se debe mejorar la indicación con asistencia de IA (por defecto: True) |
| `watermark` | BOOLEAN | No | - | Si se debe agregar una marca de agua de "Generado por IA" al resultado (por defecto: True) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | IMAGE | La imagen generada basada en la indicación de texto |