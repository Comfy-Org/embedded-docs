> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoonvalleyVideo2VideoNode/es.md)

El nodo Moonvalley Marey Video a Video transforma un video de entrada en un nuevo video basado en una descripción textual. Utiliza la API de Moonvalley para generar videos que coincidan con tu *prompt* mientras preserva las características de movimiento o pose del video original. Puedes controlar el estilo y contenido del video de salida a través de *prompts* de texto y varios parámetros de generación.

## Entradas

| Parámetro | Tipo de Datos | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | - | Describe el video a generar (entrada multilínea) |
| `negative_prompt` | STRING | No | - | Texto del *prompt* negativo (valor por defecto: lista extensa de descriptores negativos) |
| `seed` | INT | Sí | 0-4294967295 | Valor de semilla aleatoria (valor por defecto: 9) |
| `video` | VIDEO | Sí | - | El video de referencia utilizado para generar el video de salida. Debe tener al menos 5 segundos de duración. Los videos más largos de 5 segundos se recortarán automáticamente. Solo se admite formato MP4. |
| `control_type` | COMBO | No | "Motion Transfer"<br>"Pose Transfer" | Selección del tipo de control (valor por defecto: "Motion Transfer") |
| `motion_intensity` | INT | No | 0-100 | Solo se utiliza si *control_type* es 'Motion Transfer' (valor por defecto: 100) |
| `steps` | INT | Sí | 1-100 | Número de pasos de inferencia (valor por defecto: 33) |

**Nota:** El parámetro `motion_intensity` solo se aplica cuando `control_type` está configurado como "Motion Transfer". Cuando se utiliza "Pose Transfer", este parámetro se ignora.

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | La salida del video generado |