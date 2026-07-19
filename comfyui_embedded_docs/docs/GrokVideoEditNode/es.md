# Edición de video Grok

Este nodo utiliza la API de Grok para editar un video existente basándose en un mensaje de texto. Carga tu video, envía una solicitud al modelo de IA para modificarlo según tu descripción y devuelve el video recién generado.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo de IA a utilizar para la edición de video (predeterminado: `"grok-imagine-video"`). | COMBO | Sí | `"grok-imagine-video"`<br>`"grok-imagine-video-beta"` |
| `indicación` | Descripción textual del video deseado. | STRING | Sí | N/A |
| `video` | El video de entrada que se va a editar. La duración máxima admitida es de 8.7 segundos y el tamaño máximo de archivo es de 50 MB. | VIDEO | Sí | N/A |
| `semilla` | Un valor de semilla para determinar si el nodo debe ejecutarse nuevamente. Los resultados reales son no deterministas independientemente del valor de la semilla (predeterminado: 0). | INT | No | 0 a 2147483647 |

**Restricciones:**

* El `video` de entrada debe tener una duración entre 1 y 8.7 segundos.
* El tamaño del archivo del `video` de entrada no debe superar los 50 MB.
* El `prompt` no debe estar vacío.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `video` | El video editado generado por el modelo de IA. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoEditNode/es.md)

---
**Source fingerprint (SHA-256):** `dfe52a089f7bfe7abc7f40ef113c44aef2dded828221d9d1acf0ddb6a167c33f`
