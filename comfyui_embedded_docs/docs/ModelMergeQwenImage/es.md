# FusionarModeloQwenImage

ModelMergeQwenImage fusiona dos modelos de IA combinando sus componentes con pesos ajustables. Permite mezclar partes específicas de los modelos de imagen Qwen, incluidos bloques de transformador, incrustaciones posicionales y componentes de procesamiento de texto. Puedes controlar cuánta influencia tiene cada modelo en diferentes secciones del resultado fusionado.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo1` | El primer modelo a fusionar | MODEL | Sí | - |
| `modelo2` | El segundo modelo a fusionar | MODEL | Sí | - |
| `pos_embeds.` | Peso para la combinación de incrustaciones posicionales (por defecto: 1.0) | FLOAT | Sí | 0.0 a 1.0 (step: 0.01) |
| `img_in.` | Peso para la combinación del procesamiento de entrada de imagen (por defecto: 1.0) | FLOAT | Sí | 0.0 a 1.0 (step: 0.01) |
| `txt_norm.` | Peso para la combinación de la normalización de texto (por defecto: 1.0) | FLOAT | Sí | 0.0 a 1.0 (step: 0.01) |
| `txt_in.` | Peso para la combinación del procesamiento de entrada de texto (por defecto: 1.0) | FLOAT | Sí | 0.0 a 1.0 (step: 0.01) |
| `time_text_embed.` | Peso para la combinación de incrustaciones de tiempo y texto (por defecto: 1.0) | FLOAT | Sí | 0.0 a 1.0 (step: 0.01) |
| `transformer_blocks.0.` a `transformer_blocks.59.` | Peso para la combinación de cada bloque de transformador (por defecto: 1.0) | FLOAT | Sí | 0.0 a 1.0 (step: 0.01) |
| `proj_out.` | Peso para la combinación de la proyección de salida (por defecto: 1.0) | FLOAT | Sí | 0.0 a 1.0 (step: 0.01) |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | El modelo fusionado que combina componentes de ambos modelos de entrada con los pesos especificados | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeQwenImage/es.md)

---
**Source fingerprint (SHA-256):** `5f31f91f3d54d4c5085c684a98f64afd0a0f704693b6dd4f19bc35d3c5f74529`
