> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxvApiTextToVideo/es.md)

El nodo LTXV Text To Video genera videos de calidad profesional a partir de una descripción de texto. Se conecta a una API externa para crear videos con duración, resolución y tasa de cuadros personalizables. También puedes optar por añadir audio generado por IA al video.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Sí | `"LTX-2 (Fast)"`<br>`"LTX-2 (Quality)"`<br>`"LTX-2 (Turbo)"` | El modelo de IA que se utilizará para la generación del video. Los modelos disponibles se asignan desde el `MODELS_MAP` del código fuente. |
| `prompt` | STRING | Sí | - | La descripción de texto que la IA utilizará para generar el video. Este campo admite múltiples líneas de texto. |
| `duration` | COMBO | Sí | `6`<br>`8`<br>`10`<br>`12`<br>`14`<br>`16`<br>`18`<br>`20` | La duración del video generado en segundos (por defecto: 8). |
| `resolution` | COMBO | Sí | `"1920x1080"`<br>`"2560x1440"`<br>`"3840x2160"` | Las dimensiones en píxeles (ancho x alto) del video de salida. |
| `fps` | COMBO | Sí | `25`<br>`50` | Los cuadros por segundo para el video (por defecto: 25). |
| `generate_audio` | BOOLEAN | No | - | Cuando está habilitado, el video generado incluirá audio generado por IA que coincida con la escena (por defecto: Falso). |

**Restricciones Importantes:**

* El `prompt` debe tener entre 1 y 10,000 caracteres de longitud.
* Si seleccionas una `duration` mayor a 10 segundos, también debes usar el modelo `"LTX-2 (Fast)"`, una resolución de `"1920x1080"` y un `fps` de `25`. Esta combinación es obligatoria para videos más largos.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El archivo de video generado. |
