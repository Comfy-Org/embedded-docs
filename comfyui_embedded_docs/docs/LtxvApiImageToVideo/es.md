# LTXV Imagen a Video

El nodo **LTXV Imagen a Video** genera un video de calidad profesional a partir de una sola imagen inicial. Utiliza una API externa para crear una secuencia de video basada en tu indicación de texto, permitiéndote personalizar la duración, resolución y velocidad de fotogramas.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `imagen` | Primer fotograma que se utilizará para el video. | IMAGE | Sí | - |
| `modelo` | El modelo de IA a utilizar para la generación del video. El modelo "Rápido" está optimizado para velocidad, mientras que el modelo "Calidad" prioriza la fidelidad visual. | COMBO | Sí | `"LTX-2 (Rápido)"`<br>`"LTX-2 (Calidad)"` |
| `prompt` | Una descripción textual que guía el contenido y el movimiento del video generado. | STRING | Sí | - |
| `duración` | La duración del video en segundos (valor predeterminado: 8). | COMBO | Sí | `6`<br>`8`<br>`10`<br>`12`<br>`14`<br>`16`<br>`18`<br>`20` |
| `resolución` | La resolución de salida del video generado. | COMBO | Sí | `"1920x1080"`<br>`"2560x1440"`<br>`"3840x2160"` |
| `fps` | Fotogramas por segundo del video (valor predeterminado: 25). | COMBO | Sí | `25`<br>`50` |
| `generar_audio` | Cuando es verdadero, el video generado incluirá audio generado por IA que coincida con la escena (valor predeterminado: Falso). | BOOLEAN | No | - |

**Restricciones importantes:**

* La entrada `image` debe contener exactamente una imagen.
* El `prompt` debe tener entre 1 y 10,000 caracteres de longitud.
* Si seleccionas una `duration` superior a 10 segundos, debes usar el modelo **"LTX-2 (Rápido)"**, una resolución **"1920x1080"** y **25** FPS. Esta combinación es necesaria para videos más largos.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `video` | El archivo de video generado. | VIDEO |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxvApiImageToVideo/es.md)

---
**Source fingerprint (SHA-256):** `af891b45997173c3210d3de4f7b6bd05b14e9d3bf8a94dcb2c1ce08038b7d99d`
