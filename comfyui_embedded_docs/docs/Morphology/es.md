> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Morphology/es.md)

El nodo Morfología aplica diversas operaciones morfológicas a imágenes, las cuales son operaciones matemáticas utilizadas para procesar y analizar formas en imágenes. Puede realizar operaciones como erosión, dilatación, apertura, cierre y más, utilizando un tamaño de kernel personalizable para controlar la intensidad del efecto.

## Entradas

| Parámetro | Tipo de Datos | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `imagen` | IMAGE | Sí | - | La imagen de entrada a procesar |
| `operacion` | STRING | Sí | `"erode"`<br>`"dilate"`<br>`"open"`<br>`"close"`<br>`"gradient"`<br>`"bottom_hat"`<br>`"top_hat"` | La operación morfológica a aplicar |
| `tamaño_kernel` | INT | No | 3-999 | El tamaño del kernel del elemento estructurante (por defecto: 3) |

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|-------------|-----------|-------------|
| `imagen` | IMAGE | La imagen procesada después de aplicar la operación morfológica |
