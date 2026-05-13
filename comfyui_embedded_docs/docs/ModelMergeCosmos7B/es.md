> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmos7B/es.md)

El nodo ModelMergeCosmos7B fusiona dos modelos de IA utilizando una combinación ponderada de componentes específicos. Permite un control detallado sobre cómo se combinan las diferentes partes de los modelos ajustando pesos individuales para las incrustaciones de posición, los bloques del transformador y las capas finales.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `model1` | MODEL | Sí | - | Primer modelo a fusionar |
| `model2` | MODEL | Sí | - | Segundo modelo a fusionar |
| `pos_embedder.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el componente de incrustación de posición (predeterminado: 1.0) |
| `extra_pos_embedder.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el componente de incrustación de posición adicional (predeterminado: 1.0) |
| `x_embedder.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el componente de incrustación x (predeterminado: 1.0) |
| `t_embedder.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el componente de incrustación t (predeterminado: 1.0) |
| `affline_norm.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el componente de normalización afín (predeterminado: 1.0) |
| `blocks.block0.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 0 del transformador (predeterminado: 1.0) |
| `blocks.block1.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 1 del transformador (predeterminado: 1.0) |
| `blocks.block2.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 2 del transformador (predeterminado: 1.0) |
| `blocks.block3.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 3 del transformador (predeterminado: 1.0) |
| `blocks.block4.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 4 del transformador (predeterminado: 1.0) |
| `blocks.block5.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 5 del transformador (predeterminado: 1.0) |
| `blocks.block6.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 6 del transformador (predeterminado: 1.0) |
| `blocks.block7.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 7 del transformador (predeterminado: 1.0) |
| `blocks.block8.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 8 del transformador (predeterminado: 1.0) |
| `blocks.block9.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 9 del transformador (predeterminado: 1.0) |
| `blocks.block10.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 10 del transformador (predeterminado: 1.0) |
| `blocks.block11.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 11 del transformador (predeterminado: 1.0) |
| `blocks.block12.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 12 del transformador (predeterminado: 1.0) |
| `blocks.block13.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 13 del transformador (predeterminado: 1.0) |
| `blocks.block14.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 14 del transformador (predeterminado: 1.0) |
| `blocks.block15.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 15 del transformador (predeterminado: 1.0) |
| `blocks.block16.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 16 del transformador (predeterminado: 1.0) |
| `blocks.block17.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 17 del transformador (predeterminado: 1.0) |
| `blocks.block18.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 18 del transformador (predeterminado: 1.0) |
| `blocks.block19.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 19 del transformador (predeterminado: 1.0) |
| `blocks.block20.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 20 del transformador (predeterminado: 1.0) |
| `blocks.block21.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 21 del transformador (predeterminado: 1.0) |
| `blocks.block22.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 22 del transformador (predeterminado: 1.0) |
| `blocks.block23.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 23 del transformador (predeterminado: 1.0) |
| `blocks.block24.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 24 del transformador (predeterminado: 1.0) |
| `blocks.block25.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 25 del transformador (predeterminado: 1.0) |
| `blocks.block26.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 26 del transformador (predeterminado: 1.0) |
| `blocks.block27.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 27 del transformador (predeterminado: 1.0) |
| `final_layer.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el componente de capa final (predeterminado: 1.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `model` | MODEL | El modelo fusionado que combina características de ambos modelos de entrada |

---
**Source fingerprint (SHA-256):** `0721b047933179706c76f622efb5b7425aad530d302d8b33ec12dd68513dec0b`
