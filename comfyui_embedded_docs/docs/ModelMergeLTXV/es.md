> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeLTXV/es.md)

El nodo ModelMergeLTXV realiza operaciones avanzadas de fusión de modelos específicamente diseñadas para arquitecturas de modelos LTXV. Permite combinar dos modelos diferentes ajustando los pesos de interpolación para varios componentes del modelo, incluyendo bloques transformadores, capas de proyección y otros módulos especializados.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Sí | - | El primer modelo a fusionar |
| `model2` | MODEL | Sí | - | El segundo modelo a fusionar |
| `patchify_proj.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación para las capas de proyección de parcheo (valor por defecto: 1.0) |
| `adaln_single.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación para las capas únicas de normalización adaptativa de capas (valor por defecto: 1.0) |
| `caption_projection.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación para las capas de proyección de subtítulos (valor por defecto: 1.0) |
| `transformer_blocks.0.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación para el bloque transformador 0 (valor por defecto: 1.0) |
| `transformer_blocks.1.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación para el bloque transformador 1 (valor por defecto: 1.0) |
| `transformer_blocks.2.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación para el bloque transformador 2 (valor por defecto: 1.0) |
| `transformer_blocks.3.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación para el bloque transformador 3 (valor por defecto: 1.0) |
| `transformer_blocks.4.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación para el bloque transformador 4 (valor por defecto: 1.0) |
| `transformer_blocks.5.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación para el bloque transformador 5 (valor por defecto: 1.0) |
| `transformer_blocks.6.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación para el bloque transformador 6 (valor por defecto: 1.0) |
| `transformer_blocks.7.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación para el bloque transformador 7 (valor por defecto: 1.0) |
| `transformer_blocks.8.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación para el bloque transformador 8 (valor por defecto: 1.0) |
| `transformer_blocks.9.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación para el bloque transformador 9 (valor por defecto: 1.0) |
| `transformer_blocks.10.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación para el bloque transformador 10 (valor por defecto: 1.0) |
| `transformer_blocks.11.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación para el bloque transformador 11 (valor por defecto: 1.0) |
| `transformer_blocks.12.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación para el bloque transformador 12 (valor por defecto: 1.0) |
| `transformer_blocks.13.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación para el bloque transformador 13 (valor por defecto: 1.0) |
| `transformer_blocks.14.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación para el bloque transformador 14 (valor por defecto: 1.0) |
| `transformer_blocks.15.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación para el bloque transformador 15 (valor por defecto: 1.0) |
| `transformer_blocks.16.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación para el bloque transformador 16 (valor por defecto: 1.0) |
| `transformer_blocks.17.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación para el bloque transformador 17 (valor por defecto: 1.0) |
| `transformer_blocks.18.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación para el bloque transformador 18 (valor por defecto: 1.0) |
| `transformer_blocks.19.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación para el bloque transformador 19 (valor por defecto: 1.0) |
| `transformer_blocks.20.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación para el bloque transformador 20 (valor por defecto: 1.0) |
| `transformer_blocks.21.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación para el bloque transformador 21 (valor por defecto: 1.0) |
| `transformer_blocks.22.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación para el bloque transformador 22 (valor por defecto: 1.0) |
| `transformer_blocks.23.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación para el bloque transformador 23 (valor por defecto: 1.0) |
| `transformer_blocks.24.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación para el bloque transformador 24 (valor por defecto: 1.0) |
| `transformer_blocks.25.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación para el bloque transformador 25 (valor por defecto: 1.0) |
| `transformer_blocks.26.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación para el bloque transformador 26 (valor por defecto: 1.0) |
| `transformer_blocks.27.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación para el bloque transformador 27 (valor por defecto: 1.0) |
| `scale_shift_table` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación para la tabla de escala y desplazamiento (valor por defecto: 1.0) |
| `proj_out.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación para las capas de salida de proyección (valor por defecto: 1.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | El modelo fusionado que combina características de ambos modelos de entrada según los pesos de interpolación especificados |
