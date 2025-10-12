> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCut/es.md)

El nodo LatentCut extrae una sección específica de muestras latentes a lo largo de una dimensión elegida. Permite recortar una porción de la representación latente especificando la dimensión (x, y o t), la posición inicial y la cantidad a extraer. El nodo maneja tanto indexación positiva como negativa y ajusta automáticamente la cantidad de extracción para mantenerse dentro de los límites disponibles.

## Entradas

| Parámetro | Tipo de Datos | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `samples` | LATENT | Sí | - | Las muestras latentes de entrada desde las cuales extraer |
| `dim` | COMBO | Sí | "x"<br>"y"<br>"t" | La dimensión a lo largo de la cual cortar las muestras latentes |
| `index` | INT | No | -16384 a 16384 | La posición inicial para el corte (por defecto: 0). Los valores positivos cuentan desde el inicio, los valores negativos cuentan desde el final |
| `amount` | INT | No | 1 a 16384 | El número de elementos a extraer a lo largo de la dimensión especificada (por defecto: 1) |

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|-------------|-----------|-------------|
| `output` | LATENT | La porción extraída de las muestras latentes |
