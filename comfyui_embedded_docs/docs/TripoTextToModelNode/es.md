> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextToModelNode/es.md)

Genera modelos 3D de forma síncrona basándose en un prompt de texto mediante la API de Tripo. Este nodo toma una descripción textual y crea un modelo 3D con propiedades opcionales de textura y material.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | - | Descripción textual para generar el modelo 3D (entrada multilínea) |
| `negative_prompt` | STRING | No | - | Descripción textual de lo que se debe evitar en el modelo generado (entrada multilínea) |
| `model_version` | COMBO | No | Múltiples opciones disponibles | Versión del modelo Tripo a utilizar para la generación (predeterminado: v2.5-20250123) |
| `style` | COMBO | No | Múltiples opciones disponibles | Configuración de estilo para el modelo generado (predeterminado: "Ninguno") |
| `texture` | BOOLEAN | No | - | Si se deben generar texturas para el modelo (predeterminado: Verdadero) |
| `pbr` | BOOLEAN | No | - | Si se deben generar materiales PBR (renderizado basado en física) (predeterminado: Verdadero) |
| `image_seed` | INT | No | - | Semilla aleatoria para la generación de imágenes (predeterminado: 42) |
| `model_seed` | INT | No | - | Semilla aleatoria para la generación del modelo (predeterminado: 42) |
| `texture_seed` | INT | No | - | Semilla aleatoria para la generación de texturas (predeterminado: 42) |
| `texture_quality` | COMBO | No | "standard"<br>"detailed" | Nivel de calidad para la generación de texturas (predeterminado: "standard") |
| `face_limit` | INT | No | -1 a 2000000 | Número máximo de caras en el modelo generado, -1 para sin límite (predeterminado: -1) |
| `quad` | BOOLEAN | No | - | Si se debe generar geometría basada en cuadrángulos en lugar de triángulos (predeterminado: Falso) |
| `geometry_quality` | COMBO | No | "standard"<br>"detailed" | Nivel de calidad para la generación de geometría (predeterminado: "standard") |

**Nota:** El parámetro `prompt` es obligatorio y no puede estar vacío. Si no se proporciona un prompt, el nodo generará un error.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model_file` | STRING | El archivo del modelo 3D generado (solo para compatibilidad hacia atrás) |
| `model task_id` | MODEL_TASK_ID | El identificador único de la tarea para el proceso de generación del modelo |
| `GLB` | FILE3DGLB | El modelo 3D generado en formato GLB |

---
**Source fingerprint (SHA-256):** `f73316e0a50adfb6fe22ca6a20a2a5b36a6597abf0f4ddae9183d9e4a45cb46d`
