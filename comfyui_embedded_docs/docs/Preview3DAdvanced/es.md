# Vista previa 3D (Avanzado)

Este nodo proporciona una vista previa avanzada de modelos 3D con salida de información de cámara y modelo. Guarda el modelo 3D en un archivo temporal y lo muestra en la interfaz de usuario, mientras también transmite los datos del modelo, la información de la cámara y las dimensiones del viewport para su procesamiento posterior.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `model_3d` | Archivo de modelo 3D proveniente de un nodo 3D anterior. | FILE3D | Sí | GLB, GLTF, FBX, OBJ, STL, USDZ o cualquier formato 3D compatible |
| `info_modelo_3d` | Metadatos opcionales de información del modelo. | LOAD3DMODELINFO | No | - |
| `viewport_state` | Estado actual del viewport que contiene información de cámara y modelo. | LOAD3D | Sí | - |
| `info_cámara` | Configuración opcional de cámara para la vista 3D. | LOAD3DCAMERA | No | - |
| `ancho` | Ancho de la vista previa en píxeles. | INT | Sí | 1 a 4096 (predeterminado: 1024) |
| `alto` | Alto de la vista previa en píxeles. | INT | Sí | 1 a 4096 (predeterminado: 1024) |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `archivo_modelo` | Archivo de modelo 3D transmitido desde la entrada. | FILE3D |
| `info_cámara` | Metadatos de información del modelo, ya sea desde la entrada o desde el estado del viewport. | LOAD3DMODELINFO |
| `info_modelo_3d` | Configuración de cámara, ya sea desde la entrada o desde el estado del viewport. | LOAD3DCAMERA |
| `ancho` | Ancho de la vista previa en píxeles. | INT |
| `alto` | Alto de la vista previa en píxeles. | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3DAdvanced/es.md)

---
**Source fingerprint (SHA-256):** `7efe8720f88f7d6234387cd633ea629cbf43a0abea1a9aca6c5dcd43bf7f2145`
