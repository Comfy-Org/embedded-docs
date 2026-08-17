# Ventanas de Contexto WAN (Manual)

El nodo Wan Context Windows (Manual) te permite configurar manualmente ventanas de contexto para modelos similares a Wan con procesamiento bidimensional. Aplica la configuración de ventanas de contexto durante el muestreo especificando la longitud de la ventana, la superposición, el método de programación y la técnica de fusión, lo que te da control sobre cómo el modelo procesa diferentes regiones de contexto.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo al que se le aplicarán las ventanas de contexto durante el muestreo. | MODEL | Sí | - |
| `context_length` | La longitud de la ventana de contexto en fotogramas reales. Debe ser 4*n + 1. (por defecto: 81) | INT | Sí | 1 a 16384 (paso 4) |
| `context_overlap` | La superposición de la ventana de contexto en fotogramas reales. (por defecto: 30) | INT | Sí | 0 o mayor |
| `context_schedule` | Algoritmo de programación dependiente del paso para las ventanas de contexto. (por defecto: "uniform_standard") | COMBO | Sí | `"static_standard"`<br>`"uniform_standard"`<br>`"uniform_looped"`<br>`"batched"` |
| `context_stride` | El paso (stride) de la ventana de contexto; solo aplicable a programaciones uniformes. (por defecto: 1) | INT | Sí | 1 o mayor |
| `closed_loop` | Si se cierra el bucle de la ventana de contexto; solo aplicable a programaciones en bucle. (por defecto: False) | BOOLEAN | Sí | True o False |
| `fuse_method` | El método utilizado para fusionar las ventanas de contexto. (por defecto: "pyramid") | COMBO | Sí | `"pyramid"`<br>`"gaussian"`<br>`"average"`<br>`"overlap"` |
| `freenoise` | Si se aplica la reorganización de ruido FreeNoise, mejora la mezcla de ventanas. (por defecto: True) | BOOLEAN | Sí | True o False |
| `retain_first_frame` | Conservar el primer fotograma I2V en cada ventana de contexto (puede ayudar a mantener la referencia inicial). (por defecto: False) | BOOLEAN | Sí | True o False |
| `split_conds_to_windows` | Si se dividen los múltiples condicionamientos (creados por ConditionCombine) en cada ventana según el índice de región. (por defecto: False) | BOOLEAN | Sí | True o False |

**Nota:** `context_stride` solo afecta a las programaciones uniformes, y `closed_loop` solo se aplica a las programaciones en bucle. `context_length` debe seguir el patrón 4n + 1. El nodo convierte `context_length` y `context_overlap` de fotogramas reales a unidades de modelo antes de aplicarlos, imponiendo un mínimo de 1 para `context_length` y 0 para `context_overlap`. Las entradas `context_stride`, `closed_loop`, `freenoise` y `split_conds_to_windows` son opciones avanzadas.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | El modelo con la configuración de ventana de contexto aplicada. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanContextWindowsManual/es.md)

---
**Source fingerprint (SHA-256):** `cf4927371e9d4b509f2e6e5319cd6109e3ef36da6b3faee278bcf8c906672857`
