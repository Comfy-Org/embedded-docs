> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageGenerationNode/es.md)

El nodo Kling Image Generation genera imágenes a partir de prompts de texto con la opción de utilizar una imagen de referencia como guía. Crea una o más imágenes basadas en tu descripción textual y configuraciones de referencia, luego devuelve las imágenes generadas como salida.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | - | Prompt de texto positivo |
| `negative_prompt` | STRING | Sí | - | Prompt de texto negativo |
| `image_type` | COMBO | Sí | Opciones de KlingImageGenImageReferenceType<br>(extraídas del código fuente) | Selección del tipo de referencia de imagen |
| `image_fidelity` | FLOAT | Sí | 0.0 - 1.0 | Intensidad de referencia para imágenes cargadas por el usuario (valor por defecto: 0.5) |
| `human_fidelity` | FLOAT | Sí | 0.0 - 1.0 | Similitud de referencia del sujeto (valor por defecto: 0.45) |
| `model_name` | COMBO | Sí | "kling-v1"<br>(y otras opciones de KlingImageGenModelName) | Selección del modelo para generación de imágenes (valor por defecto: "kling-v1") |
| `aspect_ratio` | COMBO | Sí | "16:9"<br>(y otras opciones de KlingImageGenAspectRatio) | Relación de aspecto para las imágenes generadas (valor por defecto: "16:9") |
| `n` | INT | Sí | 1 - 9 | Número de imágenes generadas (valor por defecto: 1) |
| `image` | IMAGE | No | - | Imagen de referencia opcional |

**Restricciones de Parámetros:**
- El parámetro `image` es opcional, pero cuando se proporciona, el modelo kling-v1 no admite imágenes de referencia
- El prompt y el prompt negativo tienen limitaciones de longitud máxima (MAX_PROMPT_LENGTH_IMAGE_GEN)
- Cuando no se proporciona una imagen de referencia, el parámetro `image_type` se establece automáticamente en None

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | IMAGE | Imagen(es) generada(s) basadas en los parámetros de entrada |