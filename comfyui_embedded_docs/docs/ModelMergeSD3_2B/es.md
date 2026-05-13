> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD3_2B/es.md)

El nodo ModelMergeSD3_2B permite fusionar dos modelos Stable Diffusion 3 2B combinando sus componentes con pesos ajustables. Proporciona control individual sobre las capas de incrustación y los bloques transformadores, permitiendo combinaciones de modelos finamente ajustadas para tareas de generación especializadas.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Sí | - | Primer modelo a fusionar |
| `model2` | MODEL | Sí | - | Segundo modelo a fusionar |
| `pos_embed.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación de incrustación de posición (predeterminado: 1.0) |
| `x_embedder.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación de incrustación de entrada (predeterminado: 1.0) |
| `context_embedder.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación de incrustación de contexto (predeterminado: 1.0) |
| `y_embedder.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación de incrustación Y (predeterminado: 1.0) |
| `t_embedder.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación de incrustación temporal (predeterminado: 1.0) |
| `joint_blocks.0.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 0 (predeterminado: 1.0) |
| `joint_blocks.1.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 1 (predeterminado: 1.0) |
| `joint_blocks.2.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 2 (predeterminado: 1.0) |
| `joint_blocks.3.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 3 (predeterminado: 1.0) |
| `joint_blocks.4.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 4 (predeterminado: 1.0) |
| `joint_blocks.5.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 5 (predeterminado: 1.0) |
| `joint_blocks.6.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 6 (predeterminado: 1.0) |
| `joint_blocks.7.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 7 (predeterminado: 1.0) |
| `joint_blocks.8.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 8 (predeterminado: 1.0) |
| `joint_blocks.9.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 9 (predeterminado: 1.0) |
| `joint_blocks.10.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 10 (predeterminado: 1.0) |
| `joint_blocks.11.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 11 (predeterminado: 1.0) |
| `joint_blocks.12.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 12 (predeterminado: 1.0) |
| `joint_blocks.13.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 13 (predeterminado: 1.0) |
| `joint_blocks.14.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 14 (predeterminado: 1.0) |
| `joint_blocks.15.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 15 (predeterminado: 1.0) |
| `joint_blocks.16.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 16 (predeterminado: 1.0) |
| `joint_blocks.17.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 17 (predeterminado: 1.0) |
| `joint_blocks.18.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 18 (predeterminado: 1.0) |
| `joint_blocks.19.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 19 (predeterminado: 1.0) |
| `joint_blocks.20.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 20 (predeterminado: 1.0) |
| `joint_blocks.21.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 21 (predeterminado: 1.0) |
| `joint_blocks.22.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 22 (predeterminado: 1.0) |
| `joint_blocks.23.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación del bloque conjunto 23 (predeterminado: 1.0) |
| `final_layer.` | FLOAT | Sí | 0.0 - 1.0 | Peso de interpolación de la capa final (predeterminado: 1.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | El modelo fusionado que combina características de ambos modelos de entrada |

---
**Source fingerprint (SHA-256):** `5b0c28c66e1828742873191be424956a9006e59ea1167a5941069ba0b7bc390b`
