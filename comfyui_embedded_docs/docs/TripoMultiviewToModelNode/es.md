> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMultiviewToModelNode/es.md)

Este nodo genera modelos 3D de forma síncrona utilizando la API de Tripo mediante el procesamiento de hasta cuatro imágenes que muestran diferentes vistas de un objeto. Requiere una imagen frontal y al menos una vista adicional (izquierda, posterior o derecha) para crear un modelo 3D completo con opciones de textura y material.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sí | - | Imagen de vista frontal del objeto (requerida) |
| `image_left` | IMAGE | No | - | Imagen de vista izquierda del objeto |
| `image_back` | IMAGE | No | - | Imagen de vista posterior del objeto |
| `image_right` | IMAGE | No | - | Imagen de vista derecha del objeto |
| `model_version` | COMBO | No | Múltiples opciones disponibles | Versión del modelo Tripo a utilizar para la generación |
| `orientation` | COMBO | No | Múltiples opciones disponibles | Configuración de orientación para el modelo 3D |
| `texture` | BOOLEAN | No | - | Si generar texturas para el modelo (valor por defecto: True) |
| `pbr` | BOOLEAN | No | - | Si generar materiales PBR (Renderizado Basado en Física) (valor por defecto: True) |
| `model_seed` | INT | No | - | Semilla aleatoria para la generación del modelo (valor por defecto: 42) |
| `texture_seed` | INT | No | - | Semilla aleatoria para la generación de texturas (valor por defecto: 42) |
| `texture_quality` | COMBO | No | "standard"<br>"detailed" | Nivel de calidad para la generación de texturas (valor por defecto: "standard") |
| `texture_alignment` | COMBO | No | "original_image"<br>"geometry" | Método para alinear texturas al modelo (valor por defecto: "original_image") |
| `face_limit` | INT | No | -1 a 500000 | Número máximo de caras en el modelo generado, -1 para sin límite (valor por defecto: -1) |
| `quad` | BOOLEAN | No | - | Si generar geometría basada en cuadrículas en lugar de triángulos (valor por defecto: False) |

**Nota:** La imagen frontal (`image`) es siempre requerida. Se debe proporcionar al menos una imagen de vista adicional (`image_left`, `image_back`, o `image_right`) para el procesamiento multivista.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model_file` | STRING | Ruta de archivo o identificador para el modelo 3D generado |
| `model task_id` | MODEL_TASK_ID | Identificador de tarea para rastrear el proceso de generación del modelo |