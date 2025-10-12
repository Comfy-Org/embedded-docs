> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikadditions/es.md)

El nodo Pikadditions te permite agregar cualquier objeto o imagen a tu video. Subes un video y especificas lo que deseas agregar para crear un resultado perfectamente integrado. Este nodo utiliza la API de Pika para insertar imágenes en videos con una integración de aspecto natural.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | Sí | - | El video al que se agregará una imagen. |
| `imagen` | IMAGE | Sí | - | La imagen que se agregará al video. |
| `texto de indicación` | STRING | Sí | - | Descripción textual de lo que se debe agregar al video. |
| `indicación negativa` | STRING | Sí | - | Descripción textual de lo que se debe evitar en el video. |
| `semilla` | INT | Sí | 0 a 4294967295 | Valor de semilla aleatoria para resultados reproducibles. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El video procesado con la imagen insertada. |
