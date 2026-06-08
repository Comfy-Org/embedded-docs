El nodo de generación de texto a video Vidu Q3 crea un video a partir de una descripción textual. Utiliza el modelo Vidu Q3 Pro o Q3 Turbo para generar contenido de video basado en tu indicación, permitiéndote controlar la duración, resolución, relación de aspecto del video y si incluye audio.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | Modelo a utilizar para la generación de video. Al seleccionar un modelo, se muestran parámetros de configuración adicionales para relación de aspecto, resolución, duración y audio. | COMBO | Sí | `"viduq3-pro"`<br>`"viduq3-turbo"` |
| `model.aspect_ratio` | La relación de aspecto del video de salida. Este parámetro se muestra al seleccionar un `modelo`. | COMBO | Sí* | `"16:9"`<br>`"9:16"`<br>`"3:4"`<br>`"4:3"`<br>`"1:1"` |
| `model.resolution` | Resolución del video de salida. Este parámetro se muestra al seleccionar un `modelo`. | COMBO | Sí* | `"720p"`<br>`"1080p"` |
| `model.duration` | Duración del video de salida en segundos (predeterminado: 5). Este parámetro se muestra al seleccionar un `modelo`. | INT | Sí* | 1 a 16 |
| `model.audio` | Cuando está habilitado, genera video con sonido (incluyendo diálogos y efectos de sonido) (predeterminado: Falso). Este parámetro se muestra al seleccionar un `modelo`. | BOOLEANO | Sí* | Verdadero/Falso |
| `prompt` | Una descripción textual para la generación de video, con una longitud máxima de 2000 caracteres. | STRING | Sí | N/A |
| `semilla` | Un valor de semilla para controlar la aleatoriedad de la generación (predeterminado: 1). | INT | No | 0 a 2147483647 |

*Nota: Los parámetros `aspect_ratio`, `resolution`, `duration` y `audio` son obligatorios una vez que se selecciona un `model`, ya que forman parte de su configuración.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `video` | El archivo de video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3TextToVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `a98b6c3093d659a5a4344c2c495063acf47a7922bf7d1fc851c3b8d8c0c87c5e`
