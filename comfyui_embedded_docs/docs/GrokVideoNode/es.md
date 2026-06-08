El nodo Grok Video genera un video corto a partir de una descripción textual. Puede crear un video desde cero usando un prompt o animar una sola imagen de entrada basándose en un prompt. El nodo envía una solicitud a una API externa y devuelve el video generado.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo a utilizar para la generación de video. | COMBO | Sí | `"grok-imagine-video"`<br>`"grok-imagine-video-beta"` |
| `indicación` | Descripción textual del video deseado. | STRING | Sí | - |
| `resolución` | La resolución del video de salida. | COMBO | Sí | `"480p"`<br>`"720p"` |
| `relación de aspecto` | La relación de aspecto del video de salida (predeterminado: "auto"). | COMBO | Sí | `"auto"`<br>`"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` |
| `duración` | La duración del video de salida en segundos (predeterminado: 6). | INT | Sí | 1 a 15 |
| `semilla` | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales son no deterministas independientemente de la semilla (predeterminado: 0). | INT | Sí | 0 a 2147483647 |
| `imagen` | Una imagen de entrada opcional para animar. | IMAGE | No | - |

**Nota:** Si se proporciona una `image`, solo se admite una imagen. Proporcionar múltiples imágenes causará un error. El `prompt` debe tener al menos 1 carácter después de eliminar los espacios en blanco.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | El video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `d48049fafbe4dbf50eb5a42495d445fa4c7fc590a1d70267e220ccedc2f5328a`
