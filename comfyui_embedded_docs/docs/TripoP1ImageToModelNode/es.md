# Tripo P1: Imagen a Modelo

## Descripción general

Este nodo convierte una sola imagen 2D en un modelo 3D utilizando la API de Tripo P1. Está optimizado para generar mallas de baja poligonización listas para su uso en videojuegos.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `imagen` | La imagen de entrada que se convertirá en un modelo 3D. | IMAGE | Sí | - |
| `modo_de_salida` | Un diccionario que especifica el modo de salida y la configuración de calidad. Este parámetro controla el tipo de modelo generado y su calidad de textura. Las opciones disponibles están definidas por la función auxiliar `_build_p1_output_mode` e incluyen configuraciones para `texture_quality` (ej. "standard", "high", "ultra") y `image_alignment`. | DICT | Sí | Ver descripción |
| `activar_autocorrección_imagen` | Preprocesa la imagen de entrada para mejorar la calidad de generación. (predeterminado: False) | BOOLEAN | No | True<br>False |
| `límite_de_caras` | Limita el número de caras en la malla generada. Un valor de -1 significa sin límite. (predeterminado: -1) | INT | No | - |
| `semilla_modelo` | Un valor semilla para la generación reproducible del modelo. Si no se proporciona, se utiliza una semilla aleatoria. (predeterminado: None) | INT | No | - |
| `auto_escala` | Determina automáticamente el tamaño óptimo para el modelo generado. (predeterminado: False) | BOOLEAN | No | True<br>False |
| `exportar_uv` | Exporta las coordenadas UV junto con el modelo. (predeterminado: True) | BOOLEAN | No | True<br>False |
| `comprimir_geometría` | Comprime los datos de geometría para reducir el tamaño del archivo. (predeterminado: False) | BOOLEAN | No | True<br>False |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `archivo_modelo` | La ruta del archivo del modelo 3D generado. Esta salida se proporciona únicamente para compatibilidad con versiones anteriores. | STRING |
| `id_tarea_modelo` | El ID de tarea único para la solicitud de generación del modelo. | MODEL_TASK_ID |
| `GLB` | El modelo 3D generado en formato GLB. | FILE3DGLB |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1ImageToModelNode/es.md)

---
**Source fingerprint (SHA-256):** `2ac611603dd6eb88700a8105c19f97a8c4eefe5f4efb23d8854ccc27af590626`
