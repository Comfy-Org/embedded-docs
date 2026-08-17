# ModelMergeCosmosPredict2_2B

El nodo ModelMergeCosmosPredict2_2B fusiona dos modelos de difusión mediante un enfoque basado en bloques con control fino sobre diferentes componentes del modelo. Permite combinar partes específicas de dos modelos ajustando los pesos de interpolación para los codificadores de posición, codificadores de tiempo, bloques de transformador y capas finales. Esto proporciona un control preciso sobre cómo los diferentes componentes arquitectónicos de cada modelo contribuyen al resultado final fusionado.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model1` | El primer modelo a fusionar | MODEL | Sí | - |
| `model2` | El segundo modelo a fusionar | MODEL | Sí | - |
| `pos_embedder.` | Peso de interpolación del codificador de posición (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `x_embedder.` | Peso de interpolación del codificador de entrada (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `t_embedder.` | Peso de interpolación del codificador de tiempo (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `t_embedding_norm.` | Peso de interpolación de la normalización de la codificación de tiempo (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.0.` | Peso de interpolación del bloque de transformador 0 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.1.` | Peso de interpolación del bloque de transformador 1 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.2.` | Peso de interpolación del bloque de transformador 2 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.3.` | Peso de interpolación del bloque de transformador 3 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.4.` | Peso de interpolación del bloque de transformador 4 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.5.` | Peso de interpolación del bloque de transformador 5 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.6.` | Peso de interpolación del bloque de transformador 6 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.7.` | Peso de interpolación del bloque de transformador 7 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.8.` | Peso de interpolación del bloque de transformador 8 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.9.` | Peso de interpolación del bloque de transformador 9 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.10.` | Peso de interpolación del bloque de transformador 10 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.11.` | Peso de interpolación del bloque de transformador 11 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.12.` | Peso de interpolación del bloque de transformador 12 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.13.` | Peso de interpolación del bloque de transformador 13 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.14.` | Peso de interpolación del bloque de transformador 14 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.15.` | Peso de interpolación del bloque de transformador 15 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.16.` | Peso de interpolación del bloque de transformador 16 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.17.` | Peso de interpolación del bloque de transformador 17 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.18.` | Peso de interpolación del bloque de transformador 18 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.19.` | Peso de interpolación del bloque de transformador 19 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.20.` | Peso de interpolación del bloque de transformador 20 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.21.` | Peso de interpolación del bloque de transformador 21 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.22.` | Peso de interpolación del bloque de transformador 22 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.23.` | Peso de interpolación del bloque de transformador 23 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.24.` | Peso de interpolación del bloque de transformador 24 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.25.` | Peso de interpolación del bloque de transformador 25 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.26.` | Peso de interpolación del bloque de transformador 26 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.27.` | Peso de interpolación del bloque de transformador 27 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `final_layer.` | Peso de interpolación de la capa final (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | El modelo fusionado que combina características de ambos modelos de entrada | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmosPredict2_2B/es.md)

---
**Source fingerprint (SHA-256):** `3586868201320ae9a326a08f6a9bd74511a5342bf8496e7efcb9f45cf4b7c55d`
