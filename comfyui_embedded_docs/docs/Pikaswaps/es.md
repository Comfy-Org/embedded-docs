> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikaswaps/es.md)

El nodo Pika Swaps permite reemplazar objetos o regiones en tu video con nuevas imágenes. Puedes definir las áreas a reemplazar usando una máscara o coordenadas, y el nodo intercambiará perfectamente el contenido especificado a lo largo de la secuencia de video.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Sí | - | El video en el que se intercambiará un objeto. |
| `image` | IMAGE | Sí | - | La imagen utilizada para reemplazar el objeto enmascarado en el video. |
| `mask` | MASK | Sí | - | Usa la máscara para definir las áreas en el video que se reemplazarán. |
| `prompt_text` | STRING | Sí | - | Prompt de texto que describe el reemplazo deseado. |
| `negative_prompt` | STRING | Sí | - | Prompt de texto que describe qué evitar en el reemplazo. |
| `seed` | INT | Sí | 0 a 4294967295 | Valor de semilla aleatoria para resultados consistentes. |

**Nota:** Este nodo requiere que se proporcionen todos los parámetros de entrada. El `video`, `image` y `mask` trabajan juntos para definir la operación de reemplazo, donde la máscara especifica qué áreas del video se reemplazarán con la imagen proporcionada.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El video procesado con el objeto o región especificada reemplazada. |