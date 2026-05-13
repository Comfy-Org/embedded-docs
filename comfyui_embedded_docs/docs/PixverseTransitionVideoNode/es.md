> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTransitionVideoNode/es.md)

Genera un video de transición entre dos imágenes de entrada utilizando la API de PixVerse. Proporcionas una imagen de inicio y una imagen de finalización, y el nodo crea un video fluido que realiza la transición de una a la otra, guiado por tu indicación de texto y la configuración seleccionada.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `first_frame` | IMAGE | Sí | - | Imagen de inicio para la transición del video |
| `last_frame` | IMAGE | Sí | - | Imagen de finalización para la transición del video |
| `prompt` | STRING | Sí | - | Indicación para la generación del video (predeterminado: cadena vacía) |
| `quality` | COMBO | Sí | `"360p"`<br>`"540p"`<br>`"720p"`<br>`"1080p"` | Configuración de calidad del video (predeterminado: `"540p"`) |
| `duration_seconds` | COMBO | Sí | `5`<br>`8` | Duración del video en segundos |
| `motion_mode` | COMBO | Sí | `"normal"`<br>`"fast"` | Estilo de movimiento para la transición (predeterminado: `"normal"`) |
| `seed` | INT | Sí | 0 a 2147483647 | Semilla para la generación del video (predeterminado: 0) |
| `negative_prompt` | STRING | No | - | Una descripción textual opcional de elementos no deseados en una imagen (predeterminado: cadena vacía) |

**Nota sobre las restricciones de parámetros:** Al usar calidad 1080p, el modo de movimiento se establece automáticamente en `"normal"` y la duración se limita a 5 segundos. Para cualquier duración distinta de 5 segundos, el modo de movimiento también se establece automáticamente en `"normal"`.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | VIDEO | El video de transición generado |

---
**Source fingerprint (SHA-256):** `0b7f1e11d513c543df144031452bd9cd80e73c596aee8ffe9701bf471bf5983c`
