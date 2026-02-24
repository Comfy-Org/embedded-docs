> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProFirstLastFrameNode/es.md)

Este nodo utiliza el modelo Kling AI para generar un vídeo. Requiere una imagen inicial y un texto descriptivo (prompt). Opcionalmente, puedes proporcionar una imagen final o hasta seis imágenes de referencia para guiar el contenido y el estilo del vídeo. El nodo procesa estas entradas para crear un vídeo de una duración y resolución específicas.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model_name` | COMBO | Sí | `"kling-video-o1"` | El modelo específico de Kling AI a utilizar para la generación del vídeo. |
| `prompt` | STRING | Sí | - | Un texto descriptivo que detalla el contenido del vídeo. Puede incluir descripciones tanto positivas como negativas. |
| `duration` | INT | Sí | 3 a 10 | La duración deseada del vídeo generado, en segundos (valor por defecto: 5). |
| `first_frame` | IMAGE | Sí | - | La imagen de inicio para la secuencia de vídeo. |
| `end_frame` | IMAGE | No | - | Un fotograma final opcional para el vídeo. No se puede utilizar simultáneamente con `reference_images`. |
| `reference_images` | IMAGE | No | - | Hasta 6 imágenes de referencia adicionales. |
| `resolution` | COMBO | No | `"1080p"`<br>`"720p"` | La resolución de salida para el vídeo generado (valor por defecto: "1080p"). |

**Restricciones importantes:**

* La entrada `end_frame` no se puede utilizar al mismo tiempo que la entrada `reference_images`.
* Si no se proporciona un `end_frame` ni ninguna `reference_images`, la `duration` solo se puede establecer en 5 o 10 segundos.
* Todas las imágenes de entrada (`first_frame`, `end_frame` y cualquier `reference_images`) deben tener una dimensión mínima de 300 píxeles tanto en ancho como en alto.
* La relación de aspecto de todas las imágenes de entrada debe estar entre 1:2.5 y 2.5:1.
* Se pueden proporcionar un máximo de 6 imágenes a través de la entrada `reference_images`.
* El texto del `prompt` debe tener una longitud de entre 1 y 2500 caracteres.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El archivo de vídeo generado. |
