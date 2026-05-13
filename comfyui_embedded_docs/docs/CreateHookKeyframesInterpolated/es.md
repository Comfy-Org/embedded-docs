> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframesInterpolated/es.md)

Crea una secuencia de fotogramas clave de hook con valores de intensidad interpolados entre un punto inicial y final. El nodo genera múltiples fotogramas clave que realizan una transición suave del parámetro de intensidad a lo largo de un rango porcentual específico del proceso de generación, utilizando varios métodos de interpolación para controlar la curva de transición.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `strength_start` | FLOAT | Sí | 0.0 - 10.0 | Valor de intensidad inicial para la secuencia de interpolación (predeterminado: 1.0) |
| `strength_end` | FLOAT | Sí | 0.0 - 10.0 | Valor de intensidad final para la secuencia de interpolación (predeterminado: 1.0) |
| `interpolación` | COMBO | Sí | `LINEAR`<br>`EASE_IN`<br>`EASE_OUT`<br>`EASE_IN_OUT`<br>`EASE_OUT_IN`<br>`SINE`<br>`CUBIC`<br>`QUARTIC`<br>`QUINTIC`<br>`EXPO`<br>`CIRC`<br>`BACK`<br>`BOUNCE`<br>`ELASTIC` | Método de interpolación utilizado para la transición entre valores de intensidad (predeterminado: LINEAR) |
| `start_percent` | FLOAT | Sí | 0.0 - 1.0 | Posición porcentual inicial en el proceso de generación (predeterminado: 0.0) |
| `end_percent` | FLOAT | Sí | 0.0 - 1.0 | Posición porcentual final en el proceso de generación (predeterminado: 1.0) |
| `keyframes_count` | INT | Sí | 2 - 100 | Número de fotogramas clave a generar en la secuencia de interpolación (predeterminado: 5) |
| `print_keyframes` | BOOLEAN | Sí | True/False | Si se debe imprimir la información de los fotogramas clave generados en el registro (predeterminado: False) |
| `prev_hook_kf` | HOOK_KEYFRAMES | No | - | Grupo opcional de fotogramas clave de hook anterior al que añadir |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `HOOK_KF` | HOOK_KEYFRAMES | El grupo de fotogramas clave de hook generado que contiene la secuencia interpolada |

---
**Source fingerprint (SHA-256):** `f90c96745ca1f02bbb02e08d2d82be1bbb1f3c80ac5d53a4c6bc07a0e2b8d76f`
