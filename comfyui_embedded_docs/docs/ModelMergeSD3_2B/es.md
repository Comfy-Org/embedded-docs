# ModelMergeSD3_2B

El nodo ModelMergeSD3_2B permite fusionar dos modelos Stable Diffusion 3 2B combinando sus componentes con pesos ajustables. Proporciona control individual sobre las capas de incrustación y los bloques transformadores, permitiendo combinaciones de modelos finamente ajustadas para tareas de generación especializadas.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `model1` | Primer modelo a fusionar | MODEL | Sí | - |
| `model2` | Segundo modelo a fusionar | MODEL | Sí | - |
| `pos_embed.` | Peso de interpolación de incrustación de posición (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `x_embedder.` | Peso de interpolación de incrustación de entrada (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `context_embedder.` | Peso de interpolación de incrustación de contexto (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `y_embedder.` | Peso de interpolación de incrustación Y (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `t_embedder.` | Peso de interpolación de incrustación temporal (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `joint_blocks.0.` | Peso de interpolación del bloque conjunto 0 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `joint_blocks.1.` | Peso de interpolación del bloque conjunto 1 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `joint_blocks.2.` | Peso de interpolación del bloque conjunto 2 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `joint_blocks.3.` | Peso de interpolación del bloque conjunto 3 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `joint_blocks.4.` | Peso de interpolación del bloque conjunto 4 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `joint_blocks.5.` | Peso de interpolación del bloque conjunto 5 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `joint_blocks.6.` | Peso de interpolación del bloque conjunto 6 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `joint_blocks.7.` | Peso de interpolación del bloque conjunto 7 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `joint_blocks.8.` | Peso de interpolación del bloque conjunto 8 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `joint_blocks.9.` | Peso de interpolación del bloque conjunto 9 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `joint_blocks.10.` | Peso de interpolación del bloque conjunto 10 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `joint_blocks.11.` | Peso de interpolación del bloque conjunto 11 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `joint_blocks.12.` | Peso de interpolación del bloque conjunto 12 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `joint_blocks.13.` | Peso de interpolación del bloque conjunto 13 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `joint_blocks.14.` | Peso de interpolación del bloque conjunto 14 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `joint_blocks.15.` | Peso de interpolación del bloque conjunto 15 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `joint_blocks.16.` | Peso de interpolación del bloque conjunto 16 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `joint_blocks.17.` | Peso de interpolación del bloque conjunto 17 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `joint_blocks.18.` | Peso de interpolación del bloque conjunto 18 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `joint_blocks.19.` | Peso de interpolación del bloque conjunto 19 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `joint_blocks.20.` | Peso de interpolación del bloque conjunto 20 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `joint_blocks.21.` | Peso de interpolación del bloque conjunto 21 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `joint_blocks.22.` | Peso de interpolación del bloque conjunto 22 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `joint_blocks.23.` | Peso de interpolación del bloque conjunto 23 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `final_layer.` | Peso de interpolación de la capa final (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `model` | El modelo fusionado que combina características de ambos modelos de entrada | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD3_2B/es.md)

---
**Source fingerprint (SHA-256):** `5b0c28c66e1828742873191be424956a9006e59ea1167a5941069ba0b7bc390b`
