> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeHiDream/es.md)

El nodo CLIPTextEncodeHiDream procesa múltiples entradas de texto utilizando diferentes modelos de lenguaje y las combina en una única salida de condicionamiento. Tokeniza texto de cuatro fuentes diferentes (CLIP-L, CLIP-G, T5-XXL y LLaMA) y los codifica utilizando un enfoque de codificación programada. Esto permite un condicionamiento de texto más sofisticado aprovechando múltiples modelos de lenguaje simultáneamente.

## Entradas

| Parámetro | Tipo de Dato | Tipo de Entrada | Por Defecto | Rango | Descripción |
|-----------|-----------|------------|---------|-------|-------------|
| `clip` | CLIP | Entrada Requerida | - | - | El modelo CLIP utilizado para la tokenización y codificación |
| `clip_l` | STRING | Texto Multilínea | - | - | Entrada de texto para el procesamiento del modelo CLIP-L |
| `clip_g` | STRING | Texto Multilínea | - | - | Entrada de texto para el procesamiento del modelo CLIP-G |
| `t5xxl` | STRING | Texto Multilínea | - | - | Entrada de texto para el procesamiento del modelo T5-XXL |
| `llama` | STRING | Texto Multilínea | - | - | Entrada de texto para el procesamiento del modelo LLaMA |

**Nota:** Todas las entradas de texto admiten prompts dinámicos y entrada de texto multilínea. El nodo requiere que se proporcionen los cuatro parámetros de texto para un funcionamiento adecuado, ya que cada uno contribuye a la salida de condicionamiento final a través del proceso de codificación programada.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | La salida de condicionamiento combinada de todas las entradas de texto procesadas |