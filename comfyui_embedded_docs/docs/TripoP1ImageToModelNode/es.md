## Descripción general

Este nodo convierte una sola imagen 2D en un modelo 3D utilizando la API de Tripo P1. Está optimizado para generar mallas de baja poligonización listas para su uso en videojuegos.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `image` | La imagen de entrada que se convertirá en un modelo 3D. | IMAGE | Sí | - |
| `output_mode` | Un diccionario que especifica el modo de salida y la configuración de calidad. Este parámetro controla el tipo de modelo generado y su calidad de textura. Las opciones disponibles están definidas por la función auxiliar `_build_p1_output_mode` e incluyen configuraciones para `texture_quality` (ej. "standard", "high", "ultra") y `image_alignment`. | DICT | Sí | Ver descripción |
| `enable_image_autofix` | Preprocesa la imagen de entrada para mejorar la calidad de generación. (predeterminado: False) | BOOLEAN | No | True<br>False |
| `face_limit` | Limita el número de caras en la malla generada. Un valor de -1 significa sin límite. (predeterminado: -1) | INT | No | - |
| `model_seed` | Un valor semilla para la generación reproducible del modelo. Si no se proporciona, se utiliza una semilla aleatoria. (predeterminado: None) | INT | No | - |
| `auto_size` | Determina automáticamente el tamaño óptimo para el modelo generado. (predeterminado: False) | BOOLEAN | No | True<br>False |
| `export_uv` | Exporta las coordenadas UV junto con el modelo. (predeterminado: True) | BOOLEAN | No | True<br>False |
| `compress_geometry` | Comprime los datos de geometría para reducir el tamaño del archivo. (predeterminado: False) | BOOLEAN | No | True<br>False |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `model_file` | La ruta del archivo del modelo 3D generado. Esta salida se proporciona únicamente para compatibilidad con versiones anteriores. | STRING |
| `model task_id` | El ID de tarea único para la solicitud de generación del modelo. | MODEL_TASK_ID |
| `GLB` | El modelo 3D generado en formato GLB. | FILE3DGLB |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1ImageToModelNode/es.md)

---
**Source fingerprint (SHA-256):** `2ac611603dd6eb88700a8105c19f97a8c4eefe5f4efb23d8854ccc27af590626`
