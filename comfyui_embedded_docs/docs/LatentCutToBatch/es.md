> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCutToBatch/es.md)

El nodo LatentCutToBatch toma una representación latente y la divide a lo largo de una dimensión especificada en múltiples segmentos. Estos segmentos se apilan luego en una nueva dimensión de lote, convirtiendo efectivamente una única muestra latente en un lote de muestras latentes más pequeñas. Esto es útil para procesar diferentes partes de un espacio latente de forma independiente.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `samples` | LATENT | Sí | - | La representación latente que se va a dividir y procesar por lotes. |
| `dim` | COMBO | Sí | `"t"`<br>`"x"`<br>`"y"` | La dimensión a lo largo de la cual se cortan las muestras latentes. `"t"` se refiere a la dimensión temporal, `"x"` al ancho y `"y"` a la altura. |
| `slice_size` | INT | Sí | 1 a 16384 | El tamaño de cada segmento a cortar de la dimensión especificada. Si el tamaño de la dimensión no es perfectamente divisible por este valor, el resto se descarta. (por defecto: 1) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `samples` | LATENT | El lote latente resultante, que contiene las muestras segmentadas y apiladas. |
