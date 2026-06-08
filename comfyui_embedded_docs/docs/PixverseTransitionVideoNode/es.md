Genera un video de transición entre dos imágenes de entrada utilizando la API de PixVerse. Proporcionas una imagen de inicio y una imagen de finalización, y el nodo crea un video fluido que realiza la transición de una a la otra, guiado por tu indicación de texto y la configuración seleccionada.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `primer fotograma` | Imagen de inicio para la transición del video | IMAGE | Sí | - |
| `último fotograma` | Imagen de finalización para la transición del video | IMAGE | Sí | - |
| `prompt` | Indicación para la generación del video (predeterminado: cadena vacía) | STRING | Sí | - |
| `calidad` | Configuración de calidad del video (predeterminado: `"540p"`) | COMBO | Sí | `"360p"`<br>`"540p"`<br>`"720p"`<br>`"1080p"` |
| `duración en segundos` | Duración del video en segundos | COMBO | Sí | `5`<br>`8` |
| `modo de movimiento` | Estilo de movimiento para la transición (predeterminado: `"normal"`) | COMBO | Sí | `"normal"`<br>`"fast"` |
| `semilla` | Semilla para la generación del video (predeterminado: 0) | INT | Sí | 0 a 2147483647 |
| `prompt negativo` | Una descripción textual opcional de elementos no deseados en una imagen (predeterminado: cadena vacía) | STRING | No | - |

**Nota sobre las restricciones de parámetros:** Al usar calidad 1080p, el modo de movimiento se establece automáticamente en `"normal"` y la duración se limita a 5 segundos. Para cualquier duración distinta de 5 segundos, el modo de movimiento también se establece automáticamente en `"normal"`.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | El video de transición generado | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTransitionVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `0b7f1e11d513c543df144031452bd9cd80e73c596aee8ffe9701bf471bf5983c`
