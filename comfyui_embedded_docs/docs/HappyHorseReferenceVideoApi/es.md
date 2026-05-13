> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseReferenceVideoApi/es.md)

## Descripción general

Este nodo genera un video con una persona u objeto basado en imágenes de referencia utilizando el modelo HappyHorse. Permite crear videos con un solo personaje o múltiples personajes interactuando entre sí.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| `modelo` | COMBO | Sí | `"happyhorse-1.0-r2v"` | El modelo HappyHorse a utilizar para la generación del video. |
| `prompt` | STRING | Sí | N/A | Una descripción textual del video que deseas generar. Usa identificadores como 'character1' y 'character2' para referirte a los personajes de referencia. |
| `resolution` | COMBO | Sí | `"720P"`<br>`"1080P"` | La resolución del video generado. |
| `ratio` | COMBO | Sí | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` | La relación de aspecto del video generado. |
| `duration` | INT | Sí | 3 a 15 | La duración del video generado en segundos (predeterminado: 5). |
| `reference_images` | IMAGE | Sí | 1 a 9 | Una o más imágenes de referencia de la persona u objeto que aparecerá en el video. Debes proporcionar al menos una imagen. |
| `semilla` | INT | No | 0 a 2147483647 | Un valor de semilla para generación reproducible (predeterminado: 0). La semilla puede configurarse para cambiar automáticamente después de cada generación. |
| `marca de agua` | BOOLEAN | No | True o False | Si se debe agregar una marca de agua de IA generada al video resultante (predeterminado: False). |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `VIDEO` | VIDEO | El archivo de video generado. |

---
**Source fingerprint (SHA-256):** `9162e150aef4cbafa42d59055bdff953e9c21b1e5fbf7c800629e570ee4cd0f9`
