# T5TokenizerOptions

El nodo T5TokenizerOptions le permite configurar los ajustes del tokenizador para varios tipos de modelos T5. Establece los parámetros de padding mínimo y longitud mínima para múltiples variantes de modelos T5, incluyendo t5xxl, pile_t5xl, t5base, mt5xl y umt5xxl. El nodo toma una entrada CLIP y devuelve un CLIP modificado con las opciones de tokenizador especificadas aplicadas.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `clip` | El modelo CLIP para configurar las opciones del tokenizador | CLIP | Sí | - |
| `min_padding` | Valor mínimo de padding para establecer en todos los tipos de modelos T5 (predeterminado: 0) | INT | No | 0 a 10000 |
| `min_length` | Valor mínimo de longitud para establecer en todos los tipos de modelos T5 (predeterminado: 0) | INT | No | 0 a 10000 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `output` | El modelo CLIP modificado con las opciones de tokenizador actualizadas aplicadas a todas las variantes T5 | CLIP |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/T5TokenizerOptions/es.md)

---
**Source fingerprint (SHA-256):** `1c9a67781ddcc423fa3f6ed8ae1cb767a18681366aca9f1a4a6aff6b2eb38667`
