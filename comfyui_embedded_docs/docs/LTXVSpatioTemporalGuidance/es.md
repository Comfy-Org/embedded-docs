# LTXVSpatioTemporalGuidance

Este nodo mejora el detalle espacial y la coherencia del movimiento en la generación de video LTXV al ejecutar una pasada adicional en cada paso de muestreo. Durante esta pasada, la autoatención de los bloques del transformador seleccionados se degrada a un paso directo de valores, y la generación se guía para alejarse del resultado degradado.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `modelo` | El modelo base al que se le aplica la guía espacio-temporal. El modelo se clona y se modifica con una función de guía posterior a CFG. | MODEL | Sí | — |
| `escala` | La fuerza de la guía aplicada al resultado sin ruido. Cuando se establece en 0, la guía no tiene efecto. (por defecto: 1.0) | FLOAT | Sí | 0.0 a 100.0 (paso 0.01) |
| `bloques` | Índices de bloques del transformador separados por comas para perturbar. Solo se utilizan valores numéricos; cualquier otro carácter se ignora. (por defecto: "29") | STRING | Sí | — |
| `porcentaje_inicio` | La fracción del proceso de muestreo en la que comienza la guía. (por defecto: 0.0) | FLOAT | Sí | 0.0 a 1.0 (paso 0.001) |
| `porcentaje_fin` | La fracción del proceso de muestreo en la que finaliza la guía. (por defecto: 1.0) | FLOAT | Sí | 0.0 a 1.0 (paso 0.001) |

Nota: La guía solo se aplica durante el intervalo de muestreo entre `start_percent` y `end_percent`. Si `scale` es 0 o `blocks` no contiene valores numéricos, la pasada guiada no tiene efecto en el proceso de muestreo.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `MODEL` | El modelo clonado con la función de guía espacio-temporal incorporada. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSpatioTemporalGuidance/es.md)

---
**Source fingerprint (SHA-256):** `0e14137b3bf416d36005b6b4b6db46495b1523f88b2bf574e2dc582175422a48`
