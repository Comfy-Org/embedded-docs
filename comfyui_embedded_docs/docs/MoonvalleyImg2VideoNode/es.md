> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoonvalleyImg2VideoNode/es.md)

El nodo Moonvalry Marey Image to Video transforma una imagen de referencia en un video utilizando la API de Moonvalley. Toma una imagen de entrada y un texto descriptivo (prompt) para generar un video con una resolución, ajustes de calidad y controles creativos específicos. El nodo maneja todo el proceso desde la carga de la imagen hasta la generación y descarga del video.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen de referencia utilizada para generar el video |
| `prompt` | STRING | Sí | - | Descripción textual para la generación del video (entrada multilínea) |
| `negative_prompt` | STRING | No | - | Texto de indicación negativa para excluir elementos no deseados (valor por defecto: lista extensa de indicaciones negativas) |
| `resolution` | COMBO | No | "16:9 (1920 x 1080)"<br>"9:16 (1080 x 1920)"<br>"1:1 (1152 x 1152)"<br>"4:3 (1536 x 1152)"<br>"3:4 (1152 x 1536)" | Resolución del video de salida (valor por defecto: "16:9 (1920 x 1080)") |
| `prompt_adherence` | FLOAT | No | 1.0 - 20.0 | Escala de guía para el control de generación (valor por defecto: 4.5, paso: 1.0) |
| `seed` | INT | No | 0 - 4294967295 | Valor de semilla aleatoria (valor por defecto: 9, control después de generar habilitado) |
| `steps` | INT | No | 1 - 100 | Número de pasos de eliminación de ruido (valor por defecto: 33, paso: 1) |

**Restricciones:**

- La imagen de entrada debe tener dimensiones entre 300x300 píxeles y la altura/ancho máxima permitida
- La longitud del texto de indicación e indicación negativa está limitada a la longitud máxima de indicación de Moonvalley Marey

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El video generado como salida |
