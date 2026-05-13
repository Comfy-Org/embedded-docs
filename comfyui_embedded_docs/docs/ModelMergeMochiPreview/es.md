> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeMochiPreview/es.md)

Este nodo fusiona dos modelos de IA utilizando un enfoque basado en bloques con control detallado sobre diferentes componentes del modelo. Permite combinar modelos ajustando los pesos de interpolación para secciones específicas, incluyendo frecuencias posicionales, capas de incrustación y bloques de transformadores individuales. El proceso de fusión combina las arquitecturas y parámetros de ambos modelos de entrada según los valores de peso especificados.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Sí | - | Primer modelo a fusionar |
| `model2` | MODEL | Sí | - | Segundo modelo a fusionar |
| `pos_frequencies.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación de frecuencias posicionales (predeterminado: 1.0) |
| `t_embedder.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del incrustador de tiempo (predeterminado: 1.0) |
| `t5_y_embedder.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del incrustador T5-Y (predeterminado: 1.0) |
| `t5_yproj.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación de la proyección T5-Y (predeterminado: 1.0) |
| `blocks.0.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 0 (predeterminado: 1.0) |
| `blocks.1.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 1 (predeterminado: 1.0) |
| `blocks.2.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 2 (predeterminado: 1.0) |
| `blocks.3.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 3 (predeterminado: 1.0) |
| `blocks.4.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 4 (predeterminado: 1.0) |
| `blocks.5.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 5 (predeterminado: 1.0) |
| `blocks.6.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 6 (predeterminado: 1.0) |
| `blocks.7.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 7 (predeterminado: 1.0) |
| `blocks.8.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 8 (predeterminado: 1.0) |
| `blocks.9.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 9 (predeterminado: 1.0) |
| `blocks.10.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 10 (predeterminado: 1.0) |
| `blocks.11.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 11 (predeterminado: 1.0) |
| `blocks.12.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 12 (predeterminado: 1.0) |
| `blocks.13.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 13 (predeterminado: 1.0) |
| `blocks.14.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 14 (predeterminado: 1.0) |
| `blocks.15.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 15 (predeterminado: 1.0) |
| `blocks.16.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 16 (predeterminado: 1.0) |
| `blocks.17.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 17 (predeterminado: 1.0) |
| `blocks.18.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 18 (predeterminado: 1.0) |
| `blocks.19.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 19 (predeterminado: 1.0) |
| `blocks.20.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 20 (predeterminado: 1.0) |
| `blocks.21.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 21 (predeterminado: 1.0) |
| `blocks.22.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 22 (predeterminado: 1.0) |
| `blocks.23.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 23 (predeterminado: 1.0) |
| `blocks.24.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 24 (predeterminado: 1.0) |
| `blocks.25.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 25 (predeterminado: 1.0) |
| `blocks.26.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 26 (predeterminado: 1.0) |
| `blocks.27.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 27 (predeterminado: 1.0) |
| `blocks.28.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 28 (predeterminado: 1.0) |
| `blocks.29.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 29 (predeterminado: 1.0) |
| `blocks.30.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 30 (predeterminado: 1.0) |
| `blocks.31.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 31 (predeterminado: 1.0) |
| `blocks.32.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 32 (predeterminado: 1.0) |
| `blocks.33.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 33 (predeterminado: 1.0) |
| `blocks.34.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 34 (predeterminado: 1.0) |
| `blocks.35.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 35 (predeterminado: 1.0) |
| `blocks.36.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 36 (predeterminado: 1.0) |
| `blocks.37.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 37 (predeterminado: 1.0) |
| `blocks.38.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 38 (predeterminado: 1.0) |
| `blocks.39.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 39 (predeterminado: 1.0) |
| `blocks.40.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 40 (predeterminado: 1.0) |
| `blocks.41.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 41 (predeterminado: 1.0) |
| `blocks.42.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 42 (predeterminado: 1.0) |
| `blocks.43.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 43 (predeterminado: 1.0) |
| `blocks.44.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 44 (predeterminado: 1.0) |
| `blocks.45.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 45 (predeterminado: 1.0) |
| `blocks.46.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 46 (predeterminado: 1.0) |
| `blocks.47.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación del bloque 47 (predeterminado: 1.0) |
| `final_layer.` | FLOAT | Sí | 0.0 - 1.0 | Peso para la interpolación de la capa final (predeterminado: 1.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | El modelo fusionado que combina características de ambos modelos de entrada según los pesos especificados |

---
**Source fingerprint (SHA-256):** `aebf536f3f89ca8c81141ac871b1b612082c3bd38a29984168b05eccf0cb57e3`
