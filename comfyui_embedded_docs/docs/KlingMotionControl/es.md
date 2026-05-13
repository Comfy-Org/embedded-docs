> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingMotionControl/es.md)

El nodo Kling Motion Control genera un video aplicando el movimiento, las expresiones y los movimientos de cámara de un video de referencia a un personaje definido por una imagen de referencia y un texto descriptivo. Permite controlar si la orientación final del personaje proviene del video de referencia o de la imagen de referencia.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `prompt` | STRING | Sí | N/A | Una descripción textual del video deseado. La longitud máxima es de 2500 caracteres. |
| `imagen_referencia` | IMAGE | Sí | N/A | Una imagen del personaje a animar. Las dimensiones mínimas son 340x340 píxeles. La relación de aspecto debe estar entre 1:2.5 y 2.5:1. |
| `video_referencia` | VIDEO | Sí | N/A | Un video de referencia de movimiento utilizado para guiar el movimiento y la expresión del personaje. Las dimensiones mínimas son 340x340 píxeles, las máximas son 3850x3850 píxeles. Los límites de duración dependen de la configuración `orientación_personaje`. |
| `mantener_sonido_original` | BOOLEAN | No | N/A | Determina si se conserva el audio original del video de referencia en la salida. El valor predeterminado es `True`. |
| `orientación_personaje` | COMBO | No | `"video"`<br>`"image"` | Controla de dónde proviene la orientación/dirección del personaje. `"video"`: los movimientos, expresiones, movimientos de cámara y la orientación siguen el video de referencia de movimiento (otros detalles mediante el prompt). `"image"`: los movimientos y expresiones siguen el video de referencia de movimiento, pero la orientación del personaje coincide con la imagen de referencia (cámara/otros detalles mediante el prompt). |
| `modo` | COMBO | No | `"pro"`<br>`"std"` | El modo de generación a utilizar. |
| `modelo` | COMBO | No | `"kling-v3"`<br>`"kling-v2-6"` | La versión del modelo Kling a utilizar. El valor predeterminado es `"kling-v2-6"`. |

**Restricciones:**

* La duración de `reference_video` debe estar entre 3 y 30 segundos cuando `character_orientation` está configurado en `"video"`.
* La duración de `reference_video` debe estar entre 3 y 10 segundos cuando `character_orientation` está configurado en `"image"`.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `output` | VIDEO | El video generado con el personaje realizando el movimiento del video de referencia. |

---
**Source fingerprint (SHA-256):** `4159b10496e85ae93f522865494e9bc99ba08bda00df1601bca2314e61fb32df`
