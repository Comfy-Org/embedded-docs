# Vista previa de Splat

El nodo PreviewGaussianSplat muestra un archivo de gaussian splat 3D en una ventana de vista previa sin guardarlo en el directorio de salida de ComfyUI. Acepta un archivo de modelo 3D en varios formatos de gaussian splat, guarda una copia temporal para la vista previa y pasa los datos del modelo para su posterior procesamiento en el flujo de trabajo.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `modelo_3d` | Un archivo 3D de gaussian splat. | FILE3D | Sí | splat<br>ply<br>spz<br>ksplat |
| `info_modelo_3d` | Información de metadatos opcional sobre el modelo 3D. Cuando no está conectado, el nodo usa la información del modelo de `viewport_state`. | LOAD3DMODELINFO | No | - |
| `estado_de_vista` | El estado actual del viewport 3D, incluyendo la información de cámara y modelo. | LOAD3D | Sí | - |
| `info_cámara` | Información de cámara opcional para la vista previa. Cuando no está conectado, el nodo usa la información de cámara de `viewport_state`. | LOAD3DCAMERA | No | - |
| `ancho` | El ancho del render de vista previa en píxeles (valor predeterminado: 1024). | INT | Sí | 1 a 4096 |
| `alto` | La altura del render de vista previa en píxeles (valor predeterminado: 1024). | INT | Sí | 1 a 4096 |

Nota: cuando `camera_info` o `model_3d_info` no se proporcionan, el nodo recurre a la información de cámara y modelo almacenada en `viewport_state`.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `modelo_3d` | El archivo 3D de gaussian splat de entrada, pasado sin cambios. | FILE3D |
| `info_modelo_3d` | Información de metadatos sobre el modelo 3D, ya sea de la entrada o derivada del estado del viewport. | LOAD3DMODELINFO |
| `info_cámara` | Información de cámara para la vista previa, ya sea de la entrada o derivada del estado del viewport. | LOAD3DCAMERA |
| `ancho` | El ancho del render de vista previa. | INT |
| `alto` | La altura del render de vista previa. | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewGaussianSplat/es.md)

---
**Source fingerprint (SHA-256):** `7157a0b34d7bda3e7ec86cb2ac09e0e10ff96ea7037bb6c9d6ad2c879fdedbb2`
