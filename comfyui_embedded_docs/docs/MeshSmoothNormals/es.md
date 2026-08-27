# MeshSmoothNormals

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
|-----------|-------------|--------------|--------------|-------|
| `mesh` | La malla de entrada a procesar. | MESH | Sí | - |
| `crease_angle` | Las aristas cuyo ángulo diedro supera este valor (en grados) permanecen duras (los vértices se dividen). 180 = completamente suave; valores más bajos conservan aristas afiladas (p. ej., ~30-60 para superficies duras). Predeterminado: 180.0. | FLOAT | Sí | 0.0 to 180.0 (step 1.0) |

Cuando `crease_angle` es 180 o más, la topología de la malla no cambia. Cuando se establece por debajo de 180, los vértices se dividen a lo largo de las aristas duras, lo que puede aumentar el número de vértices.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|-----------------|-------------|--------------|
| `mesh` | La malla de entrada con datos normales suaves adjuntos, o con vértices y normales divididos cuando se establece un ángulo de pliegue. | MESH |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshSmoothNormals/es.md)

---
**Source fingerprint (SHA-256):** `bbe9c0fba68369d8e9d3fb68e635869233804f3aac458e7c217d94977e77b9be`
