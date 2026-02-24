> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProImageToVideoNode/es.md)

Este nodo utiliza el modelo Kling AI para generar un video basado en un texto descriptivo y hasta siete imágenes de referencia. Permite controlar la relación de aspecto, duración y resolución del video. El nodo envía la solicitud a una API externa y devuelve el video generado.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model_name` | COMBO | Sí | `"kling-video-o1"` | El modelo específico de Kling a utilizar para la generación de video. |
| `prompt` | STRING | Sí | - | Un texto descriptivo que detalla el contenido del video. Puede incluir tanto descripciones positivas como negativas. El texto se normaliza automáticamente y debe tener entre 1 y 2500 caracteres. |
| `aspect_ratio` | COMBO | Sí | `"16:9"`<br>`"9:16"`<br>`"1:1"` | La relación de aspecto deseada para el video generado. |
| `duration` | INT | Sí | 3 a 10 | La duración del video en segundos. El valor se puede ajustar con un control deslizante (valor por defecto: 3). |
| `reference_images` | IMAGE | Sí | - | Hasta 7 imágenes de referencia. Cada imagen debe tener al menos 300x300 píxeles y una relación de aspecto entre 1:2.5 y 2.5:1. |
| `resolution` | COMBO | No | `"1080p"`<br>`"720p"` | La resolución de salida del video. Este parámetro es opcional (valor por defecto: "1080p"). |

**Nota:** La entrada `reference_images` acepta un máximo de 7 imágenes. Si se proporcionan más, el nodo generará un error. Cada imagen se valida para cumplir con las dimensiones mínimas y la relación de aspecto.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El archivo de video generado. |
