## Descripción general

Este nodo genera un video con una persona u objeto basado en imágenes de referencia utilizando el modelo HappyHorse. Permite crear videos con un solo personaje o múltiples personajes interactuando entre sí.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo HappyHorse a utilizar para la generación del video. | COMBO | Sí | `"happyhorse-1.0-r2v"` |
| `prompt` | Una descripción textual del video que deseas generar. Usa identificadores como 'character1' y 'character2' para referirte a los personajes de referencia. | STRING | Sí | N/A |
| `resolution` | La resolución del video generado. | COMBO | Sí | `"720P"`<br>`"1080P"` |
| `ratio` | La relación de aspecto del video generado. | COMBO | Sí | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | La duración del video generado en segundos (predeterminado: 5). | INT | Sí | 3 a 15 |
| `reference_images` | Una o más imágenes de referencia de la persona u objeto que aparecerá en el video. Debes proporcionar al menos una imagen. | IMAGE | Sí | 1 a 9 |
| `semilla` | Un valor de semilla para generación reproducible (predeterminado: 0). La semilla puede configurarse para cambiar automáticamente después de cada generación. | INT | No | 0 a 2147483647 |
| `marca de agua` | Si se debe agregar una marca de agua de IA generada al video resultante (predeterminado: False). | BOOLEAN | No | True o False |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `VIDEO` | El archivo de video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseReferenceVideoApi/es.md)

---
**Source fingerprint (SHA-256):** `9162e150aef4cbafa42d59055bdff953e9c21b1e5fbf7c800629e570ee4cd0f9`
