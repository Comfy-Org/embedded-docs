# TypeSafe Jev (Choice)

El nodo TypeSafe Jev (Choice) elige una de tus propias opciones para texto, imágenes o ambos conectados. Conecta `choice` a un nodo Branch cuyas entradas lleven los nombres de las opciones, o usa `option_index` para seleccionar según la posición de la opción elegida. Un nodo Branch admite como máximo 32 entradas, por lo que una lista con más opciones que eso solo puede enrutarse mediante `option_index`. Este es un nodo de API: se ejecuta en los servidores de Comfy y requiere una cuenta de Comfy.org con créditos.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model` | Modelo Jev a usar. Actualmente solo hay un modelo disponible: `jev-1.14.0`. | COMBO | Sí | `"jev-1.14.0"` |
| `question` | La pregunta que responden las opciones. Cuando haya varios sockets de imagen, usa sus nombres, por ejemplo `Which season is shown in image_1?` (predeterminado: `What style is the image?`). | STRING | Sí | 1 a 1000 caracteres |
| `options` | Las opciones entre las que elegir, una por línea. Se eliminan los espacios en blanco iniciales y finales de cada línea, y las opciones deben ser únicas sin distinguir mayúsculas de minúsculas, por lo que se rechaza una opción repetida o dos opciones que solo difieran en mayúsculas/minúsculas. Agrega una opción como `other` para las entradas que no encajen en ninguna de ellas (predeterminado: `photo`, `illustration`, `3d render`, `anime`, `sketch` y `other`, una por línea). | STRING | Sí | 2 a 50 opciones, hasta 40 caracteres cada una |
| `images` | Las imágenes sobre las que trata la pregunta. Hasta 32 imágenes en total; una entrada por lotes cuenta una vez por cada imagen. El lado largo de cada imagen está limitado por el número total de imágenes: 1568 px para hasta 4 imágenes, 1024 px para hasta 8, 768 px para hasta 16 y 512 px para hasta 32, por lo que un lote más grande implica menos detalle en cada imagen. | AUTOGROW | No | 0 a 32 imágenes |
| `text` | El texto sobre el que trata la pregunta, como un prompt o una respuesta de LLM. | STRING | No | 0 a 3000 caracteres |

**Notas:**

- Conecta texto o al menos una imagen; el nodo genera un error cuando ambos están vacíos.
- El nodo genera un error cuando se dan menos de 2 o más de 50 opciones, cuando una opción tiene más de 40 caracteres o cuando dos opciones son iguales sin distinguir mayúsculas de minúsculas.
- `option_index` cuenta desde 0, por lo que la primera opción de la lista tiene índice 0.
- La facturación se basa en tokens; la etiqueta de precio del nodo muestra la tarifa aproximada por 1 millón de tokens.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `choice` | La opción elegida, sin espacios en blanco iniciales ni finales. Una entrada de Branch cuyo nombre conserve esos espacios no coincidirá. | STRING |
| `option_index` | Posición de la opción elegida en la lista de opciones, empezando por 0. | INT |
| `confidence` | Grado de seguridad de Jev, de 0 (sin un ganador claro) a 1 (certeza). | FLOAT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevChoice/es.md)

---
**Source fingerprint (SHA-256):** `b1cd36d600f5c07935c455d9e926e6c0a53f172fcc1a6f602c8d4dc70eeffabe`
