El nodo ModelMergeCosmos7B fusiona dos modelos de IA utilizando una combinación ponderada de componentes específicos. Permite un control detallado sobre cómo se combinan las diferentes partes de los modelos ajustando pesos individuales para las incrustaciones de posición, los bloques del transformador y las capas finales.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `model1` | Primer modelo a fusionar | MODEL | Sí | - |
| `model2` | Segundo modelo a fusionar | MODEL | Sí | - |
| `pos_embedder.` | Peso para el componente de incrustación de posición (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `extra_pos_embedder.` | Peso para el componente de incrustación de posición adicional (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `x_embedder.` | Peso para el componente de incrustación x (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `t_embedder.` | Peso para el componente de incrustación t (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `affline_norm.` | Peso para el componente de normalización afín (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block0.` | Peso para el bloque 0 del transformador (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block1.` | Peso para el bloque 1 del transformador (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block2.` | Peso para el bloque 2 del transformador (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block3.` | Peso para el bloque 3 del transformador (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block4.` | Peso para el bloque 4 del transformador (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block5.` | Peso para el bloque 5 del transformador (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block6.` | Peso para el bloque 6 del transformador (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block7.` | Peso para el bloque 7 del transformador (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block8.` | Peso para el bloque 8 del transformador (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block9.` | Peso para el bloque 9 del transformador (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block10.` | Peso para el bloque 10 del transformador (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block11.` | Peso para el bloque 11 del transformador (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block12.` | Peso para el bloque 12 del transformador (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block13.` | Peso para el bloque 13 del transformador (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block14.` | Peso para el bloque 14 del transformador (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block15.` | Peso para el bloque 15 del transformador (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block16.` | Peso para el bloque 16 del transformador (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block17.` | Peso para el bloque 17 del transformador (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block18.` | Peso para el bloque 18 del transformador (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block19.` | Peso para el bloque 19 del transformador (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block20.` | Peso para el bloque 20 del transformador (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block21.` | Peso para el bloque 21 del transformador (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block22.` | Peso para el bloque 22 del transformador (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block23.` | Peso para el bloque 23 del transformador (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block24.` | Peso para el bloque 24 del transformador (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block25.` | Peso para el bloque 25 del transformador (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block26.` | Peso para el bloque 26 del transformador (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block27.` | Peso para el bloque 27 del transformador (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `final_layer.` | Peso para el componente de capa final (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `model` | El modelo fusionado que combina características de ambos modelos de entrada | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmos7B/es.md)

---
**Source fingerprint (SHA-256):** `0721b047933179706c76f622efb5b7425aad530d302d8b33ec12dd68513dec0b`
