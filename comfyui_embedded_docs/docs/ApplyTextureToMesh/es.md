# ApplyTextureToMesh

Este nodo adjunta imágenes de texturas horneadas a la disposición UV de una malla para que puedan exportarse junto con la malla mediante el nodo SaveGLB. Conecte la misma malla con UV desplegados que usó para el horneado, junto con los mapas de imagen horneados. Los mapas opcionales de metalicidad, rugosidad y oclusión se empaquetan en una única textura ORM, y al proporcionar un mapa de normales también se almacenan las normales suavizadas y las tangentes necesarias para un sombreado correcto.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `mesh` | La malla con UV desplegados a la que se adjuntarán las texturas horneadas. Debe ser la misma malla utilizada durante el horneado; se genera un error si la malla no tiene UVs. | MESH | Sí | — |
| `base_color` | La imagen de color base horneada. Se almacena como la textura de la malla y se limita al rango 0-1. | IMAGE | Sí | — |
| `metallic` | El mapa de metalicidad horneado. Se utiliza como el canal azul de la textura ORM combinada; por defecto es 0 cuando no se proporciona. | IMAGE | No | — |
| `roughness` | El mapa de rugosidad horneado. Se utiliza como el canal verde de la textura ORM combinada; por defecto es 1 cuando no se proporciona. | IMAGE | No | — |
| `occlusion` | El mapa de oclusión ambiental horneado. Se utiliza como el canal rojo de la textura ORM combinada; por defecto es 1 cuando no se proporciona. Cuando se proporciona, la textura ORM también se marca como la textura de oclusión para SaveGLB. | IMAGE | No | — |
| `normal_map` | El mapa de normales horneado en espacio tangente. Cuando se proporciona, el nodo recalcula la base de tangentes por vértice y exporta normales de vértice suavizadas para que el mapa de normales sombree correctamente. | IMAGE | No | — |

Nota: Cuando se conecta cualquiera de los parámetros `metallic`, `roughness` o `occlusion`, los tres se empaquetan en una única textura ORM glTF con canales R = oclusión, G = rugosidad, B = metalicidad. Los mapas faltantes se rellenan con valores predeterminados (oclusión 1, rugosidad 1, metalicidad 0), y los mapas con diferentes resoluciones se redimensionan a la mayor anchura y altura. Cuando se conecta `normal_map`, las normales de la malla se reemplazan con normales de vértice suavizadas calculadas y se añade una base de tangentes. Las coordenadas UV que quedan fuera del rango [0,1] se escalan uniformemente dentro de [0,1] conservando la relación de aspecto.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `mesh` | La malla de entrada con las imágenes de textura adjuntas a su disposición UV, lista para ser guardada por SaveGLB. | MESH |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ApplyTextureToMesh/es.md)

---
**Source fingerprint (SHA-256):** `f91985ef686beddccc41a72614b3d263b4e0d9f1a156db6017d620de26d7b6cf`
