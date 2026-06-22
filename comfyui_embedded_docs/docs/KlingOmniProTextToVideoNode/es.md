# Kling Omni Texto a Video (Pro)

Este nodo utiliza el modelo Kling AI más reciente para generar un video a partir de una descripción textual. Envía tu indicación a una API remota y devuelve el video generado. El nodo te permite controlar la duración, la forma, la calidad e incluso crear guiones gráficos de múltiples tomas.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `model_name` | El modelo Kling específico a utilizar para la generación de video (predeterminado: `"kling-v3-omni"`). | COMBO | Sí | `"kling-v3-omni"`<br>`"kling-video-o1"` |
| `prompt` | Una indicación de texto que describe el contenido del video. Puede incluir descripciones tanto positivas como negativas. Se ignora cuando los guiones gráficos están habilitados. | STRING | Sí | 0 a 2500 caracteres |
| `aspect_ratio` | La forma o dimensiones del video a generar. | COMBO | Sí | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | La duración del video en segundos (predeterminado: 5). | INT | Sí | 3 a 15 segundos |
| `resolution` | La calidad o resolución en píxeles del video (predeterminado: `"1080p"`). | COMBO | No | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `storyboards` | Genera una serie de segmentos de video con indicaciones y duraciones individuales. Se ignora para el modelo o1. | DYNAMIC_COMBO | No | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `generar_audio` | Si se debe generar audio para el video (predeterminado: Falso). | BOOLEAN | No | Verdadero / Falso |
| `semilla` | La semilla controla si el nodo debe reejecutarse; los resultados no son deterministas independientemente de la semilla (predeterminado: 0). | INT | No | 0 a 2147483647 |

### Restricciones y Limitaciones de los Parámetros

- **Limitaciones específicas del modelo:**
  - El modelo `kling-video-o1` solo admite duraciones de **5 o 10 segundos**.
  - El modelo `kling-video-o1` **no** admite la generación de audio.
  - El modelo `kling-video-o1` **no** admite resolución 4k.
  - El modelo `kling-video-o1` **no** admite guiones gráficos.
- **Restricciones de los guiones gráficos:**
  - Cuando los guiones gráficos están habilitados, el campo `prompt` se ignora.
  - Cada guión gráfico requiere su propia indicación (1 a 512 caracteres) y duración.
  - La duración total de todos los guiones gráficos debe ser exactamente igual al parámetro global `duration`.
- **Requisitos de la indicación:**
  - Cuando los guiones gráficos están **deshabilitados**, el campo `prompt` es obligatorio (mínimo 1 carácter).
  - Cuando los guiones gráficos están **habilitados**, el campo `prompt` puede estar vacío (0 caracteres).

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | El video generado según la indicación de texto y la configuración proporcionadas. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProTextToVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `2f867e0bd2e7b0ec901a9ad8d2adcfe712ed479c1613b80f86af3a20863e9f4c`
