# ClipTextEncodeFlux

`CLIPTextEncodeFlux` es un nodo avanzado de codificación de texto diseñado para la arquitectura Flux. Procesa dos entradas de texto separadas mediante dos codificadores distintos —CLIP-L y T5XXL— y las combina con una escala de guía para producir una salida de condicionamiento unificada para la generación de imágenes.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `clip` | Un modelo CLIP compatible con la arquitectura Flux, que incluye los codificadores CLIP-L y T5XXL. | CLIP | Sí | - |
| `clip_l` | Entrada de texto procesada por el codificador CLIP-L. Adecuada para descripciones breves y concisas, como estilo o tema. Admite entrada multilínea y prompts dinámicos. | STRING | Sí | - |
| `t5xxl` | Entrada de texto procesada por el codificador T5XXL. Adecuada para descripciones detalladas en lenguaje natural, expresando escenas complejas y detalles. Admite entrada multilínea y prompts dinámicos. | STRING | Sí | - |
| `orientación` | Controla la influencia de las condiciones de texto en el proceso de generación. Los valores más altos implican una adherencia más estricta al texto. Valor predeterminado: 3,5. Ajustable en incrementos de 0,1. | FLOAT | Sí | 0.0 - 100.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `CONDITIONING` | Contiene las incrustaciones fusionadas de ambos codificadores y el parámetro de guía, utilizado para la generación condicional de imágenes. | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipTextEncodeFlux/es.md)

---
**Source fingerprint (SHA-256):** `022928fa6917102f5dc599364df9541b2451b42eb36a11813931b5fd71990b74`
