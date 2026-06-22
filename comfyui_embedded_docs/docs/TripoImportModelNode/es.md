# Tripo: Importar modelo

Este nodo importa un archivo de modelo 3D externo al sistema de Tripo para que puedas utilizarlo con los nodos de posprocesamiento de Tripo, como Textura, Rig y Convertir. Carga tu modelo y devuelve un ID de tarea que otros nodos de Tripo pueden usar para hacer referencia al modelo importado.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `model_3d` | Modelo 3D a importar (GLB / FBX / OBJ / STL, hasta 150 MB). Los archivos OBJ y STL no contienen texturas incrustadas. | FILE3D | Sí | GLB<br>FBX<br>OBJ<br>STL<br>Cualquier formato 3D |

**Nota:** Se recomienda el formato GLB porque las texturas se conservan solo cuando están incrustadas directamente en el archivo. Los archivos OBJ y STL no admiten texturas incrustadas. El formato GLTF (.gltf) no es compatible porque hace referencia a archivos externos; utiliza un GLB de un solo archivo en su lugar.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `model task_id` | Un ID de tarea que identifica el modelo importado para usarlo con los nodos de posprocesamiento de Tripo | MODEL_TASK_ID |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImportModelNode/es.md)

---
**Source fingerprint (SHA-256):** `4fa13a108804f2a52190a85b5b5d58ff18190e9d182b556abada444788012fab`
