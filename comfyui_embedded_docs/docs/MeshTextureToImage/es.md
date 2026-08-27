# MeshTextureToImage

Este nodo extrae las texturas horneadas de una malla y las devuelve como imágenes separadas: color base, metalness, rugosidad, oclusión y mapa normal. Los canales de textura que no fueron horneados se devuelven con valores neutros por defecto: blanco para la oclusión y azul plano para el mapa normal.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `mesh` | La malla cuyas texturas horneadas se extraen. La malla debe tener una textura de color base; las mallas que solo tienen colores de vértice (por ejemplo, después de un nodo PaintMesh) no contienen una textura y provocan un error. | MESH | Sí | — |

Nota: La malla debe tener una textura de color base horneada. Si no la tiene, el nodo genera un error y recomienda ejecutar primero BakeTextureFromVoxel. Cuando la textura de metalness-rugosidad falta, las salidas `metallic` y `roughness` son negras (0). La salida `occlusion` es blanca a menos que la malla contenga oclusión ambiental horneada. La salida `normal_map` es un azul neutro plano cuando no se horneó ningún mapa normal.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `base_color` | La textura de color base de la malla como imagen. | IMAGE |
| `metallic` | El canal de metalness de la textura de oclusión-rugosidad-metalness de la malla, como imagen en escala de grises. Negro (0) significa no metálico, blanco (1) significa totalmente metálico. Negro cuando falta la textura. | IMAGE |
| `roughness` | El canal de rugosidad de la textura de oclusión-rugosidad-metalness de la malla, como imagen en escala de grises. Negro cuando falta la textura. | IMAGE |
| `occlusion` | El canal de oclusión ambiental de la textura de oclusión-rugosidad-metalness de la malla, como imagen en escala de grises. Blanco (sin oclusión) cuando la oclusión ambiental no fue horneada. | IMAGE |
| `normal_map` | La textura de mapa normal de la malla. Un mapa normal neutro plano (0.5, 0.5, 1.0, que aparece como azul plano) cuando no se horneó ningún mapa normal. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshTextureToImage/es.md)

---
**Source fingerprint (SHA-256):** `775fd50601ed9ebfc48abf1832c58acbac0f48b5faaebb5f7f46ae4a501278c4`
