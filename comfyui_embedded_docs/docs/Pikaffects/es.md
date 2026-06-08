El nodo Pikaffects genera videos con diversos efectos visuales aplicados a una imagen de entrada. Utiliza la API de generación de video de Pika para transformar imágenes estáticas en videos animados con efectos específicos como derretimiento, explosión o levitación. El nodo requiere una clave API y un token de autenticación para acceder al servicio de Pika.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `image` | La imagen de referencia a la que se aplicará el Pikaffect. | IMAGE | Sí | - |
| `pikaffect` | El efecto visual específico que se aplicará a la imagen (predeterminado: "Cake-ify"). | COMBO | Sí | "Cake-ify"<br>"Crumble"<br>"Crush"<br>"Decapitate"<br>"Deflate"<br>"Dissolve"<br>"Explode"<br>"Eye-pop"<br>"Inflate"<br>"Levitate"<br>"Melt"<br>"Peel"<br>"Poke"<br>"Squish"<br>"Ta-da"<br>"Tear" |
| `prompt_text` | Descripción textual que guía la generación del video. | STRING | Sí | - |
| `negative_prompt` | Descripción textual de lo que se debe evitar en el video generado. | STRING | Sí | - |
| `seed` | Valor de semilla aleatoria para obtener resultados reproducibles. | INT | Sí | 0 a 4294967295 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | El video generado con el Pikaffect aplicado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikaffects/es.md)

---
**Source fingerprint (SHA-256):** `68ebbee465763d463bf73678254eed38d37ebacb1c62d386bbe66961deffd5a8`
