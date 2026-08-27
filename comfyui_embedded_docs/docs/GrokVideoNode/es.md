# Video Grok

El nodo Grok Video genera un video corto a partir de una descripción de texto. Puede crear un video desde cero usando un prompt, o generar un video a partir de una única imagen de entrada. El nodo envía la solicitud a una API externa y devuelve el video generado.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `modelo` | El modelo a utilizar para la generación de video. | COMBO | Sí | `"grok-imagine-video"`<br>`"grok-imagine-video-1.5"` |
| `indicación` | Descripción de texto del video deseado. Opcional para grok-imagine-video-1.5 cuando se proporciona una imagen de entrada. | STRING | Sí | - |
| `resolución` | La resolución del video de salida. 1080p solo está disponible para grok-imagine-video-1.5. | COMBO | Sí | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `relación de aspecto` | La relación de aspecto del video de salida. | COMBO | Sí | `"auto"`<br>`"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` |
| `duración` | La duración del video de salida en segundos (predeterminado: 6). | INT | Sí | 1 a 15 |
| `semilla` | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales son no deterministas independientemente de la semilla (predeterminado: 0). | INT | Sí | 0 a 2147483647 |
| `imagen` | Imagen inicial opcional. Si se omite, el video se genera únicamente a partir del prompt de texto. | IMAGE | No | - |

**Nota:** Cuando se proporciona una `image`, solo se admite una imagen de entrada; proporcionar múltiples imágenes causará un error. El `prompt` debe ser no vacío después de eliminar espacios en blanco cuando no se proporciona una imagen, o cuando se usa `grok-imagine-video` incluso con una imagen. Para `grok-imagine-video-1.5`, el `prompt` es opcional solo cuando se proporciona una imagen de entrada. La resolución `1080p` está disponible únicamente para `grok-imagine-video-1.5`. Cuando `aspect_ratio` se establece en `"auto"`, la relación de aspecto la selecciona automáticamente el servicio.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `output` | El video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `c7d07b7bf9a776892873698abb97c7d936c7770aab397d031a287b7ecfad0b71`
