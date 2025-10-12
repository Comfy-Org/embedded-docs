> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD3_2B/es.md)

El nodo ModelMergeSD3_2B permite fusionar dos modelos Stable Diffusion 3 2B mediante la combinación de sus componentes con pesos ajustables. Proporciona control individual sobre las capas de embedding y los bloques transformadores, permitiendo combinaciones de modelos afinadas para tareas de generación especializadas.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Sí | - | El primer modelo a fusionar |
| `model2` | MODEL | Sí | - | El segundo modelo a fusionar |
| `pos_embed.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del embedding de posición (valor por defecto: 1.0) |
| `x_embedder.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del embedding de entrada (valor por defecto: 1.0) |
| `context_embedder.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del embedding de contexto (valor por defecto: 1.0) |
| `y_embedder.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del embedding Y (valor por defecto: 1.0) |
| `t_embedder.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del embedding de tiempo (valor por defecto: 1.0) |
| `joint_blocks.0.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 0 (valor por defecto: 1.0) |
| `joint_blocks.1.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 1 (valor por defecto: 1.0) |
| `joint_blocks.2.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 2 (valor por defecto: 1.0) |
| `joint_blocks.3.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 3 (valor por defecto: 1.0) |
| `joint_blocks.4.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 4 (valor por defecto: 1.0) |
| `joint_blocks.5.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 5 (valor por defecto: 1.0) |
| `joint_blocks.6.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 6 (valor por defecto: 1.0) |
| `joint_blocks.7.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 7 (valor por defecto: 1.0) |
| `joint_blocks.8.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 8 (valor por defecto: 1.0) |
| `joint_blocks.9.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 9 (valor por defecto: 1.0) |
| `joint_blocks.10.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 10 (valor por defecto: 1.0) |
| `joint_blocks.11.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 11 (valor por defecto: 1.0) |
| `joint_blocks.12.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 12 (valor por defecto: 1.0) |
| `joint_blocks.13.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 13 (valor por defecto: 1.0) |
| `joint_blocks.14.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 14 (valor por defecto: 1.0) |
| `joint_blocks.15.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 15 (valor por defecto: 1.0) |
| `joint_blocks.16.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 16 (valor por defecto: 1.0) |
| `joint_blocks.17.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 17 (valor por defecto: 1.0) |
| `joint_blocks.18.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 18 (valor por defecto: 1.0) |
| `joint_blocks.19.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 19 (valor por defecto: 1.0) |
| `joint_blocks.20.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 20 (valor por defecto: 1.0) |
| `joint_blocks.21.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 21 (valor por defecto: 1.0) |
| `joint_blocks.22.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 22 (valor por defecto: 1.0) |
| `joint_blocks.23.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 23 (valor por defecto: 1.0) |
| `final_layer.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación de la capa final (valor por defecto: 1.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | El modelo fusionado que combina características de ambos modelos de entrada |
