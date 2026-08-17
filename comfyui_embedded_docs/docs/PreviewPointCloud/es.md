# Vista previa de nube de puntos

El nodo Preview Point Cloud le permite ver un archivo de nube de puntos 3D (como un archivo .ply) directamente en la interfaz de ComfyUI sin guardarlo en el directorio de salida. El nodo escribe la nube de puntos en un archivo temporal, la muestra en una ventana de vista previa 3D y transmite los datos del modelo, la información del modelo, la información de la cámara, el ancho y la altura para su posterior procesamiento.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `model_3d` | Archivo de nube de puntos (.ply) | FILE3D | Sí | - |
| `model_3d_info` | Información sobre el modelo 3D. Entrada avanzada. Cuando no está conectada, se utiliza el valor almacenado en `viewport_state`. | LOAD3DMODELINFO | No | - |
| `viewport_state` | El estado actual del viewport, que puede contener información de la cámara e información del modelo utilizadas para la vista previa. | LOAD3D | Sí | - |
| `camera_info` | Información de la cámara para la vista 3D. Entrada avanzada. Cuando no está conectada, se utiliza el valor almacenado en `viewport_state`. | LOAD3DCAMERA | No | - |
| `width` | Ancho de la ventana de vista previa en píxeles (predeterminado: 1024). | INT | Sí | 1 a 4096 |
| `height` | Altura de la ventana de vista previa en píxeles (predeterminado: 1024). | INT | Sí | 1 a 4096 |

Nota: Cuando `camera_info` o `model_3d_info` no están conectados, el nodo utiliza los valores almacenados en `viewport_state`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `model_3d` | Los datos del modelo de nube de puntos, transmitidos sin cambios. | FILE3D |
| `model_3d_info` | Información sobre el modelo 3D utilizado para la vista previa. | LOAD3DMODELINFO |
| `camera_info` | Información de la cámara utilizada para la vista 3D. | LOAD3DCAMERA |
| `width` | Ancho de la ventana de vista previa. | INT |
| `height` | Altura de la ventana de vista previa. | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewPointCloud/es.md)

---
**Source fingerprint (SHA-256):** `a192096df29c4d7029f6e7f4f32e0a2f48de5b3d0cd437bd5b03d79e15eb0987`
