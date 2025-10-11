> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmosPredict2_14B/es.md)

El nodo ModelMergeCosmosPredict2_14B permite fusionar dos modelos de IA ajustando la influencia de diferentes componentes del modelo. Proporciona control detallado sobre cuánto contribuye cada parte del segundo modelo al modelo fusionado final, utilizando pesos de mezcla para capas y componentes específicos del modelo.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Sí | - | El modelo base con el que fusionar |
| `model2` | MODEL | Sí | - | El modelo secundario que se fusionará en el modelo base |
| `pos_embedder.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla del incrustador de posiciones (valor por defecto: 1.0) |
| `x_embedder.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla del incrustador de entrada (valor por defecto: 1.0) |
| `t_embedder.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla del incrustador de tiempo (valor por defecto: 1.0) |
| `t_embedding_norm.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla de la normalización de incrustación de tiempo (valor por defecto: 1.0) |
| `blocks.0.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla del bloque 0 (valor por defecto: 1.0) |
| `blocks.1.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla del bloque 1 (valor por defecto: 1.0) |
| `blocks.2.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla del bloque 2 (valor por defecto: 1.0) |
| `blocks.3.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla del bloque 3 (valor por defecto: 1.0) |
| `blocks.4.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla del bloque 4 (valor por defecto: 1.0) |
| `blocks.5.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla del bloque 5 (valor por defecto: 1.0) |
| `blocks.6.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla del bloque 6 (valor por defecto: 1.0) |
| `blocks.7.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla del bloque 7 (valor por defecto: 1.0) |
| `blocks.8.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla del bloque 8 (valor por defecto: 1.0) |
| `blocks.9.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla del bloque 9 (valor por defecto: 1.0) |
| `blocks.10.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla del bloque 10 (valor por defecto: 1.0) |
| `blocks.11.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla del bloque 11 (valor por defecto: 1.0) |
| `blocks.12.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla del bloque 12 (valor por defecto: 1.0) |
| `blocks.13.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla del bloque 13 (valor por defecto: 1.0) |
| `blocks.14.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla del bloque 14 (valor por defecto: 1.0) |
| `blocks.15.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla del bloque 15 (valor por defecto: 1.0) |
| `blocks.16.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla del bloque 16 (valor por defecto: 1.0) |
| `blocks.17.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla del bloque 17 (valor por defecto: 1.0) |
| `blocks.18.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla del bloque 18 (valor por defecto: 1.0) |
| `blocks.19.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla del bloque 19 (valor por defecto: 1.0) |
| `blocks.20.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla del bloque 20 (valor por defecto: 1.0) |
| `blocks.21.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla del bloque 21 (valor por defecto: 1.0) |
| `blocks.22.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla del bloque 22 (valor por defecto: 1.0) |
| `blocks.23.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla del bloque 23 (valor por defecto: 1.0) |
| `blocks.24.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla del bloque 24 (valor por defecto: 1.0) |
| `blocks.25.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla del bloque 25 (valor por defecto: 1.0) |
| `blocks.26.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla del bloque 26 (valor por defecto: 1.0) |
| `blocks.27.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla del bloque 27 (valor por defecto: 1.0) |
| `blocks.28.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla del bloque 28 (valor por defecto: 1.0) |
| `blocks.29.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla del bloque 29 (valor por defecto: 1.0) |
| `blocks.30.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla del bloque 30 (valor por defecto: 1.0) |
| `blocks.31.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla del bloque 31 (valor por defecto: 1.0) |
| `blocks.32.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla del bloque 32 (valor por defecto: 1.0) |
| `blocks.33.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla del bloque 33 (valor por defecto: 1.0) |
| `blocks.34.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla del bloque 34 (valor por defecto: 1.0) |
| `blocks.35.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla del bloque 35 (valor por defecto: 1.0) |
| `final_layer.` | FLOAT | Sí | 0.0 - 1.0 | Peso de mezcla de la capa final (valor por defecto: 1.0) |

**Nota:** Todos los parámetros de peso de mezcla aceptan valores entre 0.0 y 1.0, donde 0.0 significa ninguna contribución del model2 y 1.0 significa contribución completa del model2 para ese componente específico.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | El modelo fusionado que combina características de ambos modelos de entrada |