El nodo ModelMergeLTXV realiza operaciones avanzadas de fusión de modelos diseñadas específicamente para arquitecturas de modelos LTXV. Permite combinar dos modelos diferentes ajustando los pesos de interpolación para diversos componentes del modelo, incluidos bloques transformadores, capas de proyección y otros módulos especializados.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model1` | El primer modelo a fusionar | MODEL | Sí | - |
| `model2` | El segundo modelo a fusionar | MODEL | Sí | - |
| `patchify_proj.` | Peso de interpolación para capas de proyección patchify (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `adaln_single.` | Peso de interpolación para capas individuales de normalización adaptativa (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `caption_projection.` | Peso de interpolación para capas de proyección de subtítulos (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.0.` | Peso de interpolación para el bloque transformador 0 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.1.` | Peso de interpolación para el bloque transformador 1 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.2.` | Peso de interpolación para el bloque transformador 2 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.3.` | Peso de interpolación para el bloque transformador 3 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.4.` | Peso de interpolación para el bloque transformador 4 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.5.` | Peso de interpolación para el bloque transformador 5 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.6.` | Peso de interpolación para el bloque transformador 6 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.7.` | Peso de interpolación para el bloque transformador 7 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.8.` | Peso de interpolación para el bloque transformador 8 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.9.` | Peso de interpolación para el bloque transformador 9 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.10.` | Peso de interpolación para el bloque transformador 10 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.11.` | Peso de interpolación para el bloque transformador 11 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.12.` | Peso de interpolación para el bloque transformador 12 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.13.` | Peso de interpolación para el bloque transformador 13 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.14.` | Peso de interpolación para el bloque transformador 14 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.15.` | Peso de interpolación para el bloque transformador 15 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.16.` | Peso de interpolación para el bloque transformador 16 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.17.` | Peso de interpolación para el bloque transformador 17 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.18.` | Peso de interpolación para el bloque transformador 18 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.19.` | Peso de interpolación para el bloque transformador 19 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.20.` | Peso de interpolación para el bloque transformador 20 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.21.` | Peso de interpolación para el bloque transformador 21 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.22.` | Peso de interpolación para el bloque transformador 22 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.23.` | Peso de interpolación para el bloque transformador 23 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.24.` | Peso de interpolación para el bloque transformador 24 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.25.` | Peso de interpolación para el bloque transformador 25 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.26.` | Peso de interpolación para el bloque transformador 26 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `transformer_blocks.27.` | Peso de interpolación para el bloque transformador 27 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `scale_shift_table` | Peso de interpolación para la tabla de desplazamiento de escala (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `proj_out.` | Peso de interpolación para capas de proyección de salida (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `model` | El modelo fusionado que combina características de ambos modelos de entrada según los pesos de interpolación especificados | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeLTXV/es.md)

---
**Source fingerprint (SHA-256):** `29ef8750b6e88f71abca10c8aaad5d75c9c32afec057af78842ca82441438922`
