El nodo ByteDance Image to Video genera videos utilizando modelos de ByteDance a través de una API basada en una imagen de entrada y un texto de instrucción. Toma un fotograma inicial de imagen y crea una secuencia de video que sigue la descripción proporcionada. El nodo ofrece varias opciones de personalización para la resolución del video, relación de aspecto, duración y otros parámetros de generación.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo de ByteDance a utilizar para la generación de video (predeterminado: `"seedance-1-0-pro-fast-251015"`). | STRING | Sí | `"seedance-1-5-pro-251215"`<br>`"seedance-1-0-pro-250528"`<br>`"seedance-1-0-lite-i2v-250428"`<br>`"seedance-1-0-pro-fast-251015"` |
| `prompt` | El texto de instrucción utilizado para generar el video. Debe tener al menos 1 carácter de longitud después de eliminar espacios en blanco. | STRING | Sí | - |
| `imagen` | Primer fotograma que se utilizará para el video. Debe tener entre 300x300 y 6000x6000 píxeles, con una relación de aspecto entre 0.4 y 2.5. | IMAGE | Sí | - |
| `resolución` | La resolución del video de salida. | STRING | Sí | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `relación_de_aspecto` | La relación de aspecto del video de salida. | STRING | Sí | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |
| `duración` | La duración del video de salida en segundos (predeterminado: 5). Para el modelo `seedance-1-5-pro-251215`, la duración mínima compatible es de 4 segundos. | INT | Sí | 3 - 12 |
| `semilla` | Semilla a utilizar para la generación (predeterminado: 0). | INT | No | 0 - 2147483647 |
| `cámara_fija` | Especifica si se debe fijar la cámara. La plataforma agrega una instrucción para fijar la cámara a tu instrucción, pero no garantiza el efecto real (predeterminado: Falso). | BOOLEAN | No | - |
| `marca_de_agua` | Si se debe agregar una marca de agua "Generado por IA" al video (predeterminado: Falso). | BOOLEAN | No | - |
| `generate_audio` | Este parámetro se ignora para cualquier modelo excepto `seedance-1-5-pro-251215` (predeterminado: Falso). | BOOLEAN | No | - |

**Nota:** La instrucción no debe contener las siguientes palabras (sin distinción entre mayúsculas y minúsculas): `resolution`, `ratio`, `duration`, `seed`, `camerafixed`, `watermark`. Estos parámetros se configuran a través de sus entradas dedicadas.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | El archivo de video generado basado en la imagen de entrada y los parámetros de instrucción. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageToVideoNode/es.md)

---
**Source fingerprint (SHA-256):** `e47e14c69f4bdf4921a5a5eaec20fb775473483e80cdd9dd6700d2c7f9219e65`
