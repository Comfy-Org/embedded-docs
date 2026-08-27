# Vista previa de nube de puntos

El nodo de vista previa de nube de puntos permite ver un archivo de nube de puntos 3D directamente en la interfaz de ComfyUI sin guardarlo en el directorio de salida de ComfyUI. Guarda la nube de puntos en una ubicación temporal y la muestra en una ventana de vista previa 3D, mientras también pasa los datos del modelo, la información de la cámara y el estado de la ventana gráfica para su posterior procesamiento.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|---------------|-------------|-------|
| `modelo_3d` | Archivo de nube de puntos (.ply) | FILE3D | Sí | - |
| `info_modelo_3d` | Información sobre el modelo 3D | LOAD3DMODELINFO | No | - |
| `estado_de_vista` | El estado actual de la ventana gráfica | LOAD3D | Sí | - |
| `info_cámara` | Información de la cámara para la vista 3D | LOAD3DCAMERA | No | - |
| `ancho` | Ancho de la ventana de vista previa (predeterminado: 1024) | INT | Sí | 1 a 4096 |
| `alto` | Alto de la ventana de vista previa (predeterminado: 1024) | INT | Sí | 1 a 4096 |

Nota: Cuando `camera_info` o `model_3d_info` no están conectados, el nodo recurre a los valores correspondientes almacenados en `viewport_state`. El archivo de nube de puntos se guarda en el directorio temporal de ComfyUI y no se escribe en el directorio de salida. Este es un nodo de salida, por lo que se utiliza principalmente para mostrar el resultado de la vista previa en la interfaz.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `modelo_3d` | Los datos del modelo de nube de puntos | FILE3D |
| `info_modelo_3d` | Información sobre el modelo 3D | LOAD3DMODELINFO |
| `info_cámara` | Información de la cámara para la vista 3D | LOAD3DCAMERA |
| `ancho` | Ancho de la ventana de vista previa | INT |
| `alto` | Alto de la ventana de vista previa | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewPointCloud/es.md)

---
**Source fingerprint (SHA-256):** `a192096df29c4d7029f6e7f4f32e0a2f48de5b3d0cd437bd5b03d79e15eb0987`
