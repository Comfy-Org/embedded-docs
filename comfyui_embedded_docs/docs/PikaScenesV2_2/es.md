> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaScenesV2_2/es.md)

El nodo PikaScenes v2.2 combina múltiples imágenes para crear un video que incorpora objetos de todas las imágenes de entrada. Puedes cargar hasta cinco imágenes diferentes como ingredientes y generar un video de alta calidad que las mezcle de forma fluida.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt_text` | STRING | Sí | - | Descripción textual de lo que se debe generar |
| `negative_prompt` | STRING | Sí | - | Descripción textual de lo que se debe evitar en la generación |
| `seed` | INT | Sí | - | Valor de semilla aleatoria para la generación |
| `resolution` | STRING | Sí | - | Resolución de salida para el video |
| `duration` | INT | Sí | - | Duración del video generado |
| `ingredients_mode` | COMBO | No | "creative"<br>"precise" | Modo para combinar ingredientes (por defecto: "creative") |
| `aspect_ratio` | FLOAT | No | 0.4 - 2.5 | Relación de aspecto (ancho / alto) (por defecto: 1.778) |
| `image_ingredient_1` | IMAGE | No | - | Imagen que se utilizará como ingrediente para crear un video |
| `image_ingredient_2` | IMAGE | No | - | Imagen que se utilizará como ingrediente para crear un video |
| `image_ingredient_3` | IMAGE | No | - | Imagen que se utilizará como ingrediente para crear un video |
| `image_ingredient_4` | IMAGE | No | - | Imagen que se utilizará como ingrediente para crear un video |
| `image_ingredient_5` | IMAGE | No | - | Imagen que se utilizará como ingrediente para crear un video |

**Nota:** Puedes proporcionar hasta 5 ingredientes de imagen, pero se requiere al menos una imagen para generar un video. El nodo utilizará todas las imágenes proporcionadas para crear la composición final del video.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El video generado que combina todas las imágenes de entrada |
