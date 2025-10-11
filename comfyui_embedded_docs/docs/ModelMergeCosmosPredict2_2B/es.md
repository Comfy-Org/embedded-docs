> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmosPredict2_2B/es.md)

El nodo ModelMergeCosmosPredict2_2B fusiona dos modelos de difusión utilizando un enfoque basado en bloques con control detallado sobre diferentes componentes del modelo. Permite combinar partes específicas de dos modelos ajustando los pesos de interpolación para los incrustadores de posición, incrustadores de tiempo, bloques transformadores y capas finales. Esto proporciona un control preciso sobre cómo los diferentes componentes arquitectónicos de cada modelo contribuyen al resultado fusionado final.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Sí | - | El primer modelo a fusionar |
| `model2` | MODEL | Sí | - | El segundo modelo a fusionar |
| `pos_embedder.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del incrustador de posición (por defecto: 1.0) |
| `x_embedder.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del incrustador de entrada (por defecto: 1.0) |
| `t_embedder.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del incrustador de tiempo (por defecto: 1.0) |
| `t_embedding_norm.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación de la normalización de incrustación de tiempo (por defecto: 1.0) |
| `blocks.0.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque transformador 0 (por defecto: 1.0) |
| `blocks.1.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque transformador 1 (por defecto: 1.0) |
| `blocks.2.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque transformador 2 (por defecto: 1.0) |
| `blocks.3.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque transformador 3 (por defecto: 1.0) |
| `blocks.4.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque transformador 4 (por defecto: 1.0) |
| `blocks.5.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque transformador 5 (por defecto: 1.0) |
| `blocks.6.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque transformador 6 (por defecto: 1.0) |
| `blocks.7.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque transformador 7 (por defecto: 1.0) |
| `blocks.8.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque transformador 8 (por defecto: 1.0) |
| `blocks.9.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque transformador 9 (por defecto: 1.0) |
| `blocks.10.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque transformador 10 (por defecto: 1.0) |
| `blocks.11.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque transformador 11 (por defecto: 1.0) |
| `blocks.12.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque transformador 12 (por defecto: 1.0) |
| `blocks.13.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque transformador 13 (por defecto: 1.0) |
| `blocks.14.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque transformador 14 (por defecto: 1.0) |
| `blocks.15.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque transformador 15 (por defecto: 1.0) |
| `blocks.16.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque transformador 16 (por defecto: 1.0) |
| `blocks.17.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque transformador 17 (por defecto: 1.0) |
| `blocks.18.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque transformador 18 (por defecto: 1.0) |
| `blocks.19.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque transformador 19 (por defecto: 1.0) |
| `blocks.20.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque transformador 20 (por defecto: 1.0) |
| `blocks.21.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque transformador 21 (por defecto: 1.0) |
| `blocks.22.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque transformador 22 (por defecto: 1.0) |
| `blocks.23.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque transformador 23 (por defecto: 1.0) |
| `blocks.24.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque transformador 24 (por defecto: 1.0) |
| `blocks.25.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque transformador 25 (por defecto: 1.0) |
| `blocks.26.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque transformador 26 (por defecto: 1.0) |
| `blocks.27.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque transformador 27 (por defecto: 1.0) |
| `final_layer.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación de la capa final (por defecto: 1.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | El modelo fusionado que combina características de ambos modelos de entrada |