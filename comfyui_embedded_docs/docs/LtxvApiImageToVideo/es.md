> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxvApiImageToVideo/es.md)

El nodo LTXV Image To Video genera un video de calidad profesional a partir de una única imagen inicial. Utiliza una API externa para crear una secuencia de video basada en su indicación de texto, permitiéndole personalizar la duración, resolución y tasa de fotogramas.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sí | - | Primer fotograma que se utilizará para el video. |
| `model` | COMBO | Sí | `"LTX-2 (Fast)"`<br>`"LTX-2 (Quality)"` | El modelo de IA a utilizar para la generación del video. El modelo "Fast" está optimizado para velocidad, mientras que el modelo "Quality" prioriza la fidelidad visual. |
| `prompt` | STRING | Sí | - | Una descripción de texto que guía el contenido y el movimiento del video generado. |
| `duration` | COMBO | Sí | `6`<br>`8`<br>`10`<br>`12`<br>`14`<br>`16`<br>`18`<br>`20` | La duración del video en segundos (por defecto: 8). |
| `resolution` | COMBO | Sí | `"1920x1080"`<br>`"2560x1440"`<br>`"3840x2160"` | La resolución de salida del video generado. |
| `fps` | COMBO | Sí | `25`<br>`50` | Los fotogramas por segundo para el video (por defecto: 25). |
| `generate_audio` | BOOLEAN | No | - | Cuando es verdadero, el video generado incluirá audio generado por IA que coincide con la escena (por defecto: Falso). |

**Restricciones Importantes:**

* La entrada `image` debe contener exactamente una imagen.
* El `prompt` debe tener entre 1 y 10,000 caracteres de longitud.
* Si selecciona una `duration` mayor a 10 segundos, debe usar el modelo **"LTX-2 (Fast)"**, una resolución de **"1920x1080"** y **25** FPS. Esta combinación es obligatoria para videos más largos.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `video` | VIDEO | El archivo de video generado. |
