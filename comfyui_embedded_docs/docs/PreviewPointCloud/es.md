# Vista Previa de Nube de Puntos

El nodo Vista Previa de Nube de Puntos le permite visualizar un archivo de nube de puntos 3D dentro de la interfaz de ComfyUI. Guarda la nube de puntos en un archivo temporal y la muestra en una ventana de vista previa 3D, transmitiendo los datos del modelo y la configuración del viewport para su procesamiento posterior.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `modelo_3d` | Archivo de nube de puntos (.ply) | FILE3D | Sí | - |
| `info_modelo_3d` | Información sobre el modelo 3D | LOAD3DMODELINFO | No | - |
| `estado_de_vista` | Estado actual del viewport | LOAD3D | Sí | - |
| `info_cámara` | Información de la cámara para la vista 3D | LOAD3DCAMERA | No | - |
| `ancho` | Ancho de la ventana de vista previa (predeterminado: 1024) | INT | Sí | 1 a 4096 |
| `alto` | Alto de la ventana de vista previa (predeterminado: 1024) | INT | Sí | 1 a 4096 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `info_modelo_3d` | Datos del modelo de nube de puntos | FILE3D |
| `info_cámara` | Información sobre el modelo 3D | LOAD3DMODELINFO |
| `ancho` | Información de la cámara para la vista 3D | LOAD3DCAMERA |
| `alto` | Ancho de la ventana de vista previa | INT |
| `alto` | Alto de la ventana de vista previa | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewPointCloud/es.md)

---
**Source fingerprint (SHA-256):** `f3121511841d1962aad881c0ac5b93f24842bf4810e84fe241330e9eab90334a`
