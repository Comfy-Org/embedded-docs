> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolate/es.md)

## Descripción general

El nodo de Interpolación de Fotogramas crea nuevos fotogramas entre los existentes en una secuencia de imágenes, aumentando efectivamente la tasa de fotogramas. Utiliza un modelo de IA para predecir cómo deberían verse los fotogramas intermedios, lo que puede usarse para crear efectos de cámara lenta suaves o para aumentar la fluidez de un video.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `interp_model` | MODEL | Sí | - | El modelo de interpolación de fotogramas a utilizar para generar fotogramas intermedios |
| `images` | IMAGE | Sí | - | Un lote de imágenes consecutivas (fotogramas) entre las que interpolar. Requiere al menos 2 imágenes. |
| `multiplier` | INT | Sí | 2 a 16 | El número de veces que se multiplicará el recuento de fotogramas. Por ejemplo, un multiplicador de 2 duplica el número de fotogramas. (predeterminado: 2) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `IMAGE` | IMAGE | Un nuevo lote de imágenes con los fotogramas interpolados insertados entre los fotogramas originales, resultando en una secuencia más fluida. El número total de fotogramas de salida es `(número de fotogramas de entrada - 1) * multiplicador + 1`. |