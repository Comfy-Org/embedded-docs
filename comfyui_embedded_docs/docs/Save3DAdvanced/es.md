# Save3DAdvanced

Este nodo guarda un modelo 3D en un archivo dentro del directorio de salida de ComfyUI, con control avanzado sobre las dimensiones de salida y la configuración de cámara/visor. También transmite el modelo 3D, la información del modelo, la información de la cámara y las dimensiones para nodos posteriores.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `model_3d` | Archivo de modelo 3D proveniente de un nodo 3D anterior. | FILE3D | Sí | GLB, GLTF, FBX, OBJ, STL, USDZ, Cualquiera |
| `filename_prefix` | Prefijo para el nombre del archivo guardado (predeterminado: "3d/ComfyUI"). | STRING | Sí | Texto libre |
| `viewport_state` | Estado del visor proveniente de un nodo Cargar 3D, que contiene información de la cámara y del modelo. | LOAD3D | Sí | - |
| `model_3d_info` | Información opcional del modelo 3D para sobrescribir el estado del visor. | LOAD3DMODELINFO | No | - |
| `camera_info` | Información opcional de la cámara para sobrescribir el estado del visor. | LOAD3DCAMERA | No | - |
| `width` | Ancho de la vista previa de salida en píxeles (predeterminado: 1024). | INT | Sí | 1 a 4096 |
| `height` | Alto de la vista previa de salida en píxeles (predeterminado: 1024). | INT | Sí | 1 a 4096 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `model_3d` | El archivo de modelo 3D transmitido desde la entrada. | FILE3D |
| `model_3d_info` | Información del modelo, ya sea desde el estado del visor o desde la entrada opcional. | LOAD3DMODELINFO |
| `camera_info` | Información de la cámara, ya sea desde el estado del visor o desde la entrada opcional. | LOAD3DCAMERA |
| `width` | El valor de ancho transmitido desde la entrada. | INT |
| `height` | El valor de alto transmitido desde la entrada. | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Save3DAdvanced/es.md)

---
**Source fingerprint (SHA-256):** `2c7d42b1875bb292e675526a2b38fcc8856c8ac45de25ac7b69d92323f0b7ae0`
