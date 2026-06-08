El nodo T5TokenizerOptions permite configurar ajustes del tokenizador para varios tipos de modelos T5. Establece el relleno mínimo y la longitud mínima para múltiples variantes del modelo T5, incluyendo t5xxl, pile_t5xl, t5base, mt5xl y umt5xxl. El nodo recibe una entrada CLIP y devuelve un CLIP modificado con las opciones de tokenizador especificadas aplicadas.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `clip` | El modelo CLIP para configurar las opciones del tokenizador | CLIP | Sí | - |
| `mín_relleno` | Valor de relleno mínimo para establecer en todos los tipos de modelo T5 (predeterminado: 0) | INT | No | 0 a 10000 |
| `mín_longitud` | Valor de longitud mínima para establecer en todos los tipos de modelo T5 (predeterminado: 0) | INT | No | 0 a 10000 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | El modelo CLIP modificado con las opciones de tokenizador actualizadas aplicadas a todas las variantes T5 | CLIP |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/T5TokenizerOptions/es.md)

---
**Source fingerprint (SHA-256):** `bc05c714e4006786d0c948ed1de05324257472337397b0aa4ce574d7483929ff`
