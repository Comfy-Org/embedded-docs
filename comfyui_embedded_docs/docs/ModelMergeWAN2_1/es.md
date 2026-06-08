El nodo `ModelMergeWAN2_1` fusiona dos modelos WAN2.1 combinando sus componentes mediante promedios ponderados. Admite diferentes tamaños de modelo, incluidos modelos de 1.3B con 30 bloques y modelos de 14B con 40 bloques, con manejo especial para modelos de imagen a video que incluyen un componente adicional de incrustación de imagen. Cada componente de los modelos puede ponderarse individualmente para controlar la proporción de fusión entre los dos modelos de entrada.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `model1` | Primer modelo a fusionar | MODEL | Sí | - |
| `model2` | Segundo modelo a fusionar | MODEL | Sí | - |
| `patch_embedding.` | Peso para el componente de incrustación de parches (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `time_embedding.` | Peso para el componente de incrustación temporal (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `time_projection.` | Peso para el componente de proyección temporal (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `text_embedding.` | Peso para el componente de incrustación de texto (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `img_emb.` | Peso para el componente de incrustación de imagen, utilizado en modelos de imagen a video (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.0.` | Peso para el bloque 0 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.1.` | Peso para el bloque 1 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.2.` | Peso para el bloque 2 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.3.` | Peso para el bloque 3 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.4.` | Peso para el bloque 4 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.5.` | Peso para el bloque 5 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.6.` | Peso para el bloque 6 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.7.` | Peso para el bloque 7 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.8.` | Peso para el bloque 8 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.9.` | Peso para el bloque 9 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.10.` | Peso para el bloque 10 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.11.` | Peso para el bloque 11 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.12.` | Peso para el bloque 12 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.13.` | Peso para el bloque 13 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.14.` | Peso para el bloque 14 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.15.` | Peso para el bloque 15 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.16.` | Peso para el bloque 16 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.17.` | Peso para el bloque 17 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.18.` | Peso para el bloque 18 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.19.` | Peso para el bloque 19 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.20.` | Peso para el bloque 20 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.21.` | Peso para el bloque 21 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.22.` | Peso para el bloque 22 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.23.` | Peso para el bloque 23 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.24.` | Peso para el bloque 24 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.25.` | Peso para el bloque 25 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.26.` | Peso para el bloque 26 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.27.` | Peso para el bloque 27 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.28.` | Peso para el bloque 28 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.29.` | Peso para el bloque 29 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.30.` | Peso para el bloque 30 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.31.` | Peso para el bloque 31 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.32.` | Peso para el bloque 32 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.33.` | Peso para el bloque 33 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.34.` | Peso para el bloque 34 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.35.` | Peso para el bloque 35 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.36.` | Peso para el bloque 36 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.37.` | Peso para el bloque 37 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.38.` | Peso para el bloque 38 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `blocks.39.` | Peso para el bloque 39 (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |
| `head.` | Peso para el componente de cabecera (predeterminado: 1.0) | FLOAT | Sí | 0.0 - 1.0 |

**Nota:** Todos los parámetros de peso utilizan un rango de 0.0 a 1.0 con incrementos de 0.01. El nodo admite hasta 40 bloques para adaptarse a diferentes tamaños de modelo, donde los modelos de 1.3B utilizan 30 bloques y los modelos de 14B utilizan 40 bloques. El parámetro `img_emb.` es específico para modelos de imagen a video.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `model` | El modelo fusionado que combina componentes de ambos modelos de entrada según los pesos especificados | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeWAN2_1/es.md)

---
**Source fingerprint (SHA-256):** `d550a2f62bbcb4b46ccdd8a04fab80e93f96ea63426d48acb3515d51175efc99`
