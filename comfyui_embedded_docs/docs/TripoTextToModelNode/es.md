> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextToModelNode/es.md)

Genera modelos 3D de forma síncrona basándose en un texto descriptivo utilizando la API de Tripo. Este nodo toma una descripción textual y crea un modelo 3D con propiedades opcionales de textura y materiales.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | - | Descripción textual para generar el modelo 3D (entrada multilínea) |
| `negative_prompt` | STRING | No | - | Descripción textual de qué evitar en el modelo generado (entrada multilínea) |
| `model_version` | COMBO | No | Múltiples opciones disponibles | La versión del modelo Tripo a utilizar para la generación |
| `style` | COMBO | No | Múltiples opciones disponibles | Configuración de estilo para el modelo generado (valor por defecto: "None") |
| `texture` | BOOLEAN | No | - | Si generar texturas para el modelo (valor por defecto: True) |
| `pbr` | BOOLEAN | No | - | Si generar materiales PBR (Renderizado Basado en Física) (valor por defecto: True) |
| `image_seed` | INT | No | - | Semilla aleatoria para la generación de imágenes (valor por defecto: 42) |
| `model_seed` | INT | No | - | Semilla aleatoria para la generación del modelo (valor por defecto: 42) |
| `texture_seed` | INT | No | - | Semilla aleatoria para la generación de texturas (valor por defecto: 42) |
| `texture_quality` | COMBO | No | "standard"<br>"detailed" | Nivel de calidad para la generación de texturas (valor por defecto: "standard") |
| `face_limit` | INT | No | -1 a 500000 | Número máximo de caras en el modelo generado, -1 para sin límite (valor por defecto: -1) |
| `quad` | BOOLEAN | No | - | Si generar geometría basada en cuadrículas en lugar de triángulos (valor por defecto: False) |

**Nota:** El parámetro `prompt` es obligatorio y no puede estar vacío. Si no se proporciona ningún texto descriptivo, el nodo generará un error.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model_file` | STRING | El archivo del modelo 3D generado |
| `model task_id` | MODEL_TASK_ID | El identificador único de tarea para el proceso de generación del modelo |