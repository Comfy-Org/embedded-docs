# TypeSafe Jev (Choice)

El nodo TypeSafe Jev (Choice) elige una de tus propias opciones para texto conectado, imágenes o ambos. Conecta `choice` a un nodo Branch cuyas entradas lleven los nombres de las opciones, o usa `option_index` para cambiar según la posición de la opción elegida. Este es un nodo de API y requiere una cuenta de Comfy.org y una clave de API.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `model` | Modelo Jev que se usará. Actualmente solo hay un modelo disponible: `jev-1.14.0`. | COMBO | Sí | `"jev-1.14.0"` |
| `question` | La pregunta que responden las opciones. Si hay varios sockets de imagen, usa sus nombres, por ejemplo `Which season is shown in image_1?` (predeterminado: `What style is the image?`). | STRING | Sí | 1 a 1000 caracteres |
| `options` | Las opciones entre las que elegir, una por línea. Agrega una opción como `other` para entradas que no encajen en ninguna (predeterminado: `photo`, `illustration`, `3d render`, `anime`, `sketch` y `other`, una por línea). | STRING | Sí | 2 a 50 opciones, hasta 40 caracteres cada una |
| `images` | Las imágenes sobre las que trata la pregunta. Hasta 32 imágenes en total; una entrada por lotes cuenta una vez por imagen, y más de 4 imágenes se envían con un tamaño menor. | AUTOGROW | No | 0 a 32 imágenes |
| `text` | El texto sobre el que trata la pregunta, como un prompt o una respuesta de LLM. | STRING | No | 0 a 3000 caracteres |

**Notas:**

- Conecta texto o al menos una imagen; el nodo genera un error cuando ambos están vacíos.
- El nodo genera un error cuando se proporcionan menos de 2 o más de 50 opciones, cuando una opción tiene más de 40 caracteres o cuando dos opciones difieren solo por mayúsculas y minúsculas.
- `option_index` cuenta desde 0, por lo que la primera opción de la lista tiene el índice 0.
- La facturación se basa en tokens; la insignia de precio en el nodo muestra la tarifa aproximada por 1M de tokens.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `choice` | La opción elegida, escrita exactamente como aparece en `options`. | STRING |
| `option_index` | Posición de la opción elegida en la lista de opciones, empezando en 0. | INT |
| `confidence` | Qué tan segura está Jev, de 0 (sin un ganador claro) a 1 (con certeza). | FLOAT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevChoice/es.md)

---
**Source fingerprint (SHA-256):** `b1cd36d600f5c07935c455d9e926e6c0a53f172fcc1a6f602c8d4dc70eeffabe`
