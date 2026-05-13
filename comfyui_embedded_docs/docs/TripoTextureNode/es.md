> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNode/es.md)

El nodo TripoTextureNode genera modelos 3D texturizados utilizando la API de Tripo. Toma un ID de tarea de modelo y aplica generación de texturas con varias opciones que incluyen materiales PBR, configuraciones de calidad de textura y métodos de alineación. El nodo se comunica con la API de Tripo para procesar la solicitud de generación de texturas y devuelve el archivo de modelo resultante y el ID de tarea.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `id_de_tarea_del_modelo` | MODEL_TASK_ID | Sí | - | El ID de tarea del modelo al que se le aplicarán texturas |
| `textura` | BOOLEAN | No | - | Si se deben generar texturas (predeterminado: True) |
| `pbr` | BOOLEAN | No | - | Si se deben generar materiales PBR (renderizado basado en física) (predeterminado: True) |
| `semilla_de_textura` | INT | No | - | Semilla aleatoria para la generación de texturas (predeterminado: 42) |
| `calidad_de_textura` | COMBO | No | "standard"<br>"detailed" | Nivel de calidad para la generación de texturas (predeterminado: "standard"). La opción "detailed" tiene un costo de $0.20 USD, mientras que "standard" cuesta $0.10 USD. |
| `alineación_de_textura` | COMBO | No | "original_image"<br>"geometry" | Método para alinear texturas (predeterminado: "original_image"). "original_image" alinea las texturas con la imagen de entrada original, mientras que "geometry" las alinea con la geometría 3D. |

*Nota: Este nodo requiere tokens de autenticación y claves API que son manejadas automáticamente por el sistema.*

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `id_de_tarea_de_modelo` | STRING | El archivo de modelo generado con texturas aplicadas (solo para compatibilidad hacia atrás) |
| `GLB` | MODEL_TASK_ID | El ID de tarea para rastrear el proceso de generación de texturas |
| `GLB` | FILE3DGLB | El modelo 3D generado en formato GLB con texturas aplicadas |

---
**Source fingerprint (SHA-256):** `6d2a6ff7bbbe9fa91f63c6c7d237799044d2f9aa5afe7b90b99cf9e5a21afc32`
