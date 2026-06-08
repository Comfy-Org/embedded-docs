Genera modelos 3D de forma síncrona basándose en un prompt de texto mediante la API de Tripo. Este nodo toma una descripción textual y crea un modelo 3D con propiedades opcionales de textura y material.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `prompt` | Descripción textual para generar el modelo 3D (entrada multilínea) | STRING | Sí | - |
| `promoción_negativa` | Descripción textual de lo que se debe evitar en el modelo generado (entrada multilínea) | STRING | No | - |
| `versión_del_modelo` | Versión del modelo Tripo a utilizar para la generación (predeterminado: v2.5-20250123) | COMBO | No | Múltiples opciones disponibles |
| `estilo` | Configuración de estilo para el modelo generado (predeterminado: "Ninguno") | COMBO | No | Múltiples opciones disponibles |
| `textura` | Si se deben generar texturas para el modelo (predeterminado: Verdadero) | BOOLEAN | No | - |
| `pbr` | Si se deben generar materiales PBR (renderizado basado en física) (predeterminado: Verdadero) | BOOLEAN | No | - |
| `semilla_de_imagen` | Semilla aleatoria para la generación de imágenes (predeterminado: 42) | INT | No | - |
| `semilla_del_modelo` | Semilla aleatoria para la generación del modelo (predeterminado: 42) | INT | No | - |
| `semilla_de_textura` | Semilla aleatoria para la generación de texturas (predeterminado: 42) | INT | No | - |
| `calidad_de_textura` | Nivel de calidad para la generación de texturas (predeterminado: "standard") | COMBO | No | "standard"<br>"detailed" |
| `límite_de_caras` | Número máximo de caras en el modelo generado, -1 para sin límite (predeterminado: -1) | INT | No | -1 a 2000000 |
| `cuadrante` | Si se debe generar geometría basada en cuadrángulos en lugar de triángulos (predeterminado: Falso) | BOOLEAN | No | - |
| `geometry_quality` | Nivel de calidad para la generación de geometría (predeterminado: "standard") | COMBO | No | "standard"<br>"detailed" |

**Nota:** El parámetro `prompt` es obligatorio y no puede estar vacío. Si no se proporciona un prompt, el nodo generará un error.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `id_de_tarea_de_modelo` | El archivo del modelo 3D generado (solo para compatibilidad hacia atrás) | STRING |
| `GLB` | El identificador único de la tarea para el proceso de generación del modelo | MODEL_TASK_ID |
| `GLB` | El modelo 3D generado en formato GLB | FILE3DGLB |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextToModelNode/es.md)

---
**Source fingerprint (SHA-256):** `f73316e0a50adfb6fe22ca6a20a2a5b36a6597abf0f4ddae9183d9e4a45cb46d`
