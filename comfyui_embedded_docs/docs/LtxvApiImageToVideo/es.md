# LTXV Imagen a Video

El nodo **LTXV Image To Video** genera un video de calidad profesional a partir de una única imagen inicial. Utiliza una API externa para crear una secuencia de video basada en su prompt de texto, lo que le permite personalizar la duración, la resolución y la velocidad de fotogramas.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `image` | Primer fotograma que se utilizará para el video. | IMAGE | Sí | - |
| `model` | El modelo de IA a utilizar para la generación de video. El modelo "Pro" está optimizado para la calidad, mientras que el modelo "Fast" está optimizado para la velocidad. | COMBO | Sí | `"LTX-2 (Pro)"`<br>`"LTX-2 (Fast)"` |
| `prompt` | Una descripción de texto que guía el contenido y el movimiento del video generado. | STRING | Sí | - |
| `duration` | La duración del video en segundos (por defecto: 8). | COMBO | Sí | `6`<br>`8`<br>`10`<br>`12`<br>`14`<br>`16`<br>`18`<br>`20` |
| `resolution` | La resolución de salida del video generado. | COMBO | Sí | `"1920x1080"`<br>`"2560x1440"`<br>`"3840x2160"` |
| `fps` | Los fotogramas por segundo del video (por defecto: 25). | COMBO | Sí | `25`<br>`50` |
| `generate_audio` | Cuando sea verdadero, el video generado incluirá audio generado por IA que coincida con la escena (por defecto: Falso). | BOOLEAN | No | - |

**Restricciones importantes:**

* La entrada `image` debe contener exactamente una imagen.
* El `prompt` debe tener entre 1 y 10.000 caracteres.
* Si selecciona una `duration` mayor a 10 segundos, debe usar el modelo **"LTX-2 (Fast)"**, una resolución **"1920x1080"** y **25** FPS. Esta combinación es necesaria para videos más largos.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `video` | El archivo de video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxvApiImageToVideo/es.md)

---
**Source fingerprint (SHA-256):** `fa3928262e59105718b6ed97ddc8d2801e540b6b0c142541d92525dd75540cc7`
