# Kling Omni Texto a Video (Pro)

Este nodo utiliza el último modelo de Kling AI para generar un video a partir de una descripción de texto. Envía tu prompt a una API remota y devuelve el video generado. El nodo te permite controlar la duración, la forma, la calidad del video e incluso crear storyboards de múltiples tomas.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `model_name` | El modelo Kling específico a utilizar para la generación de video (predeterminado: `"kling-v3-omni"`). | COMBO | Sí | `"kling-v3-omni"`<br>`"kling-video-o1"` |
| `prompt` | Un prompt de texto que describe el contenido del video. Puede incluir descripciones tanto positivas como negativas. Se ignora cuando los storyboards están habilitados. | STRING | Sí | 0 a 2500 caracteres |
| `aspect_ratio` | La forma o dimensiones del video a generar. | COMBO | Sí | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `duration` | La duración del video en segundos (predeterminado: 5). | INT | Sí | 3 a 15 segundos |
| `resolution` | La calidad o resolución de píxeles del video (predeterminado: `"1080p"`). | COMBO | No | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `storyboards` | Genera una serie de segmentos de video con prompts y duraciones individuales. Se ignora para el modelo o1. | DYNAMIC_COMBO | No | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `generar_audio` | Si se debe generar audio para el video (predeterminado: False). | BOOLEAN | No | True / False |
| `semilla` | La semilla controla si el nodo debe volver a ejecutarse; los resultados son no deterministas independientemente de la semilla (predeterminado: 0). | INT | No | 0 a 2147483647 |

### Subentradas de Storyboard

Cuando `storyboards` se establece en un valor diferente de `"disabled"`, aparecen las siguientes entradas para cada segmento de storyboard. En los nombres de parámetros a continuación, `{i}` es el número de segmento, desde 1 hasta el número de storyboards seleccionado.

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
|-----------|-------------|--------------|-------------|-------|
| `storyboard_{i}_prompt` | Prompt para el segmento de storyboard {i}. Máximo 512 caracteres. | STRING | Sí | 1 a 512 caracteres |
| `storyboard_{i}_duration` | Duración para el segmento de storyboard {i} en segundos (predeterminado: 4). | INT | Sí | 1 a 15 segundos |

### Restricciones y limitaciones de los parámetros

- **Limitaciones específicas del modelo:**
  - El modelo `kling-video-o1` solo admite duraciones de **5 o 10 segundos**.
  - El modelo `kling-video-o1` **no** admite la generación de audio.
  - El modelo `kling-video-o1` **no** admite resolución 4k.
  - El modelo `kling-video-o1` **no** admite storyboards.
- **Restricciones de storyboard:**
  - Cuando los storyboards están habilitados, el campo `prompt` se ignora.
  - Cada storyboard requiere su propio prompt (1 a 512 caracteres) y duración.
  - La duración total de todos los storyboards debe ser exactamente igual al parámetro global `duration`.
- **Requisitos del prompt:**
  - Cuando los storyboards están **deshabilitados**, el campo `prompt` es obligatorio (mínimo 1 carácter).
  - Cuando los storyboards están **habilitados**, el campo `prompt` puede estar vacío (0 caracteres).

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
|------------------|-------------|--------------|
| `output` | El video generado a partir del prompt de texto y la configuración proporcionados. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProTextToVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `d2fbbe7c6aae283eb3fa7f73d788b809098a9a4dd6e8ada54697d43fd5bf10f2`
