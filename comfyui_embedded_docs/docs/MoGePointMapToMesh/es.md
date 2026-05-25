> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePointMapToMesh/es.md)

## Descripción general

Este nodo convierte un mapa de puntos MoGe en una malla 3D. Toma los datos geométricos producidos por un nodo de estimación de profundidad MoGe y los triangula en una malla con coordenadas UV y una textura opcional.

## Entradas

| Parámetro | Tipo de dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `moge_geometry` | MOGE_GEOMETRY | Sí | N/A | Datos geométricos MoGe que contienen mapas de puntos, profundidad y, opcionalmente, la imagen de origen. |
| `batch_index` | INT | Sí | 0 a 4096 | Índice de la imagen dentro de un lote de geometría MoGe para mallar. Los recuentos de vértices por imagen difieren, por lo que los lotes no pueden apilarse en una sola MESH (predeterminado: 0). |
| `decimation` | INT | Sí | 1 a 8 | Paso de vértices; 1 = resolución completa (predeterminado: 1). |
| `discontinuity_threshold` | FLOAT | Sí | 0.0 a 1.0 | Descarta píxeles cuyo rango de profundidad 3x3 supere esta fracción. 0 = desactivado (predeterminado: 0.04). |
| `texture` | BOOLEAN | Sí | Verdadero/Falso | Transfiere la imagen de origen como textura de color base (predeterminado: Verdadero). |

## Salidas

| Nombre de salida | Tipo de dato | Descripción |
|------------------|--------------|-------------|
| `MESH` | MESH | Malla 3D con vértices, caras, coordenadas UV y una textura opcional proveniente de la imagen de origen. |

---
**Source fingerprint (SHA-256):** `65c43d64050d1c63d9efbb6c2bb96123f94c6d356d6341f2975537ac24ace29f`
