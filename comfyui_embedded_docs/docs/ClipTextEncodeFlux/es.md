# CodificarTextoCLIPFlux

`CLIPTextEncodeFlux` es un nodo de codificación de texto diseñado para la arquitectura Flux. Procesa dos entradas de texto separadas a través de diferentes codificadores—CLIP-L y T5XXL—y las combina con una escala de guía para producir una salida de condicionamiento unificada para la generación de imágenes.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `clip` | Un modelo CLIP que es compatible con la arquitectura Flux, incluye tanto el codificador CLIP-L como el T5XXL. | CLIP | Sí | - |
| `clip_l` | Texto de entrada procesado por el codificador CLIP-L. Adecuado para descripciones concisas con palabras clave, como estilo o tema. Admite entrada multilínea y prompts dinámicos. | STRING | Sí | - |
| `t5xxl` | Texto de entrada procesado por el codificador T5XXL. Adecuado para descripciones detalladas en lenguaje natural, que expresan escenas y detalles complejos. Admite entrada multilínea y prompts dinámicos. | STRING | Sí | - |
| `guidance` | Controla la influencia de las condiciones de texto en el proceso de generación. Los valores más altos indican una adherencia más estricta al texto. Valor predeterminado: 3.5. | FLOAT | Sí | 0.0 - 100.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `CONDITIONING` | Contiene los embeddings combinados de ambos codificadores y el valor de guía, utilizados para la generación condicional de imágenes. | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeFlux/es.md)

---
**Source fingerprint (SHA-256):** `022928fa6917102f5dc599364df9541b2451b42eb36a11813931b5fd71990b74`
