# ModelMergeCosmos7B

El nodo ModelMergeCosmos7B fusiona dos modelos de IA mediante una combinación ponderada de componentes específicos. Permite un control preciso sobre cómo se combinan las diferentes partes de los modelos ajustando pesos individuales para los embeddings de posición, los bloques de transformador y las capas finales.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model1` | Primer modelo a fusionar | MODEL | Sí | - |
| `model2` | Segundo modelo a fusionar | MODEL | Sí | - |
| `pos_embedder.` | Peso para el componente de embedding de posición (valor predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `extra_pos_embedder.` | Peso para el componente de embedding de posición adicional (valor predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `x_embedder.` | Peso para el componente de embedding x (valor predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `t_embedder.` | Peso para el componente de embedding t (valor predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `affline_norm.` | Peso para el componente de normalización afín (valor predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block0.` | Peso para el bloque de transformador 0 (valor predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block1.` | Peso para el bloque de transformador 1 (valor predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block2.` | Peso para el bloque de transformador 2 (valor predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block3.` | Peso para el bloque de transformador 3 (valor predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block4.` | Peso para el bloque de transformador 4 (valor predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block5.` | Peso para el bloque de transformador 5 (valor predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block6.` | Peso para el bloque de transformador 6 (valor predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block7.` | Peso para el bloque de transformador 7 (valor predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block8.` | Peso para el bloque de transformador 8 (valor predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block9.` | Peso para el bloque de transformador 9 (valor predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block10.` | Peso para el bloque de transformador 10 (valor predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block11.` | Peso para el bloque de transformador 11 (valor predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block12.` | Peso para el bloque de transformador 12 (valor predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block13.` | Peso para el bloque de transformador 13 (valor predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block14.` | Peso para el bloque de transformador 14 (valor predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block15.` | Peso para el bloque de transformador 15 (valor predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block16.` | Peso para el bloque de transformador 16 (valor predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block17.` | Peso para el bloque de transformador 17 (valor predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block18.` | Peso para el bloque de transformador 18 (valor predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block19.` | Peso para el bloque de transformador 19 (valor predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block20.` | Peso para el bloque de transformador 20 (valor predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block21.` | Peso para el bloque de transformador 21 (valor predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block22.` | Peso para el bloque de transformador 22 (valor predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block23.` | Peso para el bloque de transformador 23 (valor predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block24.` | Peso para el bloque de transformador 24 (valor predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block25.` | Peso para el bloque de transformador 25 (valor predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block26.` | Peso para el bloque de transformador 26 (valor predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.block27.` | Peso para el bloque de transformador 27 (valor predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `final_layer.` | Peso para el componente de capa final (valor predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | El modelo fusionado que combina características de ambos modelos de entrada | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmos7B/es.md)

---
**Source fingerprint (SHA-256):** `2cc4dcaa3576c5383c630e233cef55dedc8d742c20197cc83f5832dc9e887dac`
