# Vista previa 3D (Avanzado)

Este nodo proporciona una vista previa avanzada de modelos 3D con salida de información de cámara y modelo. Muestra una vista previa de un archivo de modelo 3D sin guardarlo en el directorio de salida de ComfyUI, escribiendo el modelo en un archivo temporal para mostrarlo en la interfaz de usuario. Los datos del modelo, la información del modelo, la información de la cámara y las dimensiones del viewport también se transfieren para su posterior procesamiento en los nodos siguientes.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `model_3d` | Archivo de modelo 3D procedente de un nodo 3D anterior. | FILE3D | Sí | GLB, GLTF, FBX, OBJ, STL, USDZ o cualquier formato 3D compatible |
| `model_3d_info` | Metadatos opcionales de información del modelo. | LOAD3DMODELINFO | No | - |
| `viewport_state` | El estado actual del viewport que contiene la información de cámara y modelo. | LOAD3D | Sí | - |
| `camera_info` | Configuración opcional de cámara para la vista 3D. | LOAD3DCAMERA | No | - |
| `width` | El ancho de la vista previa en píxeles. | INT | Sí | de 1 a 4096 (por defecto: 1024) |
| `height` | La altura de la vista previa en píxeles. | INT | Sí | de 1 a 4096 (por defecto: 1024) |

Nota: Cuando `camera_info` no está conectado, el nodo utiliza el valor `camera_info` de `viewport_state`. Cuando `model_3d_info` no está conectado, el nodo utiliza el valor `model_3d_info` de `viewport_state`, o una lista vacía si el estado del viewport no lo contiene.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `model_3d` | El archivo de modelo 3D transferido desde la entrada. | FILE3D |
| `model_3d_info` | Metadatos de información del modelo, provenientes de la entrada o del estado del viewport. | LOAD3DMODELINFO |
| `camera_info` | Configuración de cámara, proveniente de la entrada o del estado del viewport. | LOAD3DCAMERA |
| `width` | El ancho de la vista previa en píxeles. | INT |
| `height` | La altura de la vista previa en píxeles. | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Preview3DAdvanced/es.md)

---
**Source fingerprint (SHA-256):** `eda8c8fdd6ce7c39caf00c3054fc58e6dcab124fc3774d17af2deae651fbbf2e`
