# SavePointCloud

El nodo **Save Point Cloud** guarda un archivo de nube de puntos 3D en el directorio de salida de ComfyUI. También transmite los datos de la nube de puntos, así como información opcional de cámara y modelo, para que sean utilizados por otros nodos en su flujo de trabajo.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `model_3d` | Archivo de nube de puntos (.ply) | FILE3D | Sí | - |
| `filename_prefix` | Prefijo para el nombre del archivo guardado (predeterminado: "3d/ComfyUI") | STRING | Sí | - |
| `viewport_state` | Estado de un nodo de ventana gráfica 3D | LOAD3D | Sí | - |
| `model_3d_info` | Información opcional del modelo 3D para uso avanzado | LOAD3DMODELINFO | No | - |
| `camera_info` | Información opcional de la cámara para uso avanzado | LOAD3DCAMERA | No | - |
| `width` | Ancho de la imagen de vista previa en píxeles (predeterminado: 1024) | INT | Sí | min: 1, max: 4096, step: 1 |
| `height` | Alto de la imagen de vista previa en píxeles (predeterminado: 1024) | INT | Sí | min: 1, max: 4096, step: 1 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `model_3d` | El archivo de nube de puntos guardado | FILE3D |
| `model_3d_info` | Información sobre el modelo 3D | LOAD3DMODELINFO |
| `camera_info` | Información de la cámara para la ventana gráfica | LOAD3DCAMERA |
| `width` | Ancho de la imagen de vista previa | INT |
| `height` | Alto de la imagen de vista previa | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SavePointCloud/es.md)

---
**Source fingerprint (SHA-256):** `ce8f005c431843a57d87a4aff2eed7a1604ebdf360f83b3aaaadc3ed364d218a`
