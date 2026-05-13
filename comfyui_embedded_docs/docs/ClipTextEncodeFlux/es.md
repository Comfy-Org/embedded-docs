> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeFlux/es.md)

`CLIPTextEncodeFlux` es un nodo de codificación de texto avanzado diseñado para la arquitectura Flux. Procesa dos entradas de texto separadas a través de diferentes codificadores (CLIP-L y T5XXL) y las combina con una escala de guía para producir una salida de condicionamiento unificada para la generación de imágenes.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `clip` | CLIP | Sí | - | Un modelo CLIP que sea compatible con la arquitectura Flux, incluyendo ambos codificadores CLIP-L y T5XXL. |
| `clip_l` | STRING | Sí | - | Entrada de texto procesada por el codificador CLIP-L. Adecuada para descripciones concisas con palabras clave, como estilo o tema. Admite entrada multilínea y prompts dinámicos. |
| `t5xxl` | STRING | Sí | - | Entrada de texto procesada por el codificador T5XXL. Adecuada para descripciones detalladas en lenguaje natural, expresando escenas y detalles complejos. Admite entrada multilínea y prompts dinámicos. |
| `guidance` | FLOAT | Sí | 0.0 - 100.0 | Controla la influencia de las condiciones de texto en el proceso de generación. Los valores más altos implican una adherencia más estricta al texto. Valor predeterminado: 3.5. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `CONDITIONING` | CONDITIONING | Contiene las incrustaciones fusionadas de ambos codificadores y el parámetro de guía, utilizado para la generación condicional de imágenes. |

---
**Source fingerprint (SHA-256):** `f168610123410a44f9c5c5c18773603bd47bc7b44b21e65910a6026f86d7eb04`
