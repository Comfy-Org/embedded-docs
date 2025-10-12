> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeFlux1/es.md)

El nodo ModelMergeFlux1 fusiona dos modelos de difusión combinando sus componentes mediante interpolación ponderada. Permite un control detallado sobre cómo se combinan las diferentes partes de los modelos, incluyendo bloques de procesamiento de imágenes, capas de incrustación temporal, mecanismos de guía, entradas vectoriales, codificadores de texto y varios bloques transformadores. Esto permite crear modelos híbridos con características personalizadas a partir de dos modelos fuente.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Sí | - | Primer modelo fuente a fusionar |
| `model2` | MODEL | Sí | - | Segundo modelo fuente a fusionar |
| `img_in.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación de entrada de imagen (por defecto: 1.0) |
| `time_in.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación de incrustación temporal (por defecto: 1.0) |
| `orientación_in` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del mecanismo de guía (por defecto: 1.0) |
| `vector_in.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación de entrada vectorial (por defecto: 1.0) |
| `txt_in.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del codificador de texto (por defecto: 1.0) |
| `double_blocks.0.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque doble 0 (por defecto: 1.0) |
| `double_blocks.1.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque doble 1 (por defecto: 1.0) |
| `double_blocks.2.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque doble 2 (por defecto: 1.0) |
| `double_blocks.3.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque doble 3 (por defecto: 1.0) |
| `double_blocks.4.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque doble 4 (por defecto: 1.0) |
| `double_blocks.5.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque doble 5 (por defecto: 1.0) |
| `double_blocks.6.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque doble 6 (por defecto: 1.0) |
| `double_blocks.7.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque doble 7 (por defecto: 1.0) |
| `double_blocks.8.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque doble 8 (por defecto: 1.0) |
| `double_blocks.9.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque doble 9 (por defecto: 1.0) |
| `double_blocks.10.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque doble 10 (por defecto: 1.0) |
| `double_blocks.11.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque doble 11 (por defecto: 1.0) |
| `double_blocks.12.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque doble 12 (por defecto: 1.0) |
| `double_blocks.13.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque doble 13 (por defecto: 1.0) |
| `double_blocks.14.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque doble 14 (por defecto: 1.0) |
| `double_blocks.15.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque doble 15 (por defecto: 1.0) |
| `double_blocks.16.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque doble 16 (por defecto: 1.0) |
| `double_blocks.17.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque doble 17 (por defecto: 1.0) |
| `double_blocks.18.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque doble 18 (por defecto: 1.0) |
| `single_blocks.0.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque simple 0 (por defecto: 1.0) |
| `single_blocks.1.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque simple 1 (por defecto: 1.0) |
| `single_blocks.2.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque simple 2 (por defecto: 1.0) |
| `single_blocks.3.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque simple 3 (por defecto: 1.0) |
| `single_blocks.4.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque simple 4 (por defecto: 1.0) |
| `single_blocks.5.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque simple 5 (por defecto: 1.0) |
| `single_blocks.6.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque simple 6 (por defecto: 1.0) |
| `single_blocks.7.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque simple 7 (por defecto: 1.0) |
| `single_blocks.8.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque simple 8 (por defecto: 1.0) |
| `single_blocks.9.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque simple 9 (por defecto: 1.0) |
| `single_blocks.10.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque simple 10 (por defecto: 1.0) |
| `single_blocks.11.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque simple 11 (por defecto: 1.0) |
| `single_blocks.12.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque simple 12 (por defecto: 1.0) |
| `single_blocks.13.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque simple 13 (por defecto: 1.0) |
| `single_blocks.14.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque simple 14 (por defecto: 1.0) |
| `single_blocks.15.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque simple 15 (por defecto: 1.0) |
| `single_blocks.16.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque simple 16 (por defecto: 1.0) |
| `single_blocks.17.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque simple 17 (por defecto: 1.0) |
| `single_blocks.18.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque simple 18 (por defecto: 1.0) |
| `single_blocks.19.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque simple 19 (por defecto: 1.0) |
| `single_blocks.20.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque simple 20 (por defecto: 1.0) |
| `single_blocks.21.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque simple 21 (por defecto: 1.0) |
| `single_blocks.22.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque simple 22 (por defecto: 1.0) |
| `single_blocks.23.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque simple 23 (por defecto: 1.0) |
| `single_blocks.24.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque simple 24 (por defecto: 1.0) |
| `single_blocks.25.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque simple 25 (por defecto: 1.0) |
| `single_blocks.26.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque simple 26 (por defecto: 1.0) |
| `single_blocks.27.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque simple 27 (por defecto: 1.0) |
| `single_blocks.28.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque simple 28 (por defecto: 1.0) |
| `single_blocks.29.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque simple 29 (por defecto: 1.0) |
| `single_blocks.30.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque simple 30 (por defecto: 1.0) |
| `single_blocks.31.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque simple 31 (por defecto: 1.0) |
| `single_blocks.32.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque simple 32 (por defecto: 1.0) |
| `single_blocks.33.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque simple 33 (por defecto: 1.0) |
| `single_blocks.34.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque simple 34 (por defecto: 1.0) |
| `single_blocks.35.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque simple 35 (por defecto: 1.0) |
| `single_blocks.36.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque simple 36 (por defecto: 1.0) |
| `single_blocks.37.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación del bloque simple 37 (por defecto: 1.0) |
| `final_layer.` | FLOAT | Sí | 0.0 a 1.0 | Peso de interpolación de la capa final (por defecto: 1.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | El modelo fusionado que combina características de ambos modelos de entrada |