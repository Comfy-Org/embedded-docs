# ModelMergeLTXV

El nodo ModelMergeLTXV realiza operaciones avanzadas de fusión de modelos específicamente diseñadas para arquitecturas de modelos LTXV. Le permite combinar dos modelos diferentes ajustando los pesos de interpolación de varios componentes del modelo, incluidos los bloques transformer, las capas de proyección y otros módulos especializados.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model1` | El primer modelo a fusionar | MODEL | Sí | - |
| `model2` | El segundo modelo a fusionar | MODEL | Sí | - |
| `patchify_proj.` | Peso de interpolación para las capas de proyección patchify (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (paso: 0.01) |
| `adaln_single.` | Peso de interpolación para las capas individuales de normalización adaptativa (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (paso: 0.01) |
| `caption_projection.` | Peso de interpolación para las capas de proyección de subtítulos (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (paso: 0.01) |
| `transformer_blocks.0.` | Peso de interpolación para el bloque transformer 0 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (paso: 0.01) |
| `transformer_blocks.1.` | Peso de interpolación para el bloque transformer 1 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (paso: 0.01) |
| `transformer_blocks.2.` | Peso de interpolación para el bloque transformer 2 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (paso: 0.01) |
| `transformer_blocks.3.` | Peso de interpolación para el bloque transformer 3 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (paso: 0.01) |
| `transformer_blocks.4.` | Peso de interpolación para el bloque transformer 4 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (paso: 0.01) |
| `transformer_blocks.5.` | Peso de interpolación para el bloque transformer 5 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (paso: 0.01) |
| `transformer_blocks.6.` | Peso de interpolación para el bloque transformer 6 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (paso: 0.01) |
| `transformer_blocks.7.` | Peso de interpolación para el bloque transformer 7 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (paso: 0.01) |
| `transformer_blocks.8.` | Peso de interpolación para el bloque transformer 8 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (paso: 0.01) |
| `transformer_blocks.9.` | Peso de interpolación para el bloque transformer 9 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (paso: 0.01) |
| `transformer_blocks.10.` | Peso de interpolación para el bloque transformer 10 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (paso: 0.01) |
| `transformer_blocks.11.` | Peso de interpolación para el bloque transformer 11 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (paso: 0.01) |
| `transformer_blocks.12.` | Peso de interpolación para el bloque transformer 12 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (paso: 0.01) |
| `transformer_blocks.13.` | Peso de interpolación para el bloque transformer 13 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (paso: 0.01) |
| `transformer_blocks.14.` | Peso de interpolación para el bloque transformer 14 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (paso: 0.01) |
| `transformer_blocks.15.` | Peso de interpolación para el bloque transformer 15 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (paso: 0.01) |
| `transformer_blocks.16.` | Peso de interpolación para el bloque transformer 16 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (paso: 0.01) |
| `transformer_blocks.17.` | Peso de interpolación para el bloque transformer 17 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (paso: 0.01) |
| `transformer_blocks.18.` | Peso de interpolación para el bloque transformer 18 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (paso: 0.01) |
| `transformer_blocks.19.` | Peso de interpolación para el bloque transformer 19 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (paso: 0.01) |
| `transformer_blocks.20.` | Peso de interpolación para el bloque transformer 20 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (paso: 0.01) |
| `transformer_blocks.21.` | Peso de interpolación para el bloque transformer 21 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (paso: 0.01) |
| `transformer_blocks.22.` | Peso de interpolación para el bloque transformer 22 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (paso: 0.01) |
| `transformer_blocks.23.` | Peso de interpolación para el bloque transformer 23 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (paso: 0.01) |
| `transformer_blocks.24.` | Peso de interpolación para el bloque transformer 24 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (paso: 0.01) |
| `transformer_blocks.25.` | Peso de interpolación para el bloque transformer 25 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (paso: 0.01) |
| `transformer_blocks.26.` | Peso de interpolación para el bloque transformer 26 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (paso: 0.01) |
| `transformer_blocks.27.` | Peso de interpolación para el bloque transformer 27 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (paso: 0.01) |
| `scale_shift_table` | Peso de interpolación para la tabla de escala y desplazamiento (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (paso: 0.01) |
| `proj_out.` | Peso de interpolación para las capas de proyección de salida (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (paso: 0.01) |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | El modelo fusionado que combina características de ambos modelos de entrada de acuerdo con los pesos de interpolación especificados | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeLTXV/es.md)

---
**Source fingerprint (SHA-256):** `0ff5f93aee831259066679a27fff8f7cbd4a9686242091f1bc7dd3805725566e`
