> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingMotionControl/es.md)

El nodo Kling Motion Control genera un vídeo aplicando el movimiento, las expresiones y los movimientos de cámara de un vídeo de referencia a un personaje definido por una imagen de referencia y un texto descriptivo. Permite controlar si la orientación final del personaje proviene del vídeo de referencia o de la imagen de referencia.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | Sí | N/A | Una descripción textual del vídeo deseado. La longitud máxima es de 2500 caracteres. |
| `reference_image` | IMAGE | Sí | N/A | Una imagen del personaje que se va a animar. Las dimensiones mínimas son 340x340 píxeles. La relación de aspecto debe estar entre 1:2.5 y 2.5:1. |
| `reference_video` | VIDEO | Sí | N/A | Un vídeo de referencia de movimiento utilizado para dirigir el movimiento y la expresión del personaje. Las dimensiones mínimas son 340x340 píxeles, las dimensiones máximas son 3850x3850 píxeles. Los límites de duración dependen del ajuste `character_orientation`. |
| `keep_original_sound` | BOOLEAN | No | N/A | Determina si se conserva el audio original del vídeo de referencia en la salida. El valor predeterminado es `True`. |
| `character_orientation` | COMBO | No | `"video"`<br>`"image"` | Controla de dónde proviene la orientación/frente del personaje. `"video"`: los movimientos, expresiones, movimientos de cámara y la orientación siguen el vídeo de referencia de movimiento. `"image"`: los movimientos y expresiones siguen el vídeo de referencia de movimiento, pero la orientación del personaje coincide con la imagen de referencia. |
| `mode` | COMBO | No | `"pro"`<br>`"std"` | El modo de generación a utilizar. |

**Restricciones:**

* La duración del `reference_video` debe estar entre 3 y 30 segundos cuando `character_orientation` está configurado en `"video"`.
* La duración del `reference_video` debe estar entre 3 y 10 segundos cuando `character_orientation` está configurado en `"image"`.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | VIDEO | El vídeo generado con el personaje realizando el movimiento del vídeo de referencia. |
