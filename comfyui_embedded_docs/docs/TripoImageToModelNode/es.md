> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToModelNode/es.md)

Genera modelos 3D de forma síncrona basándose en una sola imagen utilizando la API de Tripo. Este nodo toma una imagen de entrada y la convierte en un modelo 3D con varias opciones de personalización para textura, calidad y propiedades del modelo.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sí | - | Imagen de entrada utilizada para generar el modelo 3D |
| `model_version` | COMBO | No | Múltiples opciones disponibles | La versión del modelo Tripo a utilizar para la generación |
| `style` | COMBO | No | Múltiples opciones disponibles | Configuración de estilo para el modelo generado (valor por defecto: "None") |
| `texture` | BOOLEAN | No | - | Si generar texturas para el modelo (valor por defecto: True) |
| `pbr` | BOOLEAN | No | - | Si utilizar Renderizado Basado en Física (valor por defecto: True) |
| `model_seed` | INT | No | - | Semilla aleatoria para la generación del modelo (valor por defecto: 42) |
| `orientation` | COMBO | No | Múltiples opciones disponibles | Configuración de orientación para el modelo generado |
| `texture_seed` | INT | No | - | Semilla aleatoria para la generación de texturas (valor por defecto: 42) |
| `texture_quality` | COMBO | No | "standard"<br>"detailed" | Nivel de calidad para la generación de texturas (valor por defecto: "standard") |
| `texture_alignment` | COMBO | No | "original_image"<br>"geometry" | Método de alineación para el mapeo de texturas (valor por defecto: "original_image") |
| `face_limit` | INT | No | -1 a 500000 | Número máximo de caras en el modelo generado, -1 para sin límite (valor por defecto: -1) |
| `quad` | BOOLEAN | No | - | Si utilizar caras cuadriláteras en lugar de triángulos (valor por defecto: False) |

**Nota:** El parámetro `image` es obligatorio y debe proporcionarse para que el nodo funcione. Si no se proporciona ninguna imagen, el nodo generará un RuntimeError.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model_file` | STRING | El archivo del modelo 3D generado |
| `model task_id` | MODEL_TASK_ID | El ID de tarea para rastrear el proceso de generación del modelo |