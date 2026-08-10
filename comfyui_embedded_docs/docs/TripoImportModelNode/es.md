# Tripo: Importar modelo

Este nodo importa un modelo 3D externo a Tripo para que otros nodos de posprocesamiento de Tripo, como Texture, Rig y Convert, puedan usarlo. El nodo sube el modelo y devuelve un ID de tarea que identifica el modelo importado. Se recomienda GLB porque las texturas se conservan solo cuando están incrustadas en el archivo, y texturizar un modelo importado requiere una indicación de textura.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `model_3d` | Modelo 3D a importar (GLB / FBX / OBJ / STL, hasta 150 MB). Los archivos OBJ y STL no contienen texturas incrustadas. | FILE3D | Sí | GLB<br>FBX<br>OBJ<br>STL<br>Cualquier formato 3D |

**Nota:** Solo se admiten los formatos GLB, FBX, OBJ y STL. GLTF (.gltf) no se puede importar porque hace referencia a archivos externos; use un GLB de un solo archivo en su lugar. El archivo de modelo debe tener 150 MB o menos. Se recomienda GLB porque las texturas sobreviven a la importación solo cuando están incrustadas en el archivo. Los archivos OBJ y STL no incluyen texturas incrustadas. Texturizar un modelo importado requiere una indicación de textura.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `model task_id` | Un ID de tarea que identifica el modelo importado para usarlo con los nodos de posprocesamiento de Tripo | MODEL_TASK_ID |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImportModelNode/es.md)

---
**Source fingerprint (SHA-256):** `4fa13a108804f2a52190a85b5b5d58ff18190e9d182b556abada444788012fab`
