# Vista previa de Splat

El nodo PreviewGaussianSplat permite previsualizar un archivo 3D de gaussian splat directamente en la interfaz de ComfyUI sin guardarlo en el directorio de salida. Almacena temporalmente el archivo en una carpeta temporal, lo muestra en una ventana de previsualización 3D y pasa los datos del modelo, la información de la cámara y el tamaño de la previsualización a otros nodos.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `model_3d` | Un archivo 3D de gaussian splat. | FILE3D | Sí | splat, ply, spz, ksplat |
| `model_3d_info` | Información de metadatos opcional sobre el modelo 3D. | LOAD3DMODELINFO | No | - |
| `viewport_state` | El estado actual de la ventana 3D, incluida la información de la cámara y del modelo. | LOAD3D | Sí | - |
| `camera_info` | Información opcional de la cámara para la previsualización. | LOAD3DCAMERA | No | - |
| `width` | El ancho del render de previsualización en píxeles (predeterminado: 1024). | INT | Sí | 1 a 4096 |
| `height` | La altura del render de previsualización en píxeles (predeterminado: 1024). | INT | Sí | 1 a 4096 |

Nota: Cuando no se proporcionan `camera_info` o `model_3d_info`, el nodo usa los valores correspondientes de `viewport_state` en su lugar.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `model_3d` | El archivo 3D de gaussian splat de entrada, transferido sin cambios. | FILE3D |
| `model_3d_info` | Información de metadatos sobre el modelo 3D, ya sea de la entrada o del estado de la ventana. | LOAD3DMODELINFO |
| `camera_info` | Información de la cámara para la previsualización, ya sea de la entrada o del estado de la ventana. | LOAD3DCAMERA |
| `width` | El ancho del render de previsualización. | INT |
| `height` | La altura del render de previsualización. | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewGaussianSplat/es.md)

---
**Source fingerprint (SHA-256):** `7157a0b34d7bda3e7ec86cb2ac09e0e10ff96ea7037bb6c9d6ad2c879fdedbb2`
