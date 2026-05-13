> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikaswaps/es.md)

El nodo Pika Swaps reemplaza objetos o regiones en tu video con una nueva imagen. Defines las áreas a reemplazar usando una máscara, y el nodo intercambia sin problemas el contenido especificado a lo largo de la secuencia de video.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `video` | VIDEO | Sí | - | El video en el que se intercambiará un objeto. |
| `image` | IMAGE | Sí | - | La imagen utilizada para reemplazar el objeto enmascarado en el video. |
| `mask` | MASK | Sí | - | Usa la máscara para definir las áreas del video a reemplazar. |
| `prompt_text` | STRING | Sí | - | Texto de indicación que describe el reemplazo deseado. |
| `negative_prompt` | STRING | Sí | - | Texto de indicación que describe lo que se debe evitar en el reemplazo. |
| `seed` | INT | Sí | 0 a 4294967295 | Valor de semilla aleatoria para obtener resultados consistentes. |

**Nota:** Este nodo requiere que se proporcionen todos los parámetros de entrada. Los parámetros `video`, `image` y `mask` trabajan juntos para definir la operación de reemplazo, donde la máscara especifica qué áreas del video serán reemplazadas con la imagen proporcionada.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | VIDEO | El video procesado con el objeto o región especificada reemplazada. |

---
**Source fingerprint (SHA-256):** `007b7bc429fdada2fb8910392b056ae3a98d482cce9e280bdcd162ede497eb03`
