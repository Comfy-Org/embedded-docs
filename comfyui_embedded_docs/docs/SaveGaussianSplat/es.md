# SaveGaussianSplat

Este nodo guarda un archivo 3D de splat gaussiano en el directorio de salida de ComfyUI y proporciona datos de vista previa para el visor 3D.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | Un archivo 3D de splat gaussiano. | FILE3D | Sí | - |
| `filename_prefix` | Prefijo para el nombre del archivo guardado (predeterminado: "3d/ComfyUI") | STRING | Sí | - |
| `viewport_state` | El estado actual del viewport desde un nodo cargador 3D. | LOAD3D | Sí | - |
| `model_3d_info` | Información adicional del modelo 3D para la vista previa. | LOAD3DMODELINFO | No | - |
| `camera_info` | Información de la cámara para la vista previa. | LOAD3DCAMERA | No | - |
| `width` | Ancho de la vista previa en píxeles (predeterminado: 1024) | INT | Sí | min: 1, max: 4096, step: 1 |
| `height` | Alto de la vista previa en píxeles (predeterminado: 1024) | INT | Sí | min: 1, max: 4096, step: 1 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|-------------|-------------|-----------|
| `model_3d` | El archivo 3D de splat gaussiano guardado. | FILE3D |
| `model_3d_info` | Información del modelo 3D para la vista previa. | LOAD3DMODELINFO |
| `camera_info` | Información de la cámara para la vista previa. | LOAD3DCAMERA |
| `width` | Ancho de la vista previa. | INT |
| `height` | Alto de la vista previa. | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveGaussianSplat/es.md)

---
**Source fingerprint (SHA-256):** `f2d6b98d2ce1fe11df8ba440b7f46a21e2308966c15daa5ca0bdca7dab1726cc`
