# LTXV Texto a Video

El nodo LTXV Text To Video genera videos de calidad profesional a partir de una descripción de texto. Se conecta a una API externa para crear videos con duración, resolución y tasa de fotogramas personalizables. También puede optar por añadir al video audio generado por IA.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo de IA a utilizar para la generación de video. "LTX-2 (Pro)" ofrece mayor calidad, mientras que "LTX-2 (Fast)" está optimizado para la velocidad. | COMBO | Sí | `"LTX-2 (Pro)"`<br>`"LTX-2 (Fast)"` |
| `prompt` | La descripción de texto que la IA utilizará para generar el video. Este campo admite varias líneas de texto y debe contener entre 1 y 10 000 caracteres. | STRING | Sí | - |
| `duración` | La duración del video generado en segundos (por defecto: 8). | COMBO | Sí | `6`<br>`8`<br>`10`<br>`12`<br>`14`<br>`16`<br>`18`<br>`20` |
| `resolución` | Las dimensiones en píxeles (ancho x alto) del video de salida. | COMBO | Sí | `"1920x1080"`<br>`"2560x1440"`<br>`"3840x2160"` |
| `fps` | Los fotogramas por segundo del video (por defecto: 25). | COMBO | Sí | `25`<br>`50` |
| `generar_audio` | Cuando es verdadero, el video generado incluirá audio generado por IA que coincida con la escena (por defecto: False). Esta es una configuración opcional avanzada. | BOOLEAN | No | - |

**Restricciones importantes:**

* El `prompt` debe tener entre 1 y 10 000 caracteres de longitud.
* Si selecciona una `duration` mayor de 10 segundos, también debe usar el modelo `"LTX-2 (Fast)"`, una resolución de `"1920x1080"` y un `fps` de `25`. Esta combinación es necesaria para videos más largos.

**Nota:** Este nodo está obsoleto.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `output` | El archivo de video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxvApiTextToVideo/es.md)

---
**Source fingerprint (SHA-256):** `8cf7409e46bb92abdff8a12e0d4ab49d67bb70e66c0c9074c9af99d1cf250df8`
