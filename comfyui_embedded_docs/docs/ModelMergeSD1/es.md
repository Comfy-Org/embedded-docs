> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD1/es.md)

El nodo ModelMergeSD1 permite combinar dos modelos de Stable Diffusion 1.x ajustando la influencia de diferentes componentes del modelo. Proporciona control individual sobre la incrustación temporal, la incrustación de etiquetas y todos los bloques de entrada, intermedios y de salida, permitiendo una fusión de modelos afinada para casos de uso específicos.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Sí | - | El primer modelo a fusionar |
| `model2` | MODEL | Sí | - | El segundo modelo a fusionar |
| `time_embed.` | FLOAT | Sí | 0.0 - 1.0 | Peso de fusión de la capa de incrustación temporal (valor por defecto: 1.0) |
| `label_emb.` | FLOAT | Sí | 0.0 - 1.0 | Peso de fusión de la capa de incrustación de etiquetas (valor por defecto: 1.0) |
| `input_blocks.0.` | FLOAT | Sí | 0.0 - 1.0 | Peso de fusión del bloque de entrada 0 (valor por defecto: 1.0) |
| `input_blocks.1.` | FLOAT | Sí | 0.0 - 1.0 | Peso de fusión del bloque de entrada 1 (valor por defecto: 1.0) |
| `input_blocks.2.` | FLOAT | Sí | 0.0 - 1.0 | Peso de fusión del bloque de entrada 2 (valor por defecto: 1.0) |
| `input_blocks.3.` | FLOAT | Sí | 0.0 - 1.0 | Peso de fusión del bloque de entrada 3 (valor por defecto: 1.0) |
| `input_blocks.4.` | FLOAT | Sí | 0.0 - 1.0 | Peso de fusión del bloque de entrada 4 (valor por defecto: 1.0) |
| `input_blocks.5.` | FLOAT | Sí | 0.0 - 1.0 | Peso de fusión del bloque de entrada 5 (valor por defecto: 1.0) |
| `input_blocks.6.` | FLOAT | Sí | 0.0 - 1.0 | Peso de fusión del bloque de entrada 6 (valor por defecto: 1.0) |
| `input_blocks.7.` | FLOAT | Sí | 0.0 - 1.0 | Peso de fusión del bloque de entrada 7 (valor por defecto: 1.0) |
| `input_blocks.8.` | FLOAT | Sí | 0.0 - 1.0 | Peso de fusión del bloque de entrada 8 (valor por defecto: 1.0) |
| `input_blocks.9.` | FLOAT | Sí | 0.0 - 1.0 | Peso de fusión del bloque de entrada 9 (valor por defecto: 1.0) |
| `input_blocks.10.` | FLOAT | Sí | 0.0 - 1.0 | Peso de fusión del bloque de entrada 10 (valor por defecto: 1.0) |
| `input_blocks.11.` | FLOAT | Sí | 0.0 - 1.0 | Peso de fusión del bloque de entrada 11 (valor por defecto: 1.0) |
| `middle_block.0.` | FLOAT | Sí | 0.0 - 1.0 | Peso de fusión del bloque intermedio 0 (valor por defecto: 1.0) |
| `middle_block.1.` | FLOAT | Sí | 0.0 - 1.0 | Peso de fusión del bloque intermedio 1 (valor por defecto: 1.0) |
| `middle_block.2.` | FLOAT | Sí | 0.0 - 1.0 | Peso de fusión del bloque intermedio 2 (valor por defecto: 1.0) |
| `output_blocks.0.` | FLOAT | Sí | 0.0 - 1.0 | Peso de fusión del bloque de salida 0 (valor por defecto: 1.0) |
| `output_blocks.1.` | FLOAT | Sí | 0.0 - 1.0 | Peso de fusión del bloque de salida 1 (valor por defecto: 1.0) |
| `output_blocks.2.` | FLOAT | Sí | 0.0 - 1.0 | Peso de fusión del bloque de salida 2 (valor por defecto: 1.0) |
| `output_blocks.3.` | FLOAT | Sí | 0.0 - 1.0 | Peso de fusión del bloque de salida 3 (valor por defecto: 1.0) |
| `output_blocks.4.` | FLOAT | Sí | 0.0 - 1.0 | Peso de fusión del bloque de salida 4 (valor por defecto: 1.0) |
| `output_blocks.5.` | FLOAT | Sí | 0.0 - 1.0 | Peso de fusión del bloque de salida 5 (valor por defecto: 1.0) |
| `output_blocks.6.` | FLOAT | Sí | 0.0 - 1.0 | Peso de fusión del bloque de salida 6 (valor por defecto: 1.0) |
| `output_blocks.7.` | FLOAT | Sí | 0.0 - 1.0 | Peso de fusión del bloque de salida 7 (valor por defecto: 1.0) |
| `output_blocks.8.` | FLOAT | Sí | 0.0 - 1.0 | Peso de fusión del bloque de salida 8 (valor por defecto: 1.0) |
| `output_blocks.9.` | FLOAT | Sí | 0.0 - 1.0 | Peso de fusión del bloque de salida 9 (valor por defecto: 1.0) |
| `output_blocks.10.` | FLOAT | Sí | 0.0 - 1.0 | Peso de fusión del bloque de salida 10 (valor por defecto: 1.0) |
| `output_blocks.11.` | FLOAT | Sí | 0.0 - 1.0 | Peso de fusión del bloque de salida 11 (valor por defecto: 1.0) |
| `out.` | FLOAT | Sí | 0.0 - 1.0 | Peso de fusión de la capa de salida (valor por defecto: 1.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `MODEL` | MODEL | El modelo fusionado que combina características de ambos modelos de entrada |
