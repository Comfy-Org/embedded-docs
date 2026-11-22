# TypeSafe Jev (Score)

El nodo TypeSafe Jev (Score) califica de 1 a 10 el texto, las imágenes o ambos conectados y compara la calificación con un umbral. Conecte `result` a un nodo If/Else Switch para actuar según la puntuación, o lea `score` para usar la calificación sin procesar. Este es un nodo de API: se ejecuta en los servidores de Comfy y requiere una cuenta de Comfy.org con créditos.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `model` | Modelo Jev que se utilizará. Actualmente solo hay un modelo disponible: `jev-1.14.0`. | COMBO | Sí | `"jev-1.14.0"` |
| `question` | Qué evaluar, en una escala de 1 a 10. Indique qué significan 1 y 10, como en el valor predeterminado (predeterminado: `Rate the technical quality of the image from 1 (worst) to 10 (best).`). | STRING | Sí | 1 a 1000 caracteres |
| `threshold` | `result` es verdadero cuando la puntuación es al menos este valor (predeterminado: 5.0). | FLOAT | Sí | 1.0 a 10.0 (paso 0.1) |
| `images` | Las imágenes sobre las que trata la pregunta. Hasta 32 imágenes en total; una entrada por lotes cuenta una vez por imagen. El lado largo de cada imagen se limita según el número total de imágenes: 1568 px para hasta 4 imágenes, 1024 px para hasta 8, 768 px para hasta 16 y 512 px para hasta 32, por lo que un lote más grande implica menos detalle en cada imagen. | AUTOGROW | No | 0 a 32 imágenes |
| `text` | El texto sobre el que trata la pregunta, como un prompt o una respuesta de LLM. | STRING | No | 0 a 3000 caracteres |

**Notas:**

- Conecte texto o al menos una imagen; el nodo genera un error cuando ambos están vacíos.
- La puntuación se informa de 1 a 10, y `result` es verdadero cuando es al menos `threshold`.
- La facturación se basa en tokens; el indicador de precio del nodo muestra la tarifa aproximada por 1M de tokens.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `result` | Verdadero cuando `score` es al menos `threshold`. | BOOLEAN |
| `score` | La calificación de 1 (peor) a 10 (mejor). | FLOAT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevScore/es.md)

---
**Source fingerprint (SHA-256):** `7e1970e903d2099ab3d7481a758c5291e87614b9eaf116d0ced6a1bcd36dc126`
