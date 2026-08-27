# ModelMergeCosmosPredict2_14B

El nodo ModelMergeCosmosPredict2_14B fusiona dos modelos de IA combinando sus componentes internos. Ofrece un control preciso sobre cuánto influye cada parte del segundo modelo en el resultado final fusionado, mediante valores de peso ajustables para capas y componentes específicos.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo1` | El modelo base con el que se realizará la fusión | MODEL | Sí | - |
| `modelo2` | El modelo secundario que se fusiona en el modelo base | MODEL | Sí | - |
| `pos_embedder.` | Peso de mezcla del codificador de posición (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `x_embedder.` | Peso de mezcla del codificador de entrada (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `t_embedder.` | Peso de mezcla del codificador de tiempo (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `t_embedding_norm.` | Peso de mezcla de la normalización de la incrustación temporal (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `bloques.0.` | Peso de mezcla del bloque 0 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `bloques.1.` | Peso de mezcla del bloque 1 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `bloques.2.` | Peso de mezcla del bloque 2 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `bloques.3.` | Peso de mezcla del bloque 3 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `bloques.4.` | Peso de mezcla del bloque 4 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `bloques.5.` | Peso de mezcla del bloque 5 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `bloques.6.` | Peso de mezcla del bloque 6 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `bloques.7.` | Peso de mezcla del bloque 7 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `bloques.8.` | Peso de mezcla del bloque 8 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `bloques.9.` | Peso de mezcla del bloque 9 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `bloques.10.` | Peso de mezcla del bloque 10 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `bloques.11.` | Peso de mezcla del bloque 11 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `bloques.12.` | Peso de mezcla del bloque 12 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `bloques.13.` | Peso de mezcla del bloque 13 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `bloques.14.` | Peso de mezcla del bloque 14 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `bloques.15.` | Peso de mezcla del bloque 15 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `bloques.16.` | Peso de mezcla del bloque 16 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `bloques.17.` | Peso de mezcla del bloque 17 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `bloques.18.` | Peso de mezcla del bloque 18 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `bloques.19.` | Peso de mezcla del bloque 19 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `bloques.20.` | Peso de mezcla del bloque 20 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `bloques.21.` | Peso de mezcla del bloque 21 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `bloques.22.` | Peso de mezcla del bloque 22 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `bloques.23.` | Peso de mezcla del bloque 23 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `bloques.24.` | Peso de mezcla del bloque 24 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `bloques.25.` | Peso de mezcla del bloque 25 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `bloques.26.` | Peso de mezcla del bloque 26 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `bloques.27.` | Peso de mezcla del bloque 27 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `bloques.28.` | Peso de mezcla del bloque 28 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `bloques.29.` | Peso de mezcla del bloque 29 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `bloques.30.` | Peso de mezcla del bloque 30 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `bloques.31.` | Peso de mezcla del bloque 31 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `bloques.32.` | Peso de mezcla del bloque 32 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `bloques.33.` | Peso de mezcla del bloque 33 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `bloques.34.` | Peso de mezcla del bloque 34 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `bloques.35.` | Peso de mezcla del bloque 35 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `final_layer.` | Peso de mezcla de la capa final (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |

**Nota:** Todos los parámetros de peso de mezcla aceptan valores entre 0.0 y 1.0 en incrementos de 0.01, donde 0.0 significa que model2 no contribuye y 1.0 significa que model2 contribuye por completo para ese componente específico.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | El modelo fusionado que combina características de ambos modelos de entrada | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmosPredict2_14B/es.md)

---
**Source fingerprint (SHA-256):** `a5f34deda62dc03f22613517e43996b908a8673dc5da10d8f1b7f6411ece2f0a`
