# ModelMergeMochiPreview

Este nodo fusiona dos modelos de IA mediante un enfoque basado en bloques con control fino sobre diferentes componentes del modelo. Permite combinar modelos ajustando los pesos de interpolación para secciones específicas, incluyendo frecuencias posicionales, capas de incrustación y bloques individuales del transformador. El proceso de fusión combina las arquitecturas y los parámetros de ambos modelos de entrada según los valores de peso especificados.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model1` | El primer modelo a fusionar | MODEL | Sí | - |
| `model2` | El segundo modelo a fusionar | MODEL | Sí | - |
| `pos_frequencies.` | Peso para la interpolación de frecuencias posicionales (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `t_embedder.` | Peso para la interpolación del incrustador de tiempo (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `t5_y_embedder.` | Peso para la interpolación del incrustador T5-Y (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `t5_yproj.` | Peso para la interpolación de la proyección T5-Y (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.0.` | Peso para la interpolación del bloque 0 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.1.` | Peso para la interpolación del bloque 1 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.2.` | Peso para la interpolación del bloque 2 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.3.` | Peso para la interpolación del bloque 3 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.4.` | Peso para la interpolación del bloque 4 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.5.` | Peso para la interpolación del bloque 5 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.6.` | Peso para la interpolación del bloque 6 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.7.` | Peso para la interpolación del bloque 7 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.8.` | Peso para la interpolación del bloque 8 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.9.` | Peso para la interpolación del bloque 9 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.10.` | Peso para la interpolación del bloque 10 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.11.` | Peso para la interpolación del bloque 11 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.12.` | Peso para la interpolación del bloque 12 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.13.` | Peso para la interpolación del bloque 13 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.14.` | Peso para la interpolación del bloque 14 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.15.` | Peso para la interpolación del bloque 15 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.16.` | Peso para la interpolación del bloque 16 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.17.` | Peso para la interpolación del bloque 17 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.18.` | Peso para la interpolación del bloque 18 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.19.` | Peso para la interpolación del bloque 19 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.20.` | Peso para la interpolación del bloque 20 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.21.` | Peso para la interpolación del bloque 21 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.22.` | Peso para la interpolación del bloque 22 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.23.` | Peso para la interpolación del bloque 23 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.24.` | Peso para la interpolación del bloque 24 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.25.` | Peso para la interpolación del bloque 25 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.26.` | Peso para la interpolación del bloque 26 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.27.` | Peso para la interpolación del bloque 27 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.28.` | Peso para la interpolación del bloque 28 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.29.` | Peso para la interpolación del bloque 29 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.30.` | Peso para la interpolación del bloque 30 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.31.` | Peso para la interpolación del bloque 31 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.32.` | Peso para la interpolación del bloque 32 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.33.` | Peso para la interpolación del bloque 33 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.34.` | Peso para la interpolación del bloque 34 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.35.` | Peso para la interpolación del bloque 35 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.36.` | Peso para la interpolación del bloque 36 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.37.` | Peso para la interpolación del bloque 37 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.38.` | Peso para la interpolación del bloque 38 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.39.` | Peso para la interpolación del bloque 39 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.40.` | Peso para la interpolación del bloque 40 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.41.` | Peso para la interpolación del bloque 41 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.42.` | Peso para la interpolación del bloque 42 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.43.` | Peso para la interpolación del bloque 43 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.44.` | Peso para la interpolación del bloque 44 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.45.` | Peso para la interpolación del bloque 45 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.46.` | Peso para la interpolación del bloque 46 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.47.` | Peso para la interpolación del bloque 47 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `final_layer.` | Peso para la interpolación de la capa final (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | El modelo fusionado que combina características de ambos modelos de entrada según los pesos especificados | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeMochiPreview/es.md)

---
**Source fingerprint (SHA-256):** `8fdf5d023d97ef04bf2b40577be5dbc4c16f8f4437586a98adbdbf7f9fa8a359`
