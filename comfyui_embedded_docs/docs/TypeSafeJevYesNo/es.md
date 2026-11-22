# TypeSafe Jev (Yes/No)

El nodo TypeSafe Jev (Sí/No) plantea una pregunta de sí o no sobre el texto conectado, las imágenes conectadas o una combinación de ambos, y devuelve la respuesta como un booleano. Conecta `result` a un nodo If/Else Switch para enrutar el flujo de trabajo, o lee `probability` para actuar según el grado de seguridad del modelo. Este es un nodo de API y requiere una cuenta de Comfy.org y una clave de API.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `model` | Modelo Jev a usar. Actualmente solo hay un modelo disponible: `jev-1.14.0`. | COMBO | Sí | `"jev-1.14.0"` |
| `question` | La pregunta de sí o no que responden el texto y las imágenes conectados. Formúlala de modo que el sí corresponda al caso sobre el que vas a actuar; si hay varios sockets de imagen, usa sus nombres, por ejemplo, `Does image_2 show the same person as image_1?` (predeterminado: `Is there a person in the image?`). | STRING | Sí | 1 a 1000 caracteres |
| `threshold` | La respuesta es sí cuando la probabilidad de sí es al menos este valor (predeterminado: 0.5). | FLOAT | Sí | 0.01 a 0.99 (paso 0.01) |
| `images` | Las imágenes a las que se refiere la pregunta. Hasta 32 imágenes en total; una entrada por lotes cuenta una vez por cada imagen, y si hay más de 4 imágenes, se envían con un tamaño menor. | AUTOGROW | No | 0 a 32 imágenes |
| `text` | El texto al que se refiere la pregunta, como un prompt o una respuesta de LLM. | STRING | No | 0 a 3000 caracteres |

**Notas:**

- Conecta texto o al menos una imagen; el nodo genera un error cuando ambos están vacíos.
- `result` es verdadero cuando `probability` es al menos `threshold`, y `answer` devuelve el mismo veredicto que `yes` o `no`.
- La facturación se basa en tokens; la insignia de precio del nodo muestra la tarifa aproximada por 1 millón de tokens.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `result` | La respuesta como un booleano: verdadero cuando la probabilidad de sí es al menos `threshold`. | BOOLEAN |
| `answer` | La respuesta como el texto `yes` o `no`. | STRING |
| `probability` | Probabilidad de sí, de 0 (definitivamente no) a 1 (definitivamente sí). | FLOAT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevYesNo/es.md)

---
**Source fingerprint (SHA-256):** `e8c7de5558c61e7c9058b28104a72d8d8961165983d02d63a5c9078c40855385`
