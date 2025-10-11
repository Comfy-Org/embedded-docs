> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmos14B/es.md)

El nodo ModelMergeCosmos14B fusiona dos modelos de IA utilizando un enfoque basado en bloques específicamente diseñado para la arquitectura del modelo Cosmos 14B. Permite combinar diferentes componentes de los modelos ajustando valores de peso entre 0.0 y 1.0 para cada bloque del modelo y capa de embedding.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Sí | - | Primer modelo a fusionar |
| `model2` | MODEL | Sí | - | Segundo modelo a fusionar |
| `pos_embedder.` | FLOAT | Sí | 0.0 - 1.0 | Peso del embedder de posición (valor por defecto: 1.0) |
| `extra_pos_embedder.` | FLOAT | Sí | 0.0 - 1.0 | Peso del embedder de posición extra (valor por defecto: 1.0) |
| `x_embedder.` | FLOAT | Sí | 0.0 - 1.0 | Peso del embedder X (valor por defecto: 1.0) |
| `t_embedder.` | FLOAT | Sí | 0.0 - 1.0 | Peso del embedder T (valor por defecto: 1.0) |
| `affline_norm.` | FLOAT | Sí | 0.0 - 1.0 | Peso de normalización afín (valor por defecto: 1.0) |
| `blocks.block0.` | FLOAT | Sí | 0.0 - 1.0 | Peso del bloque 0 (valor por defecto: 1.0) |
| `blocks.block1.` | FLOAT | Sí | 0.0 - 1.0 | Peso del bloque 1 (valor por defecto: 1.0) |
| `blocks.block2.` | FLOAT | Sí | 0.0 - 1.0 | Peso del bloque 2 (valor por defecto: 1.0) |
| `blocks.block3.` | FLOAT | Sí | 0.0 - 1.0 | Peso del bloque 3 (valor por defecto: 1.0) |
| `blocks.block4.` | FLOAT | Sí | 0.0 - 1.0 | Peso del bloque 4 (valor por defecto: 1.0) |
| `blocks.block5.` | FLOAT | Sí | 0.0 - 1.0 | Peso del bloque 5 (valor por defecto: 1.0) |
| `blocks.block6.` | FLOAT | Sí | 0.0 - 1.0 | Peso del bloque 6 (valor por defecto: 1.0) |
| `blocks.block7.` | FLOAT | Sí | 0.0 - 1.0 | Peso del bloque 7 (valor por defecto: 1.0) |
| `blocks.block8.` | FLOAT | Sí | 0.0 - 1.0 | Peso del bloque 8 (valor por defecto: 1.0) |
| `blocks.block9.` | FLOAT | Sí | 0.0 - 1.0 | Peso del bloque 9 (valor por defecto: 1.0) |
| `blocks.block10.` | FLOAT | Sí | 0.0 - 1.0 | Peso del bloque 10 (valor por defecto: 1.0) |
| `blocks.block11.` | FLOAT | Sí | 0.0 - 1.0 | Peso del bloque 11 (valor por defecto: 1.0) |
| `blocks.block12.` | FLOAT | Sí | 0.0 - 1.0 | Peso del bloque 12 (valor por defecto: 1.0) |
| `blocks.block13.` | FLOAT | Sí | 0.0 - 1.0 | Peso del bloque 13 (valor por defecto: 1.0) |
| `blocks.block14.` | FLOAT | Sí | 0.0 - 1.0 | Peso del bloque 14 (valor por defecto: 1.0) |
| `blocks.block15.` | FLOAT | Sí | 0.0 - 1.0 | Peso del bloque 15 (valor por defecto: 1.0) |
| `blocks.block16.` | FLOAT | Sí | 0.0 - 1.0 | Peso del bloque 16 (valor por defecto: 1.0) |
| `blocks.block17.` | FLOAT | Sí | 0.0 - 1.0 | Peso del bloque 17 (valor por defecto: 1.0) |
| `blocks.block18.` | FLOAT | Sí | 0.0 - 1.0 | Peso del bloque 18 (valor por defecto: 1.0) |
| `blocks.block19.` | FLOAT | Sí | 0.0 - 1.0 | Peso del bloque 19 (valor por defecto: 1.0) |
| `blocks.block20.` | FLOAT | Sí | 0.0 - 1.0 | Peso del bloque 20 (valor por defecto: 1.0) |
| `blocks.block21.` | FLOAT | Sí | 0.0 - 1.0 | Peso del bloque 21 (valor por defecto: 1.0) |
| `blocks.block22.` | FLOAT | Sí | 0.0 - 1.0 | Peso del bloque 22 (valor por defecto: 1.0) |
| `blocks.block23.` | FLOAT | Sí | 0.0 - 1.0 | Peso del bloque 23 (valor por defecto: 1.0) |
| `blocks.block24.` | FLOAT | Sí | 0.0 - 1.0 | Peso del bloque 24 (valor por defecto: 1.0) |
| `blocks.block25.` | FLOAT | Sí | 0.0 - 1.0 | Peso del bloque 25 (valor por defecto: 1.0) |
| `blocks.block26.` | FLOAT | Sí | 0.0 - 1.0 | Peso del bloque 26 (valor por defecto: 1.0) |
| `blocks.block27.` | FLOAT | Sí | 0.0 - 1.0 | Peso del bloque 27 (valor por defecto: 1.0) |
| `blocks.block28.` | FLOAT | Sí | 0.0 - 1.0 | Peso del bloque 28 (valor por defecto: 1.0) |
| `blocks.block29.` | FLOAT | Sí | 0.0 - 1.0 | Peso del bloque 29 (valor por defecto: 1.0) |
| `blocks.block30.` | FLOAT | Sí | 0.0 - 1.0 | Peso del bloque 30 (valor por defecto: 1.0) |
| `blocks.block31.` | FLOAT | Sí | 0.0 - 1.0 | Peso del bloque 31 (valor por defecto: 1.0) |
| `blocks.block32.` | FLOAT | Sí | 0.0 - 1.0 | Peso del bloque 32 (valor por defecto: 1.0) |
| `blocks.block33.` | FLOAT | Sí | 0.0 - 1.0 | Peso del bloque 33 (valor por defecto: 1.0) |
| `blocks.block34.` | FLOAT | Sí | 0.0 - 1.0 | Peso del bloque 34 (valor por defecto: 1.0) |
| `blocks.block35.` | FLOAT | Sí | 0.0 - 1.0 | Peso del bloque 35 (valor por defecto: 1.0) |
| `final_layer.` | FLOAT | Sí | 0.0 - 1.0 | Peso de la capa final (valor por defecto: 1.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | El modelo fusionado que combina características de ambos modelos de entrada |