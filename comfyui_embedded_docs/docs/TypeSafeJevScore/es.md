# TypeSafe Jev (Score)

El nodo TypeSafe Jev (Score) califica el texto, las imágenes o ambos conectados de 1 a 10 y compara la calificación con un umbral. Conecte `result` a un nodo If/Else Switch para actuar según la puntuación, o lea `score` para usar la calificación sin procesar. Este es un nodo de API y requiere una cuenta de Comfy.org y una clave de API.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `model` | Modelo Jev a usar. Actualmente solo hay un modelo disponible: `jev-1.14.0`. | COMBO | Sí | `"jev-1.14.0"` |
| `question` | Qué calificar, en una escala de 1 a 10. Indique qué significan 1 y 10, como en el valor predeterminado (predeterminado: `Rate the technical quality of the image from 1 (worst) to 10 (best).`). | STRING | Sí | 1 a 1000 caracteres |
| `threshold` | `result` es verdadero cuando la puntuación es al menos este valor (predeterminado: 5.0). | FLOAT | Sí | 1.0 a 10.0 (paso 0.1) |
| `images` | Las imágenes a las que se refiere la pregunta. Hasta 32 imágenes en total; una entrada por lotes cuenta una vez por imagen, y más de 4 imágenes se envían con un tamaño más pequeño. | AUTOGROW | No | 0 a 32 imágenes |
| `text` | El texto al que se refiere la pregunta, como un prompt o una respuesta de un LLM. | STRING | No | 0 a 3000 caracteres |

**Notas:**

- Conecte texto o al menos una imagen; el nodo genera un error cuando ambos están vacíos.
- La puntuación se informa de 1 a 10, y `result` es verdadero cuando es al menos `threshold`.
- La facturación se basa en tokens; la insignia de precio del nodo muestra la tarifa aproximada por 1 millón de tokens.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `result` | Verdadero cuando `score` es al menos `threshold`. | BOOLEAN |
| `score` | La calificación de 1 (peor) a 10 (mejor). | FLOAT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevScore/es.md)

---
**Source fingerprint (SHA-256):** `7e1970e903d2099ab3d7481a758c5291e87614b9eaf116d0ced6a1bcd36dc126`
