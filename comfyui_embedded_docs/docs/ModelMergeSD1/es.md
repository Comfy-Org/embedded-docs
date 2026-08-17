# ModelMergeSD1

ModelMergeSD1 te permite fusionar dos modelos Stable Diffusion 1.x ajustando la influencia de sus componentes individuales. Proporciona un peso de combinación independiente para el embedding temporal, el embedding de etiquetas, cada bloque de entrada, cada bloque central, cada bloque de salida y la capa de salida final, lo que permite un control preciso sobre cómo se combinan los dos modelos.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model1` | El primer modelo a fusionar | MODEL | Sí | - |
| `model2` | El segundo modelo a fusionar | MODEL | Sí | - |
| `time_embed.` | Peso de combinación de la capa de embedding temporal (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `label_emb.` | Peso de combinación de la capa de embedding de etiquetas (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `input_blocks.0.` | Peso de combinación del bloque de entrada 0 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `input_blocks.1.` | Peso de combinación del bloque de entrada 1 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `input_blocks.2.` | Peso de combinación del bloque de entrada 2 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `input_blocks.3.` | Peso de combinación del bloque de entrada 3 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `input_blocks.4.` | Peso de combinación del bloque de entrada 4 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `input_blocks.5.` | Peso de combinación del bloque de entrada 5 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `input_blocks.6.` | Peso de combinación del bloque de entrada 6 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `input_blocks.7.` | Peso de combinación del bloque de entrada 7 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `input_blocks.8.` | Peso de combinación del bloque de entrada 8 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `input_blocks.9.` | Peso de combinación del bloque de entrada 9 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `input_blocks.10.` | Peso de combinación del bloque de entrada 10 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `input_blocks.11.` | Peso de combinación del bloque de entrada 11 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `middle_block.0.` | Peso de combinación del bloque central 0 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `middle_block.1.` | Peso de combinación del bloque central 1 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `middle_block.2.` | Peso de combinación del bloque central 2 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `output_blocks.0.` | Peso de combinación del bloque de salida 0 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `output_blocks.1.` | Peso de combinación del bloque de salida 1 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `output_blocks.2.` | Peso de combinación del bloque de salida 2 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `output_blocks.3.` | Peso de combinación del bloque de salida 3 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `output_blocks.4.` | Peso de combinación del bloque de salida 4 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `output_blocks.5.` | Peso de combinación del bloque de salida 5 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `output_blocks.6.` | Peso de combinación del bloque de salida 6 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `output_blocks.7.` | Peso de combinación del bloque de salida 7 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `output_blocks.8.` | Peso de combinación del bloque de salida 8 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `output_blocks.9.` | Peso de combinación del bloque de salida 9 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `output_blocks.10.` | Peso de combinación del bloque de salida 10 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `output_blocks.11.` | Peso de combinación del bloque de salida 11 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `out.` | Peso de combinación de la capa de salida (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `MODEL` | El modelo fusionado que combina características de ambos modelos de entrada | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD1/es.md)

---
**Source fingerprint (SHA-256):** `b9d53f126139412fbd8b21be72e1dcdb02736519ab4dc9e28c7840d69acb7c87`
