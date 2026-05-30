> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1ImageToModelNode/es.md)

## Descripción general

Este nodo convierte una sola imagen 2D en un modelo 3D utilizando la API de Tripo P1. Está optimizado para generar mallas de baja poligonización listas para su uso en videojuegos.

## Entradas

| Parámetro | Tipo de dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen de entrada que se convertirá en un modelo 3D. |
| `output_mode` | DICT | Sí | Ver descripción | Un diccionario que especifica el modo de salida y la configuración de calidad. Este parámetro controla el tipo de modelo generado y su calidad de textura. Las opciones disponibles están definidas por la función auxiliar `_build_p1_output_mode` e incluyen configuraciones para `texture_quality` (ej. "standard", "high", "ultra") y `image_alignment`. |
| `enable_image_autofix` | BOOLEAN | No | True<br>False | Preprocesa la imagen de entrada para mejorar la calidad de generación. (predeterminado: False) |
| `face_limit` | INT | No | - | Limita el número de caras en la malla generada. Un valor de -1 significa sin límite. (predeterminado: -1) |
| `model_seed` | INT | No | - | Un valor semilla para la generación reproducible del modelo. Si no se proporciona, se utiliza una semilla aleatoria. (predeterminado: None) |
| `auto_size` | BOOLEAN | No | True<br>False | Determina automáticamente el tamaño óptimo para el modelo generado. (predeterminado: False) |
| `export_uv` | BOOLEAN | No | True<br>False | Exporta las coordenadas UV junto con el modelo. (predeterminado: True) |
| `compress_geometry` | BOOLEAN | No | True<br>False | Comprime los datos de geometría para reducir el tamaño del archivo. (predeterminado: False) |

## Salidas

| Nombre de salida | Tipo de dato | Descripción |
|------------------|--------------|-------------|
| `model_file` | STRING | La ruta del archivo del modelo 3D generado. Esta salida se proporciona únicamente para compatibilidad con versiones anteriores. |
| `model task_id` | MODEL_TASK_ID | El ID de tarea único para la solicitud de generación del modelo. |
| `GLB` | FILE3DGLB | El modelo 3D generado en formato GLB. |

---
**Source fingerprint (SHA-256):** `2ac611603dd6eb88700a8105c19f97a8c4eefe5f4efb23d8854ccc27af590626`
