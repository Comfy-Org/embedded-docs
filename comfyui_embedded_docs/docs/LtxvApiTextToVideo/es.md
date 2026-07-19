# LTXV Texto a Video

El nodo LTXV Text To Video genera videos de calidad profesional a partir de una descripción textual. Se conecta a una API externa para crear videos con duración, resolución y velocidad de fotogramas personalizables. También puedes optar por que se agregue audio generado por IA al video.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo de IA a utilizar para la generación de video. Los modelos disponibles se obtienen del `MODELS_MAP` del código fuente. | COMBO | Sí | `"LTX-2 (Fast)"`<br>`"LTX-2 (Quality)"`<br>`"LTX-2 (Turbo)"` |
| `prompt` | La descripción textual que la IA utilizará para generar el video. Este campo admite múltiples líneas de texto. | STRING | Sí | - |
| `duración` | La duración del video generado en segundos (predeterminado: 8). | COMBO | Sí | `6`<br>`8`<br>`10`<br>`12`<br>`14`<br>`16`<br>`18`<br>`20` |
| `resolución` | Las dimensiones en píxeles (ancho x alto) del video de salida. | COMBO | Sí | `"1920x1080"`<br>`"2560x1440"`<br>`"3840x2160"` |
| `fps` | Los fotogramas por segundo del video (predeterminado: 25). | COMBO | Sí | `25`<br>`50` |
| `generar_audio` | Cuando está habilitado, el video generado incluirá audio creado por IA que coincida con la escena (predeterminado: False). | BOOLEAN | No | - |

**Restricciones importantes:**

* El `prompt` debe tener entre 1 y 10,000 caracteres de longitud.
* Si seleccionas una `duration` superior a 10 segundos, también debes usar el modelo `"LTX-2 (Fast)"`, una resolución de `"1920x1080"` y un `fps` de `25`. Esta combinación es necesaria para videos más largos.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `output` | El archivo de video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxvApiTextToVideo/es.md)

---
**Source fingerprint (SHA-256):** `a0c16995a07d879113bd3ca8fea64be414feee96bd8293a3e7737ede7d30e11d`
