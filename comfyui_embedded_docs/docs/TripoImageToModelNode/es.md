Genera modelos 3D de forma síncrona a partir de una sola imagen utilizando la API de Tripo. Este nodo toma una imagen de entrada y la convierte en un modelo 3D con varias opciones de personalización para textura, calidad y propiedades del modelo.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `imagen` | Imagen de entrada utilizada para generar el modelo 3D | IMAGE | Sí | - |
| `versión_modelo` | Versión del modelo Tripo a utilizar para la generación | COMBO | No | Múltiples opciones disponibles |
| `estilo` | Configuración de estilo para el modelo generado (predeterminado: "None") | COMBO | No | Múltiples opciones disponibles |
| `textura` | Si se deben generar texturas para el modelo (predeterminado: True) | BOOLEAN | No | - |
| `pbr` | Si se debe usar renderizado basado en física (predeterminado: True) | BOOLEAN | No | - |
| `semilla_modelo` | Semilla aleatoria para la generación del modelo (predeterminado: 42) | INT | No | - |
| `orientación` | Configuración de orientación para el modelo generado | COMBO | No | Múltiples opciones disponibles |
| `semilla_textura` | Semilla aleatoria para la generación de textura (predeterminado: 42) | INT | No | - |
| `calidad_textura` | Nivel de calidad para la generación de textura (predeterminado: "standard") | COMBO | No | "standard"<br>"detailed" |
| `alineación_de_textura` | Método de alineación para el mapeo de textura (predeterminado: "original_image") | COMBO | No | "original_image"<br>"geometry" |
| `límite_de_caras` | Número máximo de caras en el modelo generado, -1 para sin límite (predeterminado: -1) | INT | No | -1 a 500000 |
| `cuadrilátero` | Si se deben usar caras cuadriláteras en lugar de triángulos (predeterminado: False) | BOOLEAN | No | - |
| `geometry_quality` | Nivel de calidad para la generación de geometría (predeterminado: "standard") | COMBO | No | "standard"<br>"detailed" |

**Nota:** El parámetro `image` es obligatorio y debe proporcionarse para que el nodo funcione. Si no se proporciona una imagen, el nodo generará un RuntimeError.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `archivo_de_modelo` | El archivo de modelo 3D generado (solo para compatibilidad hacia atrás) | STRING |
| `id_de_tarea_de_modelo` | El ID de tarea para rastrear el proceso de generación del modelo | MODEL_TASK_ID |
| `GLB` | El modelo 3D generado en formato GLB | FILE3DGLB |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToModelNode/es.md)

---
**Source fingerprint (SHA-256):** `1342de2f9788fac504fa0cfa248d011c04a8874307bb26dac86a7ced43a2809e`
