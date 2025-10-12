> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmos7B/es.md)

El nodo ModelMergeCosmos7B fusiona dos modelos de IA mediante una combinación ponderada de componentes específicos. Permite un control detallado sobre cómo se combinan las diferentes partes de los modelos ajustando los pesos individuales para las incrustaciones de posición, los bloques transformadores y las capas finales.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Sí | - | Primer modelo a fusionar |
| `model2` | MODEL | Sí | - | Segundo modelo a fusionar |
| `pos_embedder.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el componente de incrustación de posición (valor por defecto: 1.0) |
| `extra_pos_embedder.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el componente de incrustación de posición adicional (valor por defecto: 1.0) |
| `x_embedder.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el componente de incrustación X (valor por defecto: 1.0) |
| `t_embedder.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el componente de incrustación T (valor por defecto: 1.0) |
| `affline_norm.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el componente de normalización afín (valor por defecto: 1.0) |
| `blocks.block0.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque transformador 0 (valor por defecto: 1.0) |
| `blocks.block1.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque transformador 1 (valor por defecto: 1.0) |
| `blocks.block2.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque transformador 2 (valor por defecto: 1.0) |
| `blocks.block3.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque transformador 3 (valor por defecto: 1.0) |
| `blocks.block4.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque transformador 4 (valor por defecto: 1.0) |
| `blocks.block5.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque transformador 5 (valor por defecto: 1.0) |
| `blocks.block6.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque transformador 6 (valor por defecto: 1.0) |
| `blocks.block7.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque transformador 7 (valor por defecto: 1.0) |
| `blocks.block8.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque transformador 8 (valor por defecto: 1.0) |
| `blocks.block9.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque transformador 9 (valor por defecto: 1.0) |
| `blocks.block10.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque transformador 10 (valor por defecto: 1.0) |
| `blocks.block11.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque transformador 11 (valor por defecto: 1.0) |
| `blocks.block12.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque transformador 12 (valor por defecto: 1.0) |
| `blocks.block13.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque transformador 13 (valor por defecto: 1.0) |
| `blocks.block14.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque transformador 14 (valor por defecto: 1.0) |
| `blocks.block15.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque transformador 15 (valor por defecto: 1.0) |
| `blocks.block16.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque transformador 16 (valor por defecto: 1.0) |
| `blocks.block17.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque transformador 17 (valor por defecto: 1.0) |
| `blocks.block18.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque transformador 18 (valor por defecto: 1.0) |
| `blocks.block19.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque transformador 19 (valor por defecto: 1.0) |
| `blocks.block20.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque transformador 20 (valor por defecto: 1.0) |
| `blocks.block21.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque transformador 21 (valor por defecto: 1.0) |
| `blocks.block22.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque transformador 22 (valor por defecto: 1.0) |
| `blocks.block23.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque transformador 23 (valor por defecto: 1.0) |
| `blocks.block24.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque transformador 24 (valor por defecto: 1.0) |
| `blocks.block25.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque transformador 25 (valor por defecto: 1.0) |
| `blocks.block26.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque transformador 26 (valor por defecto: 1.0) |
| `blocks.block27.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque transformador 27 (valor por defecto: 1.0) |
| `final_layer.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el componente de capa final (valor por defecto: 1.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | El modelo fusionado que combina características de ambos modelos de entrada |
