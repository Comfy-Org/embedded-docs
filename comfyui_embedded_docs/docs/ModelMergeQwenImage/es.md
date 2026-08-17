# FusionarModeloQwenImage

El nodo **ModelMergeQwenImage** fusiona dos modelos de IA combinando sus componentes con pesos ajustables. Permite mezclar partes específicas de los modelos de imagen Qwen, incluyendo bloques de transformador, incrustaciones posicionales y componentes de procesamiento de texto. Puedes controlar cuánta influencia tiene cada modelo en las diferentes secciones del resultado fusionado.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model1` | El primer modelo a fusionar (predeterminado: ninguno) | MODEL | Sí | - |
| `model2` | El segundo modelo a fusionar (predeterminado: ninguno) | MODEL | Sí | - |
| `pos_embeds.` | Peso para la mezcla de incrustaciones posicionales (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `img_in.` | Peso para la mezcla del procesamiento de entrada de imagen (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `txt_norm.` | Peso para la mezcla de la normalización de texto (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `txt_in.` | Peso para la mezcla del procesamiento de entrada de texto (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `time_text_embed.` | Peso para la mezcla de incrustaciones de tiempo y texto (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `transformer_blocks.0.` a `transformer_blocks.59.` | Peso para la mezcla de cada bloque de transformador (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `proj_out.` | Peso para la mezcla de la proyección de salida (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |

Nota: Hay 60 entradas de peso individuales para bloques de transformador (`transformer_blocks.0.` hasta `transformer_blocks.59.`), una para cada bloque de transformador en el modelo.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `model` | El modelo fusionado que combina componentes de ambos modelos de entrada con los pesos especificados | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeQwenImage/es.md)

---
**Source fingerprint (SHA-256):** `5f31f91f3d54d4c5085c684a98f64afd0a0f704693b6dd4f19bc35d3c5f74529`
