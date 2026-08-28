# GetMeshInfo

Get Mesh Info informa sobre el número de vértices y caras de una malla, junto con los atributos que contiene (como UVs, colores de vértice, normales y texturas). El informe se muestra en el nodo y se devuelve como salida de texto, mientras que la malla pasa sin cambios.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `malla` | La malla a inspeccionar. El nodo cuenta sus vértices y caras, detecta qué atributos están presentes y deja pasar la malla sin cambios. | MESH | Sí | — |

Nota: Cuando la entrada contiene varias mallas (un lote), el informe muestra los recuentos totales de vértices y caras para todo el lote, más un desglose por malla. Para lotes con relleno de ceros, se utilizan los recuentos por elemento almacenados en los datos de la malla.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `malla` | La malla original, transmitida sin ninguna modificación. | MESH |
| `información` | Un informe de texto multilínea con el recuento de vértices, el recuento de caras y los atributos detectados (uvs, vertex_colors, normals, tangents, texture, metallic_roughness, normal_map). Los recuentos grandes se formatean con comas, por ejemplo "1,234,567 (1.23M)". El mismo texto se muestra en el nodo. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetMeshInfo/es.md)

---
**Source fingerprint (SHA-256):** `cd168a5e69131a4a37f1f47014af2bc2ac2c8aa69e146cf33c2072480b35ebb2`
