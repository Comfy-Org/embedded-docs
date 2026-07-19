# MoGe Point Map a Malla

## Descripción general

Este nodo convierte un mapa de puntos MoGe en una malla 3D. Toma los datos geométricos producidos por un nodo de estimación de profundidad MoGe y los triangula en una malla con coordenadas UV y una textura opcional.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `moge_geometry` | Datos geométricos MoGe que contienen mapas de puntos, profundidad y, opcionalmente, la imagen de origen. | MOGE_GEOMETRY | Sí | N/A |
| `batch_index` | Índice de la imagen dentro de un lote de geometría MoGe para mallar. Los recuentos de vértices por imagen difieren, por lo que los lotes no pueden apilarse en una sola MESH (predeterminado: 0). | INT | Sí | 0 a 4096 |
| `decimation` | Paso de vértices; 1 = resolución completa (predeterminado: 1). | INT | Sí | 1 a 8 |
| `discontinuity_threshold` | Descarta píxeles cuyo rango de profundidad 3x3 supere esta fracción. 0 = desactivado (predeterminado: 0.04). | FLOAT | Sí | 0.0 a 1.0 |
| `texture` | Transfiere la imagen de origen como textura de color base (predeterminado: Verdadero). | BOOLEAN | Sí | Verdadero/Falso |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `MESH` | Malla 3D con vértices, caras, coordenadas UV y una textura opcional proveniente de la imagen de origen. | MESH |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePointMapToMesh/es.md)

---
**Source fingerprint (SHA-256):** `65c43d64050d1c63d9efbb6c2bb96123f94c6d356d6341f2975537ac24ace29f`
