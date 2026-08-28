# LTXV Spatio-Temporal Guidance (STG)

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|-----------|----------|-------|
| `modelo` | El modelo base al que se aplica la guía espaciotemporal. El modelo se clona y se modifica con una función de guía posterior a CFG. | MODEL | Sí | — |
| `escala` | La intensidad de la guía aplicada al resultado denoizado. Cuando se establece en 0, la guía no tiene efecto. (por defecto: 1.0) | FLOAT | Sí | 0.0 a 100.0 (step 0.01) |
| `bloques` | Índices de bloques de transformador separados por comas para perturbar. Solo se usan valores numéricos; cualquier otro carácter se ignora. (por defecto: "29") | STRING | Sí | — |
| `porcentaje_inicio` | La fracción del proceso de muestreo en la que comienza la guía. Este es un parámetro avanzado. (por defecto: 0.0) | FLOAT | Sí | 0.0 a 1.0 (step 0.001) |
| `porcentaje_fin` | La fracción del proceso de muestreo en la que termina la guía. Este es un parámetro avanzado. (por defecto: 1.0) | FLOAT | Sí | 0.0 a 1.0 (step 0.001) |

Nota: la guía solo se aplica durante el intervalo de muestreo entre `start_percent` y `end_percent`. Si `scale` es 0 o `blocks` no contiene valores numéricos, la pasada guiada no tiene efecto en el proceso de muestreo.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `MODEL` | El modelo clonado con la función de guía espaciotemporal adjunta. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSpatioTemporalGuidance/es.md)

---
**Source fingerprint (SHA-256):** `0e14137b3bf416d36005b6b4b6db46495b1523f88b2bf574e2dc582175422a48`
