El nodo **ModelMergeCosmos14B** fusiona dos modelos de IA utilizando un enfoque basado en bloques diseñado específicamente para la arquitectura del modelo Cosmos 14B. Permite combinar diferentes componentes de los modelos ajustando valores de peso entre 0.0 y 1.0 para cada bloque del modelo y capa de incrustación (embedding).

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `model1` | Primer modelo a fusionar | MODEL | Sí | - |
| `model2` | Segundo modelo a fusionar | MODEL | Sí | - |
| `pos_embedder.` | Peso para el componente incrustador de posición (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `extra_pos_embedder.` | Peso para el componente incrustador de posición adicional (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `x_embedder.` | Peso para el componente incrustador x (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `t_embedder.` | Peso para el componente incrustador t (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `affline_norm.` | Peso para el componente de normalización afín (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block0.` | Peso para el bloque 0 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block1.` | Peso para el bloque 1 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block2.` | Peso para el bloque 2 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block3.` | Peso para el bloque 3 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block4.` | Peso para el bloque 4 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block5.` | Peso para el bloque 5 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block6.` | Peso para el bloque 6 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block7.` | Peso para el bloque 7 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block8.` | Peso para el bloque 8 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block9.` | Peso para el bloque 9 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block10.` | Peso para el bloque 10 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block11.` | Peso para el bloque 11 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block12.` | Peso para el bloque 12 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block13.` | Peso para el bloque 13 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block14.` | Peso para el bloque 14 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block15.` | Peso para el bloque 15 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block16.` | Peso para el bloque 16 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block17.` | Peso para el bloque 17 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block18.` | Peso para el bloque 18 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block19.` | Peso para el bloque 19 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block20.` | Peso para el bloque 20 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block21.` | Peso para el bloque 21 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block22.` | Peso para el bloque 22 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block23.` | Peso para el bloque 23 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block24.` | Peso para el bloque 24 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block25.` | Peso para el bloque 25 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block26.` | Peso para el bloque 26 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block27.` | Peso para el bloque 27 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block28.` | Peso para el bloque 28 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block29.` | Peso para el bloque 29 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block30.` | Peso para el bloque 30 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block31.` | Peso para el bloque 31 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block32.` | Peso para el bloque 32 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block33.` | Peso para el bloque 33 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block34.` | Peso para el bloque 34 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block35.` | Peso para el bloque 35 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `final_layer.` | Peso para la capa final (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `model` | El modelo fusionado que combina características de ambos modelos de entrada | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmos14B/es.md)

---
**Source fingerprint (SHA-256):** `6fcb4fefe7738d0addef49d386c0d3d22cda4c68f0e49ad003d1df595cf0e9d9`
