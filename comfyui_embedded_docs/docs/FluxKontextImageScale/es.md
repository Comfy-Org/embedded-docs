Este nodo escala la imagen de entrada a un tamaño óptimo utilizado durante el entrenamiento del modelo Flux Kontext utilizando el algoritmo Lanczos, basándose en la relación de aspecto de la imagen de entrada. Este nodo es particularmente útil cuando se introducen imágenes de gran tamaño, ya que las entradas de tamaño excesivo pueden provocar una degradación de la calidad de salida del modelo o problemas como la aparición de múltiples sujetos en la salida.

## Entradas

| Nombre del Parámetro | Tipo de Datos | Tipo de Entrada | Valor Predeterminado | Rango de Valores | Descripción |
|---------------------|----------------|------------------|---------------------|------------------|-------------|
| `image` | IMAGE | Requerido | - | - | Imagen de entrada a redimensionar |

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|------------------|---------------|-------------|
| `image` | IMAGE | Imagen redimensionada |

## Lista de Tamaños Preestablecidos

La siguiente es una lista de tamaños estándar utilizados durante el entrenamiento del modelo. El nodo seleccionará el tamaño más cercano a la relación de aspecto de la imagen de entrada:

| Ancho | Alto | Relación de Aspecto |
|-------|------|---------------------|
| 672   | 1568 | 0.429              |
| 688   | 1504 | 0.457              |
| 720   | 1456 | 0.494              |
| 752   | 1392 | 0.540              |
| 800   | 1328 | 0.603              |
| 832   | 1248 | 0.667              |
| 880   | 1184 | 0.743              |
| 944   | 1104 | 0.855              |
| 1024  | 1024 | 1.000              |
| 1104  | 944  | 1.170              |
| 1184  | 880  | 1.345              |
| 1248  | 832  | 1.500              |
| 1328  | 800  | 1.660              |
| 1392  | 752  | 1.851              |
| 1456  | 720  | 2.022              |
| 1504  | 688  | 2.186              |
| 1568  | 672  | 2.333              |
