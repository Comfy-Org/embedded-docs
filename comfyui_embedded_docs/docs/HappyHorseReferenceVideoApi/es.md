> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseReferenceVideoApi/es.md)

## Descripción General

Este nodo genera un video con una persona u objeto basándose en imágenes de referencia utilizando el modelo HappyHorse. Admite la creación de videos con un solo personaje o múltiples personajes interactuando entre sí.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `model` | COMBO | Sí | `"happyhorse-1.0-r2v"` | El modelo HappyHorse a utilizar para la generación de video. |
| `prompt` | STRING | Sí | N/A | Una descripción textual del video que deseas generar. Usa identificadores como 'character1' y 'character2' para referirte a los personajes de referencia. |
| `resolution` | COMBO | Sí | `"720P"`<br>`"1080P"` | La resolución del video generado. |
| `ratio` | COMBO | Sí | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` | La relación de aspecto del video generado. |
| `duration` | INT | Sí | 3 a 15 | La duración del video generado en segundos (predeterminado: 5). |
| `reference_images` | IMAGE | Sí | 1 a 9 | Una o más imágenes de referencia de la persona u objeto que aparecerá en el video. Debes proporcionar al menos una imagen. |
| `seed` | INT | No | 0 a 2147483647 | Un valor de semilla para generación reproducible (predeterminado: 0). La semilla se puede configurar para que cambie automáticamente después de cada generación. |
| `watermark` | BOOLEAN | No | Verdadero o Falso | Si se debe agregar una marca de agua de IA al video resultante (predeterminado: Falso). |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `VIDEO` | VIDEO | El archivo de video generado. |