# TypeSafe Jev (Pick Image)

El nodo TypeSafe Jev (Pick Image) elige una imagen de un lote. Conecta `index` a Get Image from Batch para conservar la imagen elegida, o lee `confidence` para decidir si la elección es suficientemente buena. Este es un nodo de API y requiere una cuenta de Comfy.org y una clave de API.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `model` | Modelo Jev que usar. Actualmente solo hay un modelo disponible: `jev-1.14.0`. | COMBO | Sí | `"jev-1.14.0"` |
| `question` | Qué imagen elegir. Conecta el prompt a `text` para elegir la imagen que mejor coincida con él (predeterminado: `Which image best matches the prompt in text? If there is no text, which image has the best quality?`). | STRING | Sí | 1 a 1000 caracteres |
| `images` | Las imágenes entre las que elegir. Una entrada por lotes cuenta una vez por imagen, así que cada imagen del lote es candidata. | IMAGE | Sí | 2 a 32 imágenes |
| `text` | El texto sobre el que trata la pregunta, como el prompt con el que se crearon las imágenes. | STRING | No | 0 a 3000 caracteres |

**Notas:**

- El nodo genera un error cuando se conectan menos de 2 o más de 32 imágenes.
- `index` cuenta desde 0, que es la posición que espera Get Image from Batch.
- La facturación se basa en tokens; la insignia de precio del nodo muestra la tarifa aproximada por 1 millón de tokens.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `index` | Posición de la imagen elegida en el lote, comenzando en 0. | INT |
| `confidence` | El grado de confianza de Jev, de 0 (sin un ganador claro) a 1 (con certeza). | FLOAT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevPickImage/es.md)

---
**Source fingerprint (SHA-256):** `432ee9ba69ebc0b452de4b52e94abdc56a65dc694a463a3654efb62b172c7b93`
