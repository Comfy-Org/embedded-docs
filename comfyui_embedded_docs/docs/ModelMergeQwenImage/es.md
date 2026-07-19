# FusionarModeloQwenImage

El nodo ModelMergeQwenImage fusiona dos modelos de IA combinando sus componentes con pesos ajustables. Permite mezclar partes específicas de modelos de imagen Qwen, incluyendo bloques transformadores, incrustaciones posicionales y componentes de procesamiento de texto. Puedes controlar cuánta influencia tiene cada modelo en diferentes secciones del resultado fusionado.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo1` | El primer modelo a fusionar (predeterminado: ninguno) | MODEL | Sí | - |
| `modelo2` | El segundo modelo a fusionar (predeterminado: ninguno) | MODEL | Sí | - |
| `pos_embeds.` | Peso para la mezcla de incrustaciones posicionales (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `img_in.` | Peso para la mezcla del procesamiento de entrada de imagen (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `txt_norm.` | Peso para la mezcla de normalización de texto (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `txt_in.` | Peso para la mezcla del procesamiento de entrada de texto (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `time_text_embed.` | Peso para la mezcla de incrustaciones de tiempo y texto (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `transformer_blocks.0.` a `transformer_blocks.59.` | Peso para la mezcla de cada bloque transformador (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |
| `proj_out.` | Peso para la mezcla de proyección de salida (predeterminado: 1.0) | FLOAT | Sí | 0.0 a 1.0 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `model` | El modelo fusionado que combina componentes de ambos modelos de entrada con los pesos especificados | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeQwenImage/es.md)

---
**Source fingerprint (SHA-256):** `a0424a3f4d4ffe170471ba463350d741f67ff1b1f5a8a016ad844c111033f97c`
