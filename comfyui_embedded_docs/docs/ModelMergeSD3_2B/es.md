# ModelMergeSD3_2B

El nodo **ModelMergeSD3_2B** permite fusionar dos modelos Stable Diffusion 3 de 2B combinando sus componentes con pesos ajustables. Proporciona control individual sobre las capas de embedding y los bloques transformadores, lo que permite combinaciones de modelos finamente ajustadas para tareas de generación especializadas.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model1` | El primer modelo a fusionar | MODEL | Sí | - |
| `model2` | El segundo modelo a fusionar | MODEL | Sí | - |
| `pos_embed.` | Peso de interpolación del embedding de posición (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (step: 0.01) |
| `x_embedder.` | Peso de interpolación del embedding de entrada (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (step: 0.01) |
| `context_embedder.` | Peso de interpolación del embedding de contexto (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (step: 0.01) |
| `y_embedder.` | Peso de interpolación del embedding de Y (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (step: 0.01) |
| `t_embedder.` | Peso de interpolación del embedding de tiempo (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (step: 0.01) |
| `joint_blocks.0.` | Peso de interpolación del bloque conjunto 0 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (step: 0.01) |
| `joint_blocks.1.` | Peso de interpolación del bloque conjunto 1 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (step: 0.01) |
| `joint_blocks.2.` | Peso de interpolación del bloque conjunto 2 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (step: 0.01) |
| `joint_blocks.3.` | Peso de interpolación del bloque conjunto 3 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (step: 0.01) |
| `joint_blocks.4.` | Peso de interpolación del bloque conjunto 4 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (step: 0.01) |
| `joint_blocks.5.` | Peso de interpolación del bloque conjunto 5 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (step: 0.01) |
| `joint_blocks.6.` | Peso de interpolación del bloque conjunto 6 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (step: 0.01) |
| `joint_blocks.7.` | Peso de interpolación del bloque conjunto 7 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (step: 0.01) |
| `joint_blocks.8.` | Peso de interpolación del bloque conjunto 8 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (step: 0.01) |
| `joint_blocks.9.` | Peso de interpolación del bloque conjunto 9 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (step: 0.01) |
| `joint_blocks.10.` | Peso de interpolación del bloque conjunto 10 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (step: 0.01) |
| `joint_blocks.11.` | Peso de interpolación del bloque conjunto 11 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (step: 0.01) |
| `joint_blocks.12.` | Peso de interpolación del bloque conjunto 12 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (step: 0.01) |
| `joint_blocks.13.` | Peso de interpolación del bloque conjunto 13 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (step: 0.01) |
| `joint_blocks.14.` | Peso de interpolación del bloque conjunto 14 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (step: 0.01) |
| `joint_blocks.15.` | Peso de interpolación del bloque conjunto 15 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (step: 0.01) |
| `joint_blocks.16.` | Peso de interpolación del bloque conjunto 16 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (step: 0.01) |
| `joint_blocks.17.` | Peso de interpolación del bloque conjunto 17 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (step: 0.01) |
| `joint_blocks.18.` | Peso de interpolación del bloque conjunto 18 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (step: 0.01) |
| `joint_blocks.19.` | Peso de interpolación del bloque conjunto 19 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (step: 0.01) |
| `joint_blocks.20.` | Peso de interpolación del bloque conjunto 20 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (step: 0.01) |
| `joint_blocks.21.` | Peso de interpolación del bloque conjunto 21 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (step: 0.01) |
| `joint_blocks.22.` | Peso de interpolación del bloque conjunto 22 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (step: 0.01) |
| `joint_blocks.23.` | Peso de interpolación del bloque conjunto 23 (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (step: 0.01) |
| `final_layer.` | Peso de interpolación de la capa final (por defecto: 1.0) | FLOAT | Sí | 0.0 - 1.0 (step: 0.01) |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `MODEL` | El modelo fusionado que combina características de ambos modelos de entrada | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD3_2B/es.md)

---
**Source fingerprint (SHA-256):** `db27b10ade457933f6225218bb806aafcf9fc4478cac85b1623a75d110103529`
