# Tripo: Modelo de textura

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | El ID de tarea del modelo al que se le aplicarán las texturas | MODEL_TASK_ID | Sí | - |
| `texture` | Determina si se generan texturas (predeterminado: True) | BOOLEAN | No | - |
| `pbr` | Determina si se generan materiales PBR (renderizado basado en la física) (predeterminado: True) | BOOLEAN | No | - |
| `texture_seed` | Semilla aleatoria para la generación de texturas (predeterminado: 42) | INT | No | - |
| `texture_quality` | Nivel de calidad para la generación de texturas (predeterminado: "standard"). La opción "detailed" cuesta 0,20 USD, mientras que "standard" cuesta 0,10 USD | COMBO | No | "standard"<br>"detailed" |
| `texture_alignment` | Método de alineación de texturas (predeterminado: "original_image"). "original_image" alinea las texturas con la imagen de entrada original, mientras que "geometry" las alinea con la geometría 3D | COMBO | No | "original_image"<br>"geometry" |
| `texture_prompt` | Texto de guía opcional para el texturizado. En la práctica, es necesario para los modelos importados (Tripo: Import Model), que no incluyen una imagen de origen de la que inferir los colores. (cuadro de texto multilínea, predeterminado: cadena vacía) | STRING | No | - |

*Nota: Este nodo requiere tokens de autenticación y claves de API que el sistema maneja automáticamente.*

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `model_file` | El archivo de modelo generado con las texturas aplicadas (solo por retrocompatibilidad) | STRING |
| `model task_id` | El ID de tarea para el seguimiento del proceso de generación de texturas | MODEL_TASK_ID |
| `GLB` | El modelo 3D generado en formato GLB con las texturas aplicadas | FILE3DGLB |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNode/es.md)

---
**Source fingerprint (SHA-256):** `a0157b7fa2bb94d174ea5893d7389885180876794032a510642586e310ba30d4`
