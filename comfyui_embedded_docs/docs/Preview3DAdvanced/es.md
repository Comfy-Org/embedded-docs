# Vista previa 3D (Avanzado)

Este nodo muestra una vista previa del modelo 3D en la interfaz de usuario sin guardar el archivo en el directorio de salida de ComfyUI. Guarda el modelo en un archivo temporal y transmite los datos del modelo, la información del modelo, la información de la cámara y las dimensiones de la vista previa para su posterior procesamiento en etapas posteriores.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `model_3d` | Archivo de modelo 3D proveniente de un nodo 3D anterior. | FILE3D | Sí | GLB, GLTF, FBX, OBJ, STL, USDZ o cualquier formato 3D admitido |
| `info_modelo_3d` | Metadatos opcionales de información del modelo. Opción avanzada. | LOAD3DMODELINFO | No | - |
| `viewport_state` | El estado actual de la vista que contiene información de la cámara y del modelo. | LOAD3D | Sí | - |
| `info_cámara` | Configuración opcional de la cámara para la vista 3D. Opción avanzada. | LOAD3DCAMERA | No | - |
| `ancho` | El ancho de la vista previa en píxeles. Valor predeterminado: 1024. | INT | Sí | 1 a 4096 |
| `alto` | El alto de la vista previa en píxeles. Valor predeterminado: 1024. | INT | Sí | 1 a 4096 |

Nota: cuando `camera_info` o `model_3d_info` no están conectados, sus valores se toman de `viewport_state` cuando esté disponible. Si `viewport_state` no tiene información del modelo, `model_3d_info` se establece por defecto en una lista vacía. Si `viewport_state` no es un diccionario, se considera vacío.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `archivo_modelo` | El archivo de modelo 3D transmitido desde la entrada. | FILE3D |
| `info_cámara` | Metadatos de información del modelo, ya sea desde la entrada o desde el estado de la vista. | LOAD3DMODELINFO |
| `info_modelo_3d` | Configuración de la cámara, ya sea desde la entrada o desde el estado de la vista. | LOAD3DCAMERA |
| `ancho` | El ancho de la vista previa en píxeles. | INT |
| `alto` | El alto de la vista previa en píxeles. | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3DAdvanced/es.md)

---
**Source fingerprint (SHA-256):** `eda8c8fdd6ce7c39caf00c3054fc58e6dcab124fc3774d17af2deae651fbbf2e`
