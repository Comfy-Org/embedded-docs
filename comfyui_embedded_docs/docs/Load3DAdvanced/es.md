# Load3DAdvanced

Este nodo carga un archivo de modelo 3D desde tu directorio de entrada de ComfyUI y proporciona los datos del modelo junto con información de la cámara y la vista. Soporta formatos de archivo 3D comunes y permite especificar las dimensiones de la imagen de salida para el renderizado.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `model_file` | El archivo de modelo 3D a cargar. Selecciona "none" para omitir la carga de un modelo. | STRING | Sí | `"none"`<br>Lista de archivos 3D disponibles en el directorio input/3d |
| `viewport_state` | El estado actual de la vista que contiene información de la cámara y el modelo desde el visor 3D. | LOAD3D | Sí | - |
| `width` | El ancho de la imagen de salida en píxeles (predeterminado: 1024) | INT | Sí | Mín: 1<br>Máx: 4096<br>Paso: 1 |
| `height` | La altura de la imagen de salida en píxeles (predeterminado: 1024) | INT | Sí | Mín: 1<br>Máx: 4096<br>Paso: 1 |

**Notas sobre los Parámetros:**
- El parámetro `model_file` solo muestra archivos con las siguientes extensiones: .gltf, .glb, .obj, .fbx, .stl
- Los archivos deben colocarse en el directorio `input/3d` de tu instalación de ComfyUI
- Si `model_file` está configurado como "none", no se cargarán datos del modelo 3D (la salida `model_3d` estará vacía)

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `model_3d` | Los datos del modelo 3D cargado, o vacío si no se seleccionó ningún archivo de modelo | FILE3DANY |
| `model_3d_info` | Información sobre el modelo 3D cargado desde el estado de la vista | LOAD3DMODELINFO |
| `camera_info` | Información de la cámara desde el estado de la vista | LOAD3DCAMERA |
| `width` | El ancho de imagen de salida especificado | INT |
| `height` | La altura de imagen de salida especificada | INT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Load3DAdvanced/es.md)

---
**Source fingerprint (SHA-256):** `fdacea8abf627621150e1196743e36f61534333837c33cc9a7416a6d11700c4d`
