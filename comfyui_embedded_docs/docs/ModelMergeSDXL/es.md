El nodo ModelMergeSDXL te permite combinar dos modelos SDXL ajustando la influencia de cada modelo en diferentes partes de la arquitectura. Puedes controlar cuánto contribuye cada modelo a las incrustaciones temporales, las incrustaciones de etiquetas y varios bloques dentro de la estructura del modelo. Esto crea un modelo híbrido que combina características de ambos modelos de entrada.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `model1` | El primer modelo SDXL a fusionar | MODEL | Sí | - |
| `model2` | El segundo modelo SDXL a fusionar | MODEL | Sí | - |
| `time_embed.` | Peso de mezcla para las capas de incrustación temporal (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `label_emb.` | Peso de mezcla para las capas de incrustación de etiquetas (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `input_blocks.0` | Peso de mezcla para el bloque de entrada 0 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `input_blocks.1` | Peso de mezcla para el bloque de entrada 1 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `input_blocks.2` | Peso de mezcla para el bloque de entrada 2 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `input_blocks.3` | Peso de mezcla para el bloque de entrada 3 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `input_blocks.4` | Peso de mezcla para el bloque de entrada 4 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `input_blocks.5` | Peso de mezcla para el bloque de entrada 5 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `input_blocks.6` | Peso de mezcla para el bloque de entrada 6 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `input_blocks.7` | Peso de mezcla para el bloque de entrada 7 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `input_blocks.8` | Peso de mezcla para el bloque de entrada 8 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `middle_block.0` | Peso de mezcla para el bloque medio 0 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `middle_block.1` | Peso de mezcla para el bloque medio 1 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `middle_block.2` | Peso de mezcla para el bloque medio 2 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `output_blocks.0` | Peso de mezcla para el bloque de salida 0 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `output_blocks.1` | Peso de mezcla para el bloque de salida 1 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `output_blocks.2` | Peso de mezcla para el bloque de salida 2 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `output_blocks.3` | Peso de mezcla para el bloque de salida 3 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `output_blocks.4` | Peso de mezcla para el bloque de salida 4 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `output_blocks.5` | Peso de mezcla para el bloque de salida 5 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `output_blocks.6` | Peso de mezcla para el bloque de salida 6 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `output_blocks.7` | Peso de mezcla para el bloque de salida 7 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `output_blocks.8` | Peso de mezcla para el bloque de salida 8 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `out.` | Peso de mezcla para las capas de salida (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `model` | El modelo SDXL fusionado que combina características de ambos modelos de entrada | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSDXL/es.md)

---
**Source fingerprint (SHA-256):** `6c7572a6ed50534f2d9ad6f499146763457da58f0c9dd4b85204e67f7d3e9660`
