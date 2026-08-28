# MeshSmoothNormals

Calcula normales suaves por vértice para una malla y adjúntalas. Las mallas sin normales se sombrean planas (por cara) en los visores glTF; este nodo hace que se sombreen suavemente. Con un ángulo de pliegue inferior a 180, los bordes más pronunciados que el umbral se mantienen duros dividiendo los vértices a lo largo de ellos.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `malla` | La malla de entrada a procesar. | MESH | Sí | - |
| `crease_angle` | Los bordes cuyo ángulo diedro supera este valor (grados) permanecen duros (los vértices se dividen). 180 = totalmente suave; valores más bajos conservan bordes afilados (p. ej. ~30-60 para superficies duras). Predeterminado: 180.0. | FLOAT | Sí | 0.0 a 180.0 (paso 1.0) |

Cuando `crease_angle` es 180 o más, la topología de la malla no cambia. Si se establece por debajo de 180, los vértices se dividen a lo largo de los bordes duros, lo que puede aumentar el número de vértices.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `malla` | La malla de entrada con datos de normales suaves adjuntos, o con vértices y normales divididos cuando se establece un ángulo de pliegue. | MESH |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshSmoothNormals/es.md)

---
**Source fingerprint (SHA-256):** `bbe9c0fba68369d8e9d3fb68e635869233804f3aac458e7c217d94977e77b9be`
