# Interpolar fotogramas

El nodo Frame Interpolate crea fotogramas nuevos entre los existentes en una secuencia de imágenes, lo que aumenta efectivamente la tasa de fotogramas. Utiliza un modelo de IA para predecir cómo deberían verse los fotogramas intermedios, lo que puede servir para crear efectos de cámara lenta suaves o para aumentar la fluidez de un vídeo. Para cada par consecutivo de fotogramas, el nodo genera `multiplier - 1` fotogramas nuevos y los inserta entre los originales.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `interp_model` | El modelo de interpolación de fotogramas que se usará para generar fotogramas intermedios (por ejemplo, modelos RIFE o FILM) | INTERP_MODEL | Sí | - |
| `images` | Un lote de imágenes consecutivas (fotogramas) entre los que interpolar. Se requieren al menos 2 imágenes; si se proporcionan menos, el nodo devuelve las imágenes de entrada sin cambios. | IMAGE | Sí | - |
| `multiplier` | El factor por el que se multiplica el número de fotogramas. Por ejemplo, un multiplicador de 2 duplica el número de fotogramas. (predeterminado: 2) | INT | Sí | 2 a 16 |

Nota: El lote de imágenes de entrada debe contener al menos 2 fotogramas, porque la interpolación se realiza entre pares consecutivos de fotogramas. El número total de fotogramas en la salida es `(number of input frames - 1) * multiplier + 1`.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `IMAGE` | Un nuevo lote de imágenes con los fotogramas interpolados insertados entre los originales, lo que da como resultado una secuencia más fluida. El número total de fotogramas de salida es `(number of input frames - 1) * multiplier + 1`. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolate/es.md)

---
**Source fingerprint (SHA-256):** `e0b9dd6ec3b09e665bcc0f95d2b7a0209d9045ba9b96828e46f126e6914f049c`
