# Pikaswaps

El nodo Pika Swaps reemplaza objetos o regiones en tu video con una nueva imagen. Defines las áreas a reemplazar usando una máscara, y el nodo intercambia sin problemas el contenido especificado a lo largo de la secuencia de video.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `video` | El video en el que se intercambiará un objeto. | VIDEO | Sí | - |
| `image` | La imagen utilizada para reemplazar el objeto enmascarado en el video. | IMAGE | Sí | - |
| `mask` | Usa la máscara para definir las áreas del video a reemplazar. | MASK | Sí | - |
| `prompt_text` | Texto de indicación que describe el reemplazo deseado. | STRING | Sí | - |
| `negative_prompt` | Texto de indicación que describe lo que se debe evitar en el reemplazo. | STRING | Sí | - |
| `seed` | Valor de semilla aleatoria para obtener resultados consistentes. | INT | Sí | 0 a 4294967295 |

**Nota:** Este nodo requiere que se proporcionen todos los parámetros de entrada. Los parámetros `video`, `image` y `mask` trabajan juntos para definir la operación de reemplazo, donde la máscara especifica qué áreas del video serán reemplazadas con la imagen proporcionada.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | El video procesado con el objeto o región especificada reemplazada. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikaswaps/es.md)

---
**Source fingerprint (SHA-256):** `007b7bc429fdada2fb8910392b056ae3a98d482cce9e280bdcd162ede497eb03`
