# TypeSafe Jev (Pick Image)

El nodo TypeSafe Jev (Pick Image) selecciona una imagen de un lote. Conecte el mismo lote de imágenes a Get Image from Batch junto con `index` para conservar la imagen seleccionada, o lea `confidence` para decidir si la selección es suficientemente buena. Este es un nodo de API: se ejecuta en los servidores de Comfy y requiere una cuenta de Comfy.org con créditos.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `model` | Modelo de Jev a usar. Actualmente solo hay un modelo disponible: `jev-1.14.0`. | COMBO | Sí | `"jev-1.14.0"` |
| `question` | Qué imagen seleccionar. Conecte el prompt a `text` para seleccionar la imagen que mejor coincida (predeterminado: `Which image best matches the prompt in text? If there is no text, which image has the best quality?`). | STRING | Sí | 1 a 1000 caracteres |
| `images` | Las imágenes entre las que elegir. Una entrada por lotes cuenta una vez por imagen, así que cada imagen del lote es candidata. El lado largo de cada imagen se limita según el tamaño del lote antes de la carga: 1568 px para hasta 4 imágenes, 1024 px para hasta 8, 768 px para hasta 16 y 512 px para hasta 32, por lo que un lote más grande implica menos detalle en cada imagen. | IMAGE | Sí | 2 a 32 imágenes |
| `text` | El texto al que se refiere la pregunta, como el prompt a partir del cual se generaron las imágenes. | STRING | No | 0 a 3000 caracteres |

**Notas:**

- El nodo genera un error cuando se conectan menos de 2 o más de 32 imágenes.
- `index` cuenta desde 0, que es la posición que espera Get Image from Batch.
- La facturación se basa en tokens; la insignia de precio del nodo muestra la tarifa aproximada por 1 millón de tokens.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `index` | Posición de la imagen seleccionada en el lote, comenzando en 0. | INT |
| `confidence` | Qué tan seguro está Jev, de 0 (sin ganador claro) a 1 (certeza). | FLOAT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevPickImage/es.md)

---
**Source fingerprint (SHA-256):** `432ee9ba69ebc0b452de4b52e94abdc56a65dc694a463a3654efb62b172c7b93`
