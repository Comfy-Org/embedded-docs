> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikaffects/es.md)

El nodo Pikaffects genera videos con varios efectos visuales aplicados a una imagen de entrada. Utiliza la API de generación de video de Pika para transformar imágenes estáticas en videos animados con efectos específicos como derretir, explotar o levitar. El nodo requiere una clave de API y un token de autenticación para acceder al servicio Pika.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `imagen` | IMAGE | Sí | - | La imagen de referencia a la que aplicar el efecto Pikaffect. |
| `pikaffect` | COMBO | Sí | "Cake-ify"<br>"Crumble"<br>"Crush"<br>"Decapitate"<br>"Deflate"<br>"Dissolve"<br>"Explode"<br>"Eye-pop"<br>"Inflate"<br>"Levitate"<br>"Melt"<br>"Peel"<br>"Poke"<br>"Squish"<br>"Ta-da"<br>"Tear" | El efecto visual específico a aplicar a la imagen (por defecto: "Cake-ify"). |
| `texto de prompt` | STRING | Sí | - | Descripción textual que guía la generación del video. |
| `prompt negativo` | STRING | Sí | - | Descripción textual de lo que se debe evitar en el video generado. |
| `semilla` | INT | Sí | 0 a 4294967295 | Valor de semilla aleatoria para resultados reproducibles. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El video generado con el efecto Pikaffect aplicado. |