> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProFirstLastFrameNode/es.md)

Este nodo utiliza el modelo de IA Kling más reciente para generar un video a partir de un fotograma inicial, un fotograma final opcional o imágenes de referencia. Puede crear un solo video o un guion gráfico de múltiples tomas con indicaciones y duraciones individuales para cada segmento. El nodo procesa estas entradas para producir un video de una longitud y resolución específicas, con generación de audio opcional.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `model_name` | COMBO | Sí | `"kling-v3-omni"`<br>`"kling-video-o1"` | El modelo específico de IA Kling a utilizar para la generación de video. |
| `prompt` | STRING | Sí | - | Una indicación de texto que describe el contenido del video. Puede incluir tanto descripciones positivas como negativas. Se ignora cuando los guiones gráficos están habilitados. |
| `duration` | INT | Sí | 3 a 15 | La duración deseada del video generado en segundos (predeterminado: 5). |
| `first_frame` | IMAGE | Sí | - | La imagen inicial para la secuencia de video. |
| `end_frame` | IMAGE | No | - | Un fotograma final opcional para el video. No se puede usar simultáneamente con `reference_images`. No funciona con guiones gráficos. |
| `reference_images` | IMAGE | No | - | Hasta 6 imágenes de referencia adicionales. |
| `resolution` | COMBO | No | `"4k"`<br>`"1080p"`<br>`"720p"` | La resolución de salida para el video generado (predeterminado: "1080p"). |
| `storyboards` | DYNAMIC_COMBO | No | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` | Genera una serie de segmentos de video con indicaciones y duraciones individuales. Solo compatible con `kling-v3-omni`. Cuando está habilitado, cada guión gráfico requiere una indicación y una duración. |
| `generar_audio` | BOOLEAN | No | True / False | Genera audio para el video (predeterminado: False). Solo compatible con `kling-v3-omni`. |
| `semilla` | INT | No | 0 a 2147483647 | La semilla controla si el nodo debe reejecutarse; los resultados no son deterministas independientemente de la semilla (predeterminado: 0). |

**Restricciones importantes:**

* La entrada `end_frame` no se puede usar al mismo tiempo que la entrada `reference_images`.
* La entrada `end_frame` no se puede usar simultáneamente con guiones gráficos.
* El modelo `kling-video-o1` no admite duraciones superiores a 10 segundos, generación de audio, resolución 4k ni guiones gráficos.
* Si no proporciona un `end_frame` ni ninguna `reference_images` con el modelo `kling-video-o1`, la `duration` solo se puede establecer en 5 o 10 segundos.
* Todas las imágenes de entrada (`first_frame`, `end_frame` y cualquier `reference_images`) deben tener una dimensión mínima de 300 píxeles tanto en ancho como en alto.
* La relación de aspecto de todas las imágenes de entrada debe estar entre 1:2.5 y 2.5:1.
* Se puede proporcionar un máximo de 6 imágenes a través de la entrada `reference_images`.
* El texto de `prompt` debe tener entre 1 y 2500 caracteres de longitud (se permiten 0 caracteres cuando los guiones gráficos están habilitados).
* Cuando los guiones gráficos están habilitados, la duración total de todos los segmentos del guión gráfico debe ser igual al valor global de `duration`.
* Cada indicación de guión gráfico debe tener entre 1 y 512 caracteres de longitud.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | VIDEO | El archivo de video generado. |

---
**Source fingerprint (SHA-256):** `bd0fb11242b7f79062079b1aa48c3524abf59ecf06a90f013e57b6910cd8e224`
