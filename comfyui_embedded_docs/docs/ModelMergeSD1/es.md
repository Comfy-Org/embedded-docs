# ModelMergeSD1

El nodo ModelMergeSD1 permite combinar dos modelos Stable Diffusion 1.x ajustando la influencia de diferentes componentes del modelo. Proporciona control individual sobre la incrustación temporal, la incrustación de etiquetas y todos los bloques de entrada, medio y salida, permitiendo una fusión de modelos ajustada para casos de uso específicos.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model1` | Primer modelo a fusionar | MODEL | Sí | - |
| `model2` | Segundo modelo a fusionar | MODEL | Sí | - |
| `time_embed.` | Peso de mezcla de la capa de incrustación temporal (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `label_emb.` | Peso de mezcla de la capa de incrustación de etiquetas (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `input_blocks.0.` | Peso de mezcla del bloque de entrada 0 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `input_blocks.1.` | Peso de mezcla del bloque de entrada 1 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `input_blocks.2.` | Peso de mezcla del bloque de entrada 2 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `input_blocks.3.` | Peso de mezcla del bloque de entrada 3 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `input_blocks.4.` | Peso de mezcla del bloque de entrada 4 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `input_blocks.5.` | Peso de mezcla del bloque de entrada 5 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `input_blocks.6.` | Peso de mezcla del bloque de entrada 6 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `input_blocks.7.` | Peso de mezcla del bloque de entrada 7 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `input_blocks.8.` | Peso de mezcla del bloque de entrada 8 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `input_blocks.9.` | Peso de mezcla del bloque de entrada 9 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `input_blocks.10.` | Peso de mezcla del bloque de entrada 10 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `input_blocks.11.` | Peso de mezcla del bloque de entrada 11 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `middle_block.0.` | Peso de mezcla del bloque medio 0 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `middle_block.1.` | Peso de mezcla del bloque medio 1 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `middle_block.2.` | Peso de mezcla del bloque medio 2 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `output_blocks.0.` | Peso de mezcla del bloque de salida 0 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `output_blocks.1.` | Peso de mezcla del bloque de salida 1 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `output_blocks.2.` | Peso de mezcla del bloque de salida 2 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `output_blocks.3.` | Peso de mezcla del bloque de salida 3 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `output_blocks.4.` | Peso de mezcla del bloque de salida 4 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `output_blocks.5.` | Peso de mezcla del bloque de salida 5 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `output_blocks.6.` | Peso de mezcla del bloque de salida 6 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `output_blocks.7.` | Peso de mezcla del bloque de salida 7 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `output_blocks.8.` | Peso de mezcla del bloque de salida 8 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `output_blocks.9.` | Peso de mezcla del bloque de salida 9 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `output_blocks.10.` | Peso de mezcla del bloque de salida 10 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `output_blocks.11.` | Peso de mezcla del bloque de salida 11 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `out.` | Peso de mezcla de la capa de salida (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `MODEL` | El modelo fusionado que combina características de ambos modelos de entrada | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD1/es.md)

---
**Source fingerprint (SHA-256):** `512c62fb5a4e1b7f90f5ad5b80de5818659a20c8f4b024cfa33ca13b823efad8`
