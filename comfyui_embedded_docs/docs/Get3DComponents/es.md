# Obtener componentes 3D

Get3DComponents analiza un archivo de modelo 3D (GLB, GLTF, OBJ o STL) y lo convierte en una malla editable que puede ser utilizada por nodos de procesamiento de mallas, como decimate, remesh, UV unwrap y bake. Todos los nodos y primitivas de la escena se fusionan en una sola malla con sus transformaciones aplicadas, y las texturas y los ajustes de material provienen del primer material. Es la contraparte del nodo MeshToFile3D.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `model_3d` | Archivo de modelo 3D desde Load 3D u otro nodo 3D. No se admiten FBX/USDZ: convierta a GLB primero. | File3DGLB<br>File3DGLTF<br>File3DOBJ<br>File3DSTL<br>File3DAny | Sí | GLB<br>GLTF<br>OBJ<br>STL |

Nota: los archivos FBX y USDZ no son compatibles y causan un error; conviértalos a GLB o GLTF primero. Si el archivo 3D contiene múltiples materiales, solo se conservan las texturas y los factores de material del primer material (se registra una advertencia). Todas las primitivas de la escena se fusionan en una sola malla con sus transformaciones aplicadas. Este nodo es experimental.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|--------------|
| `mesh` | Malla editable que contiene vértices, caras, UVs, colores de vértice, normales, tangentes e información de material (textura, metal-rugosidad, mapa de normales, emisiva, indicador de no iluminado) extraída del archivo de modelo. | MESH |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Get3DComponents/es.md)

---
**Source fingerprint (SHA-256):** `f2cdc9767a50503988484f09d2b3d110caf086b8cd84f65034a4a1e17a94405e`
