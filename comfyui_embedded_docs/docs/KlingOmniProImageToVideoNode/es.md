Este nodo utiliza el modelo Kling AI para generar un video basado en un texto descriptivo y hasta siete imágenes de referencia. Permite controlar la relación de aspecto, duración, resolución del video y, opcionalmente, usar guiones gráficos o generar audio. El nodo envía la solicitud a una API externa y devuelve el video generado.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `model_name` | El modelo Kling específico a utilizar para la generación de video (predeterminado: "kling-v3-omni"). | COMBO | Sí | `"kling-v3-omni"`<br>`"kling-video-o1"` |
| `prompt` | Un texto descriptivo que describe el contenido del video. Puede incluir descripciones tanto positivas como negativas. El texto se normaliza automáticamente y debe tener entre 1 y 2500 caracteres. Se ignora cuando los guiones gráficos están habilitados. | STRING | Sí | - |
| `aspect_ratio` | La relación de aspecto deseada para el video generado. | COMBO | Sí | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | La duración del video en segundos. El valor se puede ajustar con un control deslizante (predeterminado: 5). | INT | Sí | 3 a 15 |
| `reference_images` | Hasta 7 imágenes de referencia. Cada imagen debe tener al menos 300x300 píxeles y una relación de aspecto entre 1:2.5 y 2.5:1. | IMAGE | Sí | - |
| `resolution` | La resolución de salida del video. Este parámetro es opcional (predeterminado: "1080p"). | COMBO | No | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `storyboards` | Genera una serie de segmentos de video con indicaciones y duraciones individuales. Solo compatible con `kling-v3-omni`. Cuando está habilitado, se ignora el `prompt` global y la duración total de todos los segmentos del guión gráfico debe ser igual a la `duration` global. | DYNAMIC_COMBO | No | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `generar_audio` | Genera audio para el video. Solo compatible con `kling-v3-omni` (predeterminado: false). | BOOLEAN | No | `true`<br>`false` |
| `semilla` | La semilla controla si el nodo debe re-ejecutarse; los resultados no son deterministas independientemente de la semilla (predeterminado: 0). | INT | No | 0 a 2147483647 |

**Nota:** La entrada `reference_images` acepta un máximo de 7 imágenes. Si se proporcionan más, el nodo generará un error. Cada imagen se valida según las dimensiones mínimas y la relación de aspecto.

**Restricciones específicas del modelo:**
- `kling-video-o1` no admite duraciones mayores a 10 segundos.
- `kling-video-o1` no admite generación de audio.
- `kling-video-o1` no admite resolución 4k.
- `kling-video-o1` no admite guiones gráficos.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | El archivo de video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProImageToVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `80f4568be81b23c75bfff2bd3f21a61b242563c3c9fb1985a03e76ace24dceb2`
