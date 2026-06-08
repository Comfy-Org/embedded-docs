## Descripción general

El nodo de Interpolación de Fotogramas crea nuevos fotogramas entre los existentes en una secuencia de imágenes, aumentando efectivamente la frecuencia de fotogramas. Utiliza un modelo de IA para predecir cómo deberían verse los fotogramas intermedios, lo que puede emplearse para crear efectos de cámara lenta suaves o para aumentar la fluidez de un video.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `interp_model` | El modelo de interpolación de fotogramas a utilizar para generar los fotogramas intermedios | MODEL | Sí | - |
| `imágenes` | Un lote de imágenes consecutivas (fotogramas) entre las que interpolar. Requiere al menos 2 imágenes. | IMAGE | Sí | - |
| `multiplicador` | El número de veces que se multiplicará el recuento de fotogramas. Por ejemplo, un multiplicador de 2 duplica el número de fotogramas. (predeterminado: 2) | INT | Sí | 2 a 16 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `IMAGE` | Un nuevo lote de imágenes con los fotogramas interpolados insertados entre los fotogramas originales, lo que resulta en una secuencia más fluida. El número total de fotogramas de salida es `(número de fotogramas de entrada - 1) * multiplicador + 1`. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolate/es.md)

---
**Source fingerprint (SHA-256):** `05fdac188d9d7c7d5cac9ade55ba22cc743395b3c659a519ca03fe293b9a6e34`
