# TypeSafe Jev (Yes/No)

El nodo TypeSafe Jev (Yes/No) formula una pregunta de sí o no sobre el texto, las imágenes o ambos conectados, y devuelve la respuesta como un booleano. Conecte `result` a un nodo If/Else Switch para enrutar el flujo de trabajo, o lea `probability` para actuar según la seguridad del modelo. Este es un nodo de API: se ejecuta en los servidores de Comfy y requiere una cuenta de Comfy.org con créditos.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `model` | Modelo Jev que se va a usar. Actualmente solo hay un modelo disponible: `jev-1.14.0`. | COMBO | Sí | `"jev-1.14.0"` |
| `question` | La pregunta de sí o no que responden el texto y las imágenes conectados. Formúlela de modo que el «sí» sea el caso sobre el que se actúa; si hay varios sockets de imagen, use sus nombres, por ejemplo `Does image_2 show the same person as image_1?` (predeterminado: `Is there a person in the image?`). | STRING | Sí | 1 a 1000 caracteres |
| `threshold` | La respuesta es «sí» cuando la probabilidad de «sí» es al menos este valor (predeterminado: 0.5). | FLOAT | Sí | 0.01 a 0.99 (paso 0.01) |
| `images` | Las imágenes a las que se refiere la pregunta. Hasta 32 imágenes en total; una entrada por lotes cuenta una vez por imagen. El lado largo de cada imagen está limitado por el número total de imágenes: 1568 px para hasta 4 imágenes, 1024 px para hasta 8, 768 px para hasta 16 y 512 px para hasta 32, por lo que un lote más grande significa menos detalle en cada imagen. | AUTOGROW | No | 0 a 32 imágenes |
| `text` | El texto al que se refiere la pregunta, como un prompt o una respuesta de LLM. | STRING | No | 0 a 3000 caracteres |

**Notas:**

- Conecte texto o al menos una imagen; el nodo genera un error cuando ambos están vacíos.
- `result` es verdadero cuando `probability` es al menos `threshold`, y `answer` devuelve el mismo veredicto como `yes` o `no`.
- El cobro se basa en tokens; la insignia de precio del nodo muestra la tarifa aproximada por 1 millón de tokens.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `result` | La respuesta como un booleano: verdadero cuando la probabilidad de sí es al menos `threshold`. | BOOLEAN |
| `answer` | La respuesta como el texto `yes` o `no`. | STRING |
| `probability` | Probabilidad de sí, de 0 (definitivamente no) a 1 (definitivamente sí). | FLOAT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevYesNo/es.md)

---
**Source fingerprint (SHA-256):** `e8c7de5558c61e7c9058b28104a72d8d8961165983d02d63a5c9078c40855385`
