> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaStartEndFrameNode2_2/es.md)

El nodo PikaFrames v2.2 genera videos combinando tu primer y último fotograma. Subes dos imágenes para definir los puntos de inicio y fin, y la IA crea una transición suave entre ellas para producir un video completo.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `imagen_inicial` | IMAGE | Sí | - | La primera imagen a combinar. |
| `imagen_final` | IMAGE | Sí | - | La última imagen a combinar. |
| `texto_de_prompt` | STRING | Sí | - | Prompt de texto que describe el contenido de video deseado. |
| `prompt_negativo` | STRING | Sí | - | Texto que describe qué evitar en el video. |
| `semilla` | INT | Sí | - | Valor de semilla aleatoria para consistencia en la generación. |
| `resolución` | STRING | Sí | - | Resolución del video de salida. |
| `duración` | INT | Sí | - | Duración del video generado. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El video generado que combina los fotogramas inicial y final con transiciones de IA. |
