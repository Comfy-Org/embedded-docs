# Tripo: Modelo de textura

El nodo TripoTextureNode genera modelos 3D texturizados utilizando la API de Tripo. Toma un ID de tarea de modelo y aplica generación de texturas con varias opciones que incluyen materiales PBR, configuraciones de calidad de textura y métodos de alineación. El nodo se comunica con la API de Tripo para procesar la solicitud de generación de texturas y devuelve el archivo de modelo resultante y el ID de tarea.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `id_de_tarea_del_modelo` | El ID de tarea del modelo al que se le aplicarán texturas | MODEL_TASK_ID | Sí | - |
| `textura` | Si se deben generar texturas (predeterminado: True) | BOOLEAN | No | - |
| `pbr` | Si se deben generar materiales PBR (renderizado basado en física) (predeterminado: True) | BOOLEAN | No | - |
| `semilla_de_textura` | Semilla aleatoria para la generación de texturas (predeterminado: 42) | INT | No | - |
| `calidad_de_textura` | Nivel de calidad para la generación de texturas (predeterminado: "standard"). La opción "detailed" tiene un costo de $0.20 USD, mientras que "standard" cuesta $0.10 USD. | COMBO | No | "standard"<br>"detailed" |
| `alineación_de_textura` | Método para alinear texturas (predeterminado: "original_image"). "original_image" alinea las texturas con la imagen de entrada original, mientras que "geometry" las alinea con la geometría 3D. | COMBO | No | "original_image"<br>"geometry" |

*Nota: Este nodo requiere tokens de autenticación y claves API que son manejadas automáticamente por el sistema.*

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `id_de_tarea_de_modelo` | El archivo de modelo generado con texturas aplicadas (solo para compatibilidad hacia atrás) | STRING |
| `GLB` | El ID de tarea para rastrear el proceso de generación de texturas | MODEL_TASK_ID |
| `GLB` | El modelo 3D generado en formato GLB con texturas aplicadas | FILE3DGLB |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNode/es.md)

---
**Source fingerprint (SHA-256):** `6d2a6ff7bbbe9fa91f63c6c7d237799044d2f9aa5afe7b90b99cf9e5a21afc32`
