> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeHiDream/es.md)

El nodo CLIPTextEncodeHiDream procesa cuatro entradas de texto independientes utilizando diferentes modelos de lenguaje (CLIP-L, CLIP-G, T5-XXL y LLaMA) y las combina en una única salida de condicionamiento. Tokeniza cada entrada de texto con su modelo correspondiente y las codifica mediante un enfoque de codificación programada, lo que permite un condicionamiento de texto más sofisticado al aprovechar múltiples modelos de lenguaje simultáneamente.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `clip` | CLIP | Sí | - | El modelo CLIP utilizado para tokenización y codificación |
| `clip_l` | STRING | Sí | - | Entrada de texto para el procesamiento del modelo CLIP-L. Admite texto multilínea y prompts dinámicos. |
| `clip_g` | STRING | Sí | - | Entrada de texto para el procesamiento del modelo CLIP-G. Admite texto multilínea y prompts dinámicos. |
| `t5xxl` | STRING | Sí | - | Entrada de texto para el procesamiento del modelo T5-XXL. Admite texto multilínea y prompts dinámicos. |
| `llama` | STRING | Sí | - | Entrada de texto para el procesamiento del modelo LLaMA. Admite texto multilínea y prompts dinámicos. |

**Nota:** Las cuatro entradas de texto (`clip_l`, `clip_g`, `t5xxl` y `llama`) son necesarias para un funcionamiento correcto, ya que cada una contribuye a la salida final de condicionamiento mediante el proceso de codificación programada.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `CONDITIONING` | CONDITIONING | La salida de condicionamiento combinada de todas las entradas de texto procesadas, codificada mediante el método de codificación programada |

---
**Source fingerprint (SHA-256):** `51d117d82a9d833f095e874bf442d5cf8c46a12313fda6b98e628fa988797565`
