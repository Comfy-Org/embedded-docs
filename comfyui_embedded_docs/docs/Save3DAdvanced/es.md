# Save3DAdvanced

Este nodo guarda un modelo 3D en el directorio de salida de ComfyUI y proporciona capacidades avanzadas de vista previa. Permite especificar el nombre del archivo de salida, las dimensiones de la vista previa y, opcionalmente, pasar información de cámara y modelo para una experiencia mejorada en el visor 3D.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `model_3d` | Archivo de modelo 3D proveniente de un nodo 3D anterior. | FILE3D | Sí | GLB, GLTF, FBX, OBJ, STL, USDZ o cualquier formato 3D |
| `filename_prefix` | Prefijo para el nombre del archivo guardado. Se agregarán automáticamente un contador y la extensión del archivo. (predeterminado: "3d/ComfyUI") | STRING | Sí | Cualquier cadena de nombre de archivo válida |
| `viewport_state` | El estado actual de la ventana gráfica, generalmente desde un nodo visor 3D. | LOAD3D | Sí | - |
| `model_3d_info` | Información opcional del modelo 3D para la vista previa. | LOAD3DMODELINFO | No | - |
| `camera_info` | Información opcional de la cámara para la vista previa. | LOAD3DCAMERA | No | - |
| `width` | Ancho de la vista previa en píxeles. (predeterminado: 1024) | INT | Sí | 1 a 4096 |
| `height` | Alto de la vista previa en píxeles. (predeterminado: 1024) | INT | Sí | 1 a 4096 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `model_3d` | El archivo de modelo 3D guardado. | FILE3D |
| `model_3d_info` | Información del modelo 3D transferida para nodos posteriores. | LOAD3DMODELINFO |
| `camera_info` | Información de la cámara transferida para nodos posteriores. | LOAD3DCAMERA |
| `width` | El valor de ancho transferido para nodos posteriores. | INT |
| `height` | El valor de alto transferido para nodos posteriores. | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Save3DAdvanced/es.md)

---
**Source fingerprint (SHA-256):** `2c7d42b1875bb292e675526a2b38fcc8856c8ac45de25ac7b69d92323f0b7ae0`
