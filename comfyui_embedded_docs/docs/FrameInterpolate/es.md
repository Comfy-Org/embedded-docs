# Interpolar fotogramas

El nodo Frame Interpolate crea nuevos fotogramas entre los existentes en una secuencia de imágenes, aumentando efectivamente la velocidad de fotogramas. Utiliza un modelo de IA para predecir cómo deberían verse los fotogramas intermedios, lo que puede usarse para crear efectos de cámara lenta suaves o para aumentar la fluidez de un video.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `interp_model` | El modelo de interpolación de fotogramas que se usará para generar fotogramas intermedios | INTERP_MODEL | Sí | - |
| `imágenes` | Un lote de imágenes consecutivas (fotogramas) entre las que se interpolará. Se requieren al menos 2 imágenes. Si se proporcionan menos de 2 fotogramas, el nodo devuelve las imágenes de entrada sin cambios. | IMAGE | Sí | - |
| `multiplicador` | El número de veces que se multiplicará el recuento de fotogramas. Por ejemplo, un multiplicador de 2 duplica el número de fotogramas. (por defecto: 2) | INT | Sí | 2 a 16 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `IMAGE` | Un nuevo lote de imágenes con los fotogramas interpolados insertados entre los fotogramas originales, lo que da como resultado una secuencia más fluida. El número total de fotogramas de salida es `(number of input frames - 1) * multiplier + 1`. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolate/es.md)

---
**Source fingerprint (SHA-256):** `e0b9dd6ec3b09e665bcc0f95d2b7a0209d9045ba9b96828e46f126e6914f049c`
