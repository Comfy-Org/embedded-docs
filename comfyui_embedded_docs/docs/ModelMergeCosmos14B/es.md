> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmos14B/es.md)

El nodo **ModelMergeCosmos14B** fusiona dos modelos de IA utilizando un enfoque basado en bloques diseñado específicamente para la arquitectura del modelo Cosmos 14B. Permite combinar diferentes componentes de los modelos ajustando valores de peso entre 0.0 y 1.0 para cada bloque del modelo y capa de incrustación (embedding).

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `model1` | MODEL | Sí | - | Primer modelo a fusionar |
| `model2` | MODEL | Sí | - | Segundo modelo a fusionar |
| `pos_embedder.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el componente incrustador de posición (predeterminado: 1.0) |
| `extra_pos_embedder.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el componente incrustador de posición adicional (predeterminado: 1.0) |
| `x_embedder.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el componente incrustador x (predeterminado: 1.0) |
| `t_embedder.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el componente incrustador t (predeterminado: 1.0) |
| `affline_norm.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el componente de normalización afín (predeterminado: 1.0) |
| `blocks.block0.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 0 (predeterminado: 1.0) |
| `blocks.block1.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 1 (predeterminado: 1.0) |
| `blocks.block2.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 2 (predeterminado: 1.0) |
| `blocks.block3.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 3 (predeterminado: 1.0) |
| `blocks.block4.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 4 (predeterminado: 1.0) |
| `blocks.block5.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 5 (predeterminado: 1.0) |
| `blocks.block6.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 6 (predeterminado: 1.0) |
| `blocks.block7.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 7 (predeterminado: 1.0) |
| `blocks.block8.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 8 (predeterminado: 1.0) |
| `blocks.block9.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 9 (predeterminado: 1.0) |
| `blocks.block10.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 10 (predeterminado: 1.0) |
| `blocks.block11.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 11 (predeterminado: 1.0) |
| `blocks.block12.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 12 (predeterminado: 1.0) |
| `blocks.block13.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 13 (predeterminado: 1.0) |
| `blocks.block14.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 14 (predeterminado: 1.0) |
| `blocks.block15.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 15 (predeterminado: 1.0) |
| `blocks.block16.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 16 (predeterminado: 1.0) |
| `blocks.block17.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 17 (predeterminado: 1.0) |
| `blocks.block18.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 18 (predeterminado: 1.0) |
| `blocks.block19.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 19 (predeterminado: 1.0) |
| `blocks.block20.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 20 (predeterminado: 1.0) |
| `blocks.block21.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 21 (predeterminado: 1.0) |
| `blocks.block22.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 22 (predeterminado: 1.0) |
| `blocks.block23.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 23 (predeterminado: 1.0) |
| `blocks.block24.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 24 (predeterminado: 1.0) |
| `blocks.block25.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 25 (predeterminado: 1.0) |
| `blocks.block26.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 26 (predeterminado: 1.0) |
| `blocks.block27.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 27 (predeterminado: 1.0) |
| `blocks.block28.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 28 (predeterminado: 1.0) |
| `blocks.block29.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 29 (predeterminado: 1.0) |
| `blocks.block30.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 30 (predeterminado: 1.0) |
| `blocks.block31.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 31 (predeterminado: 1.0) |
| `blocks.block32.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 32 (predeterminado: 1.0) |
| `blocks.block33.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 33 (predeterminado: 1.0) |
| `blocks.block34.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 34 (predeterminado: 1.0) |
| `blocks.block35.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 35 (predeterminado: 1.0) |
| `final_layer.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la capa final (predeterminado: 1.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `model` | MODEL | El modelo fusionado que combina características de ambos modelos de entrada |

---
**Source fingerprint (SHA-256):** `6fcb4fefe7738d0addef49d386c0d3d22cda4c68f0e49ad003d1df595cf0e9d9`
