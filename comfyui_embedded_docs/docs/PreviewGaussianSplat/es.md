# Vista previa de Splat

El nodo PreviewGaussianSplat muestra un archivo de gaussian splat 3D en una ventana de vista previa sin guardarlo en el directorio de salida de ComfyUI. Acepta un archivo de modelo 3D en varios formatos de gaussian splat, guarda una copia temporal para la vista previa y pasa los datos del modelo para su procesamiento posterior en el flujo de trabajo. Este nodo está marcado como experimental y actúa como un nodo de salida.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | Un archivo de gaussian splat 3D. | FILE3D | Sí | splat<br>ply<br>spz<br>ksplat |
| `model_3d_info` | Información de metadatos opcional sobre el modelo 3D. Cuando no está conectado, el nodo usa la información del modelo de `viewport_state`. | LOAD3DMODELINFO | No | - |
| `viewport_state` | El estado actual del viewport 3D, incluida la información de la cámara y del modelo. | LOAD3D | Sí | - |
| `camera_info` | Información de cámara opcional para la vista previa. Cuando no está conectado, el nodo usa la información de cámara de `viewport_state`. | LOAD3DCAMERA | No | - |
| `width` | El ancho del renderizado de la vista previa en píxeles (predeterminado: 1024). | INT | Sí | 1 a 4096 |
| `height` | La altura del renderizado de la vista previa en píxeles (predeterminado: 1024). | INT | Sí | 1 a 4096 |

Nota: Cuando no se proporcionan `camera_info` o `model_3d_info`, el nodo recurre a la información de cámara y modelo almacenada en `viewport_state`. Si `viewport_state` no es un objeto de estado de viewport válido, se trata como vacío.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `model_3d` | El archivo de gaussian splat 3D de entrada, pasado sin cambios. | FILE3D |
| `model_3d_info` | Información de metadatos sobre el modelo 3D, ya sea desde la entrada o derivada del estado del viewport. | LOAD3DMODELINFO |
| `camera_info` | Información de cámara para la vista previa, ya sea desde la entrada o derivada del estado del viewport. | LOAD3DCAMERA |
| `width` | El ancho del renderizado de la vista previa. | INT |
| `height` | La altura del renderizado de la vista previa. | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewGaussianSplat/es.md)

---
**Source fingerprint (SHA-256):** `4fc86c692724ce406f9bba9aa9ebe22a92e72a25d11abf8f55d1b99044bb1acd`
