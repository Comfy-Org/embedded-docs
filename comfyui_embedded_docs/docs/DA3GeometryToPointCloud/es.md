# Convertir Geometría DA3 a Nube de Puntos

Este nodo convierte un mapa de profundidad de un objeto DA3_GEOMETRY en una nube de puntos 3D. Aplica filtrado basado en máscaras de confianza y cielo, y transforma los puntos a un sistema de coordenadas mundial común adecuado para escenas multivista.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `da3_geometry` | El objeto DA3_GEOMETRY que contiene datos de profundidad y mapas opcionales de imagen, confianza y cielo | DA3_GEOMETRY | Sí | - |
| `batch_index` | Qué imagen de un lote convertir (predeterminado: 0) | INT | Sí | 0 a 4096 |
| `confidence_threshold` | Excluir píxeles cuya confianza normalizada por imagen esté por debajo de este valor (0 = conservar todos). Se usa cuando la geometría tiene un mapa de confianza (modelos Small/Base). (predeterminado: 0.1) | FLOAT | Sí | 0.0 a 1.0 |
| `use_sky_mask` | Excluir píxeles de probabilidad de cielo (cielo >= 0.5). Se usa cuando la geometría tiene un mapa de cielo (modelos Mono/Metric). (predeterminado: True) | BOOLEAN | Sí | True o False |
| `downsample` | Tomar cada N-ésimo píxel (1 = resolución completa). Valores más altos generan menos puntos y procesamiento más rápido. (predeterminado: 1) | INT | Sí | 1 a 16 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `point_cloud` | Un objeto de nube de puntos que contiene puntos 3D filtrados, colores opcionales y valores de confianza opcionales | DA3_POINT_CLOUD |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DA3GeometryToPointCloud/es.md)

---
**Source fingerprint (SHA-256):** `3cf5bdbb8afdfcfc02f9832a8cbc5a3df49da755dea6df01792aa6ef9e5d7287`
