# MoGe Point Map a Malla

Este nodo convierte un mapa de puntos MoGe en una malla 3D. Toma los datos de geometría producidos por un nodo de estimación de profundidad MoGe y triangula una imagen de ellos para crear una malla con coordenadas UV y una textura opcional.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `moge_geometry` | Los datos de geometría MoGe que contienen mapas de puntos, profundidad y opcionalmente la imagen de origen. | MOGE_GEOMETRY | Sí | N/A |
| `batch_index` | Qué imagen de una geometría MoGe por lotes se convertirá en malla. El recuento de vértices por imagen difiere, por lo que los lotes no se pueden apilar en un solo MESH (predeterminado: 0). | INT | Sí | 0 a 4096 |
| `decimation` | Paso de vértices; 1 = resolución completa (predeterminado: 1). | INT | Sí | 1 a 8 |
| `discontinuity_threshold` | Descarta píxeles cuyo rango de profundidad 3x3 supere esta fracción. 0 = desactivado (predeterminado: 0,04). | FLOAT | Sí | 0,0 a 1,0 |
| `texture` | Transmite la imagen de origen como textura baseColor (predeterminado: True). | BOOLEAN | Sí | True/False |

Nota: `batch_index` debe ser menor que el tamaño del lote del `moge_geometry` proporcionado. La geometría de entrada debe contener datos de puntos, y si la malla generada está vacía, el nodo devuelve un error sugiriendo `discontinuity_threshold = 0`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `MESH` | Una malla 3D con vértices, caras, coordenadas UV y una textura opcional de la imagen de origen. | MESH |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePointMapToMesh/es.md)

---
**Source fingerprint (SHA-256):** `626925866eed6805d2ce87529909fc76b9484cd2e8118fdd1669a237d44b9b0b`
