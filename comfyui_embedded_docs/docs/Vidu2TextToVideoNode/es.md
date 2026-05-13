> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2TextToVideoNode/es.md)

El nodo de Generación de Video de Texto a Video Vidu2 crea un video a partir de una descripción textual. Se conecta a una API externa para generar contenido de video basado en tu indicación, permitiéndote controlar la duración, el estilo visual y el formato del video.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|--------------|-----------|-------|-------------|
| `model` | COMBO | Sí | `"viduq2"` | El modelo de IA a utilizar para la generación de video. Actualmente, solo está disponible un modelo. |
| `prompt` | STRING | Sí | - | Una descripción textual para la generación de video, con una longitud máxima de 2000 caracteres. |
| `duration` | INT | No | 1 a 10 | La duración del video generado en segundos. El valor se puede ajustar mediante un control deslizante (predeterminado: 5). |
| `seed` | INT | No | 0 a 2147483647 | Un número utilizado para controlar la aleatoriedad de la generación, permitiendo obtener resultados reproducibles. Se puede controlar después de la generación (predeterminado: 1). |
| `aspect_ratio` | COMBO | No | `"16:9"`<br>`"9:16"`<br>`"3:4"`<br>`"4:3"`<br>`"1:1"` | La relación proporcional entre el ancho y el alto del video. |
| `resolution` | COMBO | No | `"720p"`<br>`"1080p"` | Las dimensiones en píxeles del video generado. Este es un parámetro avanzado. |
| `background_music` | BOOLEAN | No | - | Si se debe agregar música de fondo al video generado (predeterminado: Falso). Este es un parámetro avanzado. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | VIDEO | El archivo de video generado. |

---
**Source fingerprint (SHA-256):** `1e9e3629806e9b5a66d8f830d8ec33ef208a7a27b53caf43b44f7b746a85014b`
