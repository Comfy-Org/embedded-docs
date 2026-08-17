# ModelMergeLTXV

ModelMergeLTXV fusiona dos modelos LTXV en uno solo combinando sus componentes internos. Cada parámetro de peso controla con qué intensidad una parte específica de `model2` se mezcla en `model1`, donde los valores más bajos favorecen a `model1` y los valores más altos favorecen a `model2`.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model1` | El primer modelo a fusionar | MODEL | Sí | - |
| `model2` | El segundo modelo a fusionar | MODEL | Sí | - |
| `patchify_proj.` | Peso de interpolación para capas de proyección patchify (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `adaln_single.` | Peso de interpolación para capas individuales de normalización adaptativa de capas (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `caption_projection.` | Peso de interpolación para capas de proyección de subtítulos (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.0.` | Peso de interpolación para el bloque Transformer 0 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.1.` | Peso de interpolación para el bloque Transformer 1 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.2.` | Peso de interpolación para el bloque Transformer 2 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.3.` | Peso de interpolación para el bloque Transformer 3 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.4.` | Peso de interpolación para el bloque Transformer 4 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.5.` | Peso de interpolación para el bloque Transformer 5 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.6.` | Peso de interpolación para el bloque Transformer 6 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.7.` | Peso de interpolación para el bloque Transformer 7 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.8.` | Peso de interpolación para el bloque Transformer 8 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.9.` | Peso de interpolación para el bloque Transformer 9 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.10.` | Peso de interpolación para el bloque Transformer 10 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.11.` | Peso de interpolación para el bloque Transformer 11 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.12.` | Peso de interpolación para el bloque Transformer 12 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.13.` | Peso de interpolación para el bloque Transformer 13 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.14.` | Peso de interpolación para el bloque Transformer 14 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.15.` | Peso de interpolación para el bloque Transformer 15 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.16.` | Peso de interpolación para el bloque Transformer 16 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.17.` | Peso de interpolación para el bloque Transformer 17 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.18.` | Peso de interpolación para el bloque Transformer 18 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.19.` | Peso de interpolación para el bloque Transformer 19 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.20.` | Peso de interpolación para el bloque Transformer 20 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.21.` | Peso de interpolación para el bloque Transformer 21 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.22.` | Peso de interpolación para el bloque Transformer 22 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.23.` | Peso de interpolación para el bloque Transformer 23 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.24.` | Peso de interpolación para el bloque Transformer 24 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.25.` | Peso de interpolación para el bloque Transformer 25 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.26.` | Peso de interpolación para el bloque Transformer 26 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.27.` | Peso de interpolación para el bloque Transformer 27 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `scale_shift_table` | Peso de interpolación para la tabla de cambio de escala (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `proj_out.` | Peso de interpolación para capas de salida de proyección (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `model` | El modelo fusionado que combina características de ambos modelos de entrada según los pesos de interpolación especificados | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeLTXV/es.md)

---
**Source fingerprint (SHA-256):** `0ff5f93aee831259066679a27fff8f7cbd4a9686242091f1bc7dd3805725566e`
