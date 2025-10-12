> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeQwenImage/es.md)

El nodo ModelMergeQwenImage fusiona dos modelos de IA combinando sus componentes con pesos ajustables. Permite mezclar partes específicas de los modelos Qwen de imagen, incluyendo bloques transformadores, incrustaciones posicionales y componentes de procesamiento de texto. Puedes controlar cuánta influencia tiene cada modelo en diferentes secciones del resultado fusionado.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Sí | - | El primer modelo a fusionar (predeterminado: ninguno) |
| `model2` | MODEL | Sí | - | El segundo modelo a fusionar (predeterminado: ninguno) |
| `pos_embeds.` | FLOAT | Sí | 0.0 a 1.0 | Peso para la fusión de incrustaciones posicionales (predeterminado: 1.0) |
| `img_in.` | FLOAT | Sí | 0.0 a 1.0 | Peso para la fusión del procesamiento de entrada de imagen (predeterminado: 1.0) |
| `txt_norm.` | FLOAT | Sí | 0.0 a 1.0 | Peso para la fusión de normalización de texto (predeterminado: 1.0) |
| `txt_in.` | FLOAT | Sí | 0.0 a 1.0 | Peso para la fusión del procesamiento de entrada de texto (predeterminado: 1.0) |
| `time_text_embed.` | FLOAT | Sí | 0.0 a 1.0 | Peso para la fusión de incrustaciones de tiempo y texto (predeterminado: 1.0) |
| `transformer_blocks.0.` a `transformer_blocks.59.` | FLOAT | Sí | 0.0 a 1.0 | Peso para la fusión de cada bloque transformador (predeterminado: 1.0) |
| `proj_out.` | FLOAT | Sí | 0.0 a 1.0 | Peso para la fusión de proyección de salida (predeterminado: 1.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | El modelo fusionado que combina componentes de ambos modelos de entrada con los pesos especificados |
