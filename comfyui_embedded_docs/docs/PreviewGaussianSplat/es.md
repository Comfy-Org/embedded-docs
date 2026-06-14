# PreviewGaussianSplat

El nodo PreviewGaussianSplat permite previsualizar un archivo de splat gaussiano 3D dentro de la interfaz de ComfyUI. Acepta un archivo de modelo 3D en varios formatos de splat gaussiano y lo renderiza en una ventana de previsualización 3D, transmitiendo los datos del modelo para su procesamiento posterior.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `modelo_3d` | Un archivo 3D de splat gaussiano. | FILE3D | Sí | Formatos compatibles: splat, ply, spz, ksplat |
| `info_modelo_3d` | Información de metadatos opcional sobre el modelo 3D. | LOAD3DMODELINFO | No | - |
| `estado_de_vista` | El estado actual del viewport 3D, incluyendo información de cámara y modelo. | LOAD3D | Sí | - |
| `info_cámara` | Información opcional de cámara para la previsualización. | LOAD3DCAMERA | No | - |
| `ancho` | El ancho del renderizado de previsualización en píxeles (predeterminado: 1024). | INT | Sí | 1 a 4096 |
| `alto` | La altura del renderizado de previsualización en píxeles (predeterminado: 1024). | INT | Sí | 1 a 4096 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `info_modelo_3d` | El archivo 3D de splat gaussiano de entrada, transmitido sin cambios. | FILE3D |
| `info_cámara` | Información de metadatos sobre el modelo 3D, ya sea de la entrada o derivada del estado del viewport. | LOAD3DMODELINFO |
| `ancho` | Información de cámara para la previsualización, ya sea de la entrada o derivada del estado del viewport. | LOAD3DCAMERA |
| `alto` | El ancho del renderizado de previsualización. | INT |
| `alto` | La altura del renderizado de previsualización. | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewGaussianSplat/es.md)

---
**Source fingerprint (SHA-256):** `7b79e9ab25858e7db6e999313cc11226895aeb4d7fee414f56f0d5fd2363b485`
