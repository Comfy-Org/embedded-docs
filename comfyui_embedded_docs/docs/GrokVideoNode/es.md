> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoNode/es.md)

El nodo Grok Video genera un video corto a partir de una descripción textual. Puede crear un video desde cero usando un prompt o animar una sola imagen de entrada basándose en un prompt. El nodo envía una solicitud a una API externa y devuelve el video generado.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `modelo` | COMBO | Sí | `"grok-imagine-video"`<br>`"grok-imagine-video-beta"` | El modelo a utilizar para la generación de video. |
| `indicación` | STRING | Sí | - | Descripción textual del video deseado. |
| `resolución` | COMBO | Sí | `"480p"`<br>`"720p"` | La resolución del video de salida. |
| `relación de aspecto` | COMBO | Sí | `"auto"`<br>`"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` | La relación de aspecto del video de salida (predeterminado: "auto"). |
| `duración` | INT | Sí | 1 a 15 | La duración del video de salida en segundos (predeterminado: 6). |
| `semilla` | INT | Sí | 0 a 2147483647 | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales son no deterministas independientemente de la semilla (predeterminado: 0). |
| `imagen` | IMAGE | No | - | Una imagen de entrada opcional para animar. |

**Nota:** Si se proporciona una `image`, solo se admite una imagen. Proporcionar múltiples imágenes causará un error. El `prompt` debe tener al menos 1 carácter después de eliminar los espacios en blanco.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El video generado. |

---
**Source fingerprint (SHA-256):** `d48049fafbe4dbf50eb5a42495d445fa4c7fc590a1d70267e220ccedc2f5328a`
