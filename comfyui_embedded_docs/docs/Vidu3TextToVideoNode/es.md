# Generación de video de texto a video Vidu Q3

The Vidu Q3 Text-to-Video Generation node crea un video a partir de una descripción de texto. Utiliza el modelo Vidu Q3 Pro o Q3 Turbo para generar contenido de video basado en tu prompt, permitiéndote controlar la duración, la resolución, la relación de aspecto del video y si incluye o no audio.

## Entradas

### Entradas comunes

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model` | Modelo a utilizar para la generación de video. Al seleccionar un modelo, se muestran parámetros de configuración adicionales para la relación de aspecto, la resolución, la duración y el audio. | COMBO | Sí | `"viduq3-pro"`<br>`"viduq3-turbo"` |
| `prompt` | Una descripción textual para la generación de video, con una longitud máxima de 2000 caracteres. | STRING | Sí | N/A |
| `seed` | Un valor semilla para controlar la aleatoriedad de la generación (por defecto: 1). | INT | Sí | 0 a 2147483647 |

### Entradas de viduq3-pro y viduq3-turbo

Los siguientes parámetros de configuración son compartidos por los modelos `viduq3-pro` y `viduq3-turbo`.

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model.aspect_ratio` | La relación de aspecto del video de salida. | COMBO | Sí | `"16:9"`<br>`"9:16"`<br>`"3:4"`<br>`"4:3"`<br>`"1:1"` |
| `model.resolution` | Resolución del video de salida. | COMBO | Sí | `"720p"`<br>`"1080p"` |
| `model.duration` | Duración del video de salida en segundos (por defecto: 5). | INT | Sí | 1 a 16 |
| `model.audio` | Cuando está habilitado, produce video con sonido (incluyendo diálogos y efectos de sonido) (por defecto: False). | BOOLEAN | Sí | True/False |

**Nota:** Los parámetros `aspect_ratio`, `resolution`, `duration` y `audio` son obligatorios una vez que se selecciona un `model`, ya que forman parte de su configuración. El `prompt` no debe estar vacío y no puede superar los 2000 caracteres.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `video` | El archivo de video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3TextToVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `89c23454375a43cdfaf46c9e0e55a8a8166d02ada47ca2e237bd9f73fa4d78db`
