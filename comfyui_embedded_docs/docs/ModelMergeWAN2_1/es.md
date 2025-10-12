> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeWAN2_1/es.md)

El nodo ModelMergeWAN2_1 fusiona dos modelos combinando sus componentes mediante promedios ponderados. Soporta diferentes tamaños de modelos, incluyendo modelos de 1.3B con 30 bloques y modelos de 14B con 40 bloques, con manejo especial para modelos de imagen a video que incluyen un componente adicional de incrustación de imagen. Cada componente de los modelos puede ponderarse individualmente para controlar la proporción de mezcla entre los dos modelos de entrada.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model1` | MODEL | Sí | - | Primer modelo a fusionar |
| `model2` | MODEL | Sí | - | Segundo modelo a fusionar |
| `patch_embedding.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el componente de incrustación de parches (predeterminado: 1.0) |
| `time_embedding.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el componente de incrustación temporal (predeterminado: 1.0) |
| `time_projection.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el componente de proyección temporal (predeterminado: 1.0) |
| `text_embedding.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el componente de incrustación de texto (predeterminado: 1.0) |
| `img_emb.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el componente de incrustación de imagen, utilizado en modelos de imagen a video (predeterminado: 1.0) |
| `blocks.0.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 0 (predeterminado: 1.0) |
| `blocks.1.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 1 (predeterminado: 1.0) |
| `blocks.2.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 2 (predeterminado: 1.0) |
| `blocks.3.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 3 (predeterminado: 1.0) |
| `blocks.4.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 4 (predeterminado: 1.0) |
| `blocks.5.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 5 (predeterminado: 1.0) |
| `blocks.6.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 6 (predeterminado: 1.0) |
| `blocks.7.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 7 (predeterminado: 1.0) |
| `blocks.8.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 8 (predeterminado: 1.0) |
| `blocks.9.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 9 (predeterminado: 1.0) |
| `blocks.10.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 10 (predeterminado: 1.0) |
| `blocks.11.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 11 (predeterminado: 1.0) |
| `blocks.12.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 12 (predeterminado: 1.0) |
| `blocks.13.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 13 (predeterminado: 1.0) |
| `blocks.14.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 14 (predeterminado: 1.0) |
| `blocks.15.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 15 (predeterminado: 1.0) |
| `blocks.16.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 16 (predeterminado: 1.0) |
| `blocks.17.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 17 (predeterminado: 1.0) |
| `blocks.18.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 18 (predeterminado: 1.0) |
| `blocks.19.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 19 (predeterminado: 1.0) |
| `blocks.20.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 20 (predeterminado: 1.0) |
| `blocks.21.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 21 (predeterminado: 1.0) |
| `blocks.22.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 22 (predeterminado: 1.0) |
| `blocks.23.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 23 (predeterminado: 1.0) |
| `blocks.24.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 24 (predeterminado: 1.0) |
| `blocks.25.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 25 (predeterminado: 1.0) |
| `blocks.26.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 26 (predeterminado: 1.0) |
| `blocks.27.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 27 (predeterminado: 1.0) |
| `blocks.28.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 28 (predeterminado: 1.0) |
| `blocks.29.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 29 (predeterminado: 1.0) |
| `blocks.30.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 30 (predeterminado: 1.0) |
| `blocks.31.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 31 (predeterminado: 1.0) |
| `blocks.32.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 32 (predeterminado: 1.0) |
| `blocks.33.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 33 (predeterminado: 1.0) |
| `blocks.34.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 34 (predeterminado: 1.0) |
| `blocks.35.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 35 (predeterminado: 1.0) |
| `blocks.36.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 36 (predeterminado: 1.0) |
| `blocks.37.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 37 (predeterminado: 1.0) |
| `blocks.38.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 38 (predeterminado: 1.0) |
| `blocks.39.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el bloque 39 (predeterminado: 1.0) |
| `head.` | FLOAT | Sí | 0.0 - 1.0 | Peso para el componente de cabeza (predeterminado: 1.0) |

**Nota:** Todos los parámetros de peso utilizan un rango de 0.0 a 1.0 con incrementos de 0.01. El nodo soporta hasta 40 bloques para acomodar diferentes tamaños de modelos, donde los modelos de 1.3B utilizan 30 bloques y los modelos de 14B utilizan 40 bloques. El parámetro `img_emb.` es específicamente para modelos de imagen a video.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | El modelo fusionado que combina componentes de ambos modelos de entrada según los pesos especificados |
