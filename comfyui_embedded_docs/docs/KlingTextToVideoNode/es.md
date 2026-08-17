# Kling Texto a Video

El nodo Kling de texto a video convierte indicaciones de texto en clips de video cortos mediante el servicio de generación de video de Kling. Debe proporcionar indicaciones positivas y negativas junto con ajustes como la relación de aspecto, la escala de configuración y el modo de generación, y el nodo devuelve el video generado con su identificador y duración.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Indicación de texto positiva que describe el contenido de video deseado. Entrada multilínea. No puede estar vacía. | STRING | Sí | Máximo 2500 caracteres |
| `negative_prompt` | Indicación de texto negativa que describe lo que se debe evitar en el video. Entrada multilínea. Puede dejarse vacía. | STRING | Sí | Máximo 2500 caracteres |
| `cfg_scale` | Valor de escala de configuración que controla cuán fielmente sigue el video la indicación (predeterminado: 1.0). | FLOAT | No | 0.0 a 1.0 |
| `aspect_ratio` | Configuración de relación de aspecto del video (predeterminado: "16:9"). | COMBO | No | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `mode` | La configuración a usar para la generación del video con el formato: modo / duración / nombre_modelo (predeterminado: "pro mode / 5s duration / kling-v2-5-turbo"). El modo de 5s cuesta USD 0.35, el modo de 10s cuesta USD 0.70. | COMBO | No | `"pro mode / 5s duration / kling-v2-5-turbo"`<br>`"pro mode / 10s duration / kling-v2-5-turbo"` |

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `output` | La salida de video generada. | VIDEO |
| `video_id` | Identificador único para el video generado. | STRING |
| `duration` | Información de duración para el video generado. | STRING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `6a63b0b8bc45dc5a6300cdfe7a373399eeead36de6727f7aae2c026ba0deaea8`
