# ApplyTextureToMesh

Este nodo adjunta imágenes de textura horneadas a la disposición UV de una malla para que puedan exportarse junto con la malla mediante el nodo SaveGLB. Conecte la misma malla con UV desenvueltos que utilizó para el horneado, junto con los mapas de imagen horneados. Los mapas opcionales de metalness, rugosidad y oclusión se empaquetan en una única textura ORM, y el suministro de un mapa de normales también almacena las normales suavizadas y las tangentes necesarias para un sombreado correcto.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `mesh` | La malla con UV desenvueltos a la que se adjuntarán las texturas horneadas. Debe ser la misma malla utilizada durante el horneado; se muestra un error si la malla no tiene UVs. | MESH | Sí | — |
| `base_color` | La imagen de color base horneada. Se almacena como textura de la malla y se limita al rango 0-1. | IMAGE | Sí | — |
| `metallic` | El mapa de metalness horneado. Se utiliza como canal azul de la textura ORM combinada; el valor predeterminado es 0 si no se proporciona. | IMAGE | No | — |
| `roughness` | El mapa de rugosidad horneado. Se utiliza como canal verde de la textura ORM combinada; el valor predeterminado es 1 si no se proporciona. | IMAGE | No | — |
| `occlusion` | El mapa de oclusión ambiental horneado. Se utiliza como canal rojo de la textura ORM combinada; el valor predeterminado es 1 si no se proporciona. Cuando se proporciona, la textura ORM también se marca como textura de oclusión para SaveGLB. | IMAGE | No | — |
| `normal_map` | El mapa de normales horneado en espacio tangente. Cuando se proporciona, el nodo recalcula la base tangente por vértice y exporta normales de vértice suavizadas para que el mapa de normales sombree correctamente. | IMAGE | No | — |

Nota: Cuando se conecta cualquiera de `metallic`, `roughness` u `occlusion`, los tres se empaquetan en una única textura ORM (glTF) con canales R = oclusión, G = rugosidad, B = metalness. Los mapas faltantes se rellenan con valores predeterminados (oclusión 1, rugosidad 1, metalness 0), y los mapas con diferentes resoluciones se redimensionan al ancho y alto mayores. Cuando se conecta `normal_map`, las normales de la malla se reemplazan con normales de vértice suavizadas calculadas y se añade una base tangente. Las coordenadas UV que caen fuera del rango [0,1] se escalan uniformemente a [0,1] conservando la proporción de aspecto.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `mesh` | La malla de entrada con las imágenes de textura adjuntas a su disposición UV, lista para ser guardada por SaveGLB. | MESH |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ApplyTextureToMesh/es.md)

---
**Source fingerprint (SHA-256):** `f91985ef686beddccc41a72614b3d263b4e0d9f1a156db6017d620de26d7b6cf`
