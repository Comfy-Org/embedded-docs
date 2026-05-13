> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToModelNode/es.md)

Genera modelos 3D de forma síncrona a partir de una sola imagen utilizando la API de Tripo. Este nodo toma una imagen de entrada y la convierte en un modelo 3D con varias opciones de personalización para textura, calidad y propiedades del modelo.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `imagen` | IMAGE | Sí | - | Imagen de entrada utilizada para generar el modelo 3D |
| `versión_modelo` | COMBO | No | Múltiples opciones disponibles | Versión del modelo Tripo a utilizar para la generación |
| `estilo` | COMBO | No | Múltiples opciones disponibles | Configuración de estilo para el modelo generado (predeterminado: "None") |
| `textura` | BOOLEAN | No | - | Si se deben generar texturas para el modelo (predeterminado: True) |
| `pbr` | BOOLEAN | No | - | Si se debe usar renderizado basado en física (predeterminado: True) |
| `semilla_modelo` | INT | No | - | Semilla aleatoria para la generación del modelo (predeterminado: 42) |
| `orientación` | COMBO | No | Múltiples opciones disponibles | Configuración de orientación para el modelo generado |
| `semilla_textura` | INT | No | - | Semilla aleatoria para la generación de textura (predeterminado: 42) |
| `calidad_textura` | COMBO | No | "standard"<br>"detailed" | Nivel de calidad para la generación de textura (predeterminado: "standard") |
| `alineación_de_textura` | COMBO | No | "original_image"<br>"geometry" | Método de alineación para el mapeo de textura (predeterminado: "original_image") |
| `límite_de_caras` | INT | No | -1 a 500000 | Número máximo de caras en el modelo generado, -1 para sin límite (predeterminado: -1) |
| `cuadrilátero` | BOOLEAN | No | - | Si se deben usar caras cuadriláteras en lugar de triángulos (predeterminado: False) |
| `geometry_quality` | COMBO | No | "standard"<br>"detailed" | Nivel de calidad para la generación de geometría (predeterminado: "standard") |

**Nota:** El parámetro `image` es obligatorio y debe proporcionarse para que el nodo funcione. Si no se proporciona una imagen, el nodo generará un RuntimeError.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `id_de_tarea_de_modelo` | STRING | El archivo de modelo 3D generado (solo para compatibilidad hacia atrás) |
| `GLB` | MODEL_TASK_ID | El ID de tarea para rastrear el proceso de generación del modelo |
| `GLB` | FILE3DGLB | El modelo 3D generado en formato GLB |

---
**Source fingerprint (SHA-256):** `1342de2f9788fac504fa0cfa248d011c04a8874307bb26dac86a7ced43a2809e`
