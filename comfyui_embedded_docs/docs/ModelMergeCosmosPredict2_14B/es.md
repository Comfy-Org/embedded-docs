# ModelMergeCosmosPredict2_14B

El nodo `ModelMergeCosmosPredict2_14B` fusiona dos modelos de IA combinando sus componentes internos. Proporciona un control preciso sobre cuánto influye cada parte del segundo modelo en el resultado final fusionado, utilizando valores de peso ajustables para capas y componentes específicos.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo1` | El modelo base con el que fusionar | MODEL | Sí | - |
| `modelo2` | El modelo secundario para fusionar en el modelo base | MODEL | Sí | - |
| `pos_embedder.` | Peso de mezcla del integrador de posición (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `x_embedder.` | Peso de mezcla del integrador de entrada (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `t_embedder.` | Peso de mezcla del integrador de tiempo (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `t_embedding_norm.` | Peso de mezcla de la normalización de incrustación temporal (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.0.` | Peso de mezcla del bloque 0 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.1.` | Peso de mezcla del bloque 1 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.2.` | Peso de mezcla del bloque 2 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.3.` | Peso de mezcla del bloque 3 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.4.` | Peso de mezcla del bloque 4 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.5.` | Peso de mezcla del bloque 5 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.6.` | Peso de mezcla del bloque 6 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.7.` | Peso de mezcla del bloque 7 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.8.` | Peso de mezcla del bloque 8 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.9.` | Peso de mezcla del bloque 9 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.10.` | Peso de mezcla del bloque 10 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.11.` | Peso de mezcla del bloque 11 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.12.` | Peso de mezcla del bloque 12 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.13.` | Peso de mezcla del bloque 13 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.14.` | Peso de mezcla del bloque 14 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.15.` | Peso de mezcla del bloque 15 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.16.` | Peso de mezcla del bloque 16 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.17.` | Peso de mezcla del bloque 17 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.18.` | Peso de mezcla del bloque 18 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.19.` | Peso de mezcla del bloque 19 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.20.` | Peso de mezcla del bloque 20 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.21.` | Peso de mezcla del bloque 21 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.22.` | Peso de mezcla del bloque 22 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.23.` | Peso de mezcla del bloque 23 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.24.` | Peso de mezcla del bloque 24 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.25.` | Peso de mezcla del bloque 25 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.26.` | Peso de mezcla del bloque 26 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.27.` | Peso de mezcla del bloque 27 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.28.` | Peso de mezcla del bloque 28 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.29.` | Peso de mezcla del bloque 29 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.30.` | Peso de mezcla del bloque 30 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.31.` | Peso de mezcla del bloque 31 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.32.` | Peso de mezcla del bloque 32 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.33.` | Peso de mezcla del bloque 33 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.34.` | Peso de mezcla del bloque 34 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.35.` | Peso de mezcla del bloque 35 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `final_layer.` | Peso de mezcla de la capa final (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |

**Nota:** Todos los parámetros de peso de mezcla aceptan valores entre 0.0 y 1.0, donde 0.0 significa que no hay contribución de `model2` y 1.0 significa contribución completa de `model2` para ese componente específico.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `model` | El modelo fusionado que combina características de ambos modelos de entrada | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmosPredict2_14B/es.md)

---
**Source fingerprint (SHA-256):** `5e72608391bc47c2610c93fda19e6e12a1695f95f6135a08efe97e3d400acf84`
