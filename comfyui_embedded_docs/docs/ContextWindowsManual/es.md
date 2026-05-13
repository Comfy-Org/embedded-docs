> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ContextWindowsManual/es.md)

El nodo **Ventanas de Contexto (Manual)** te permite configurar manualmente ventanas de contexto para modelos durante el muestreo. Crea segmentos de contexto superpuestos con una longitud, superposición y patrones de programación específicos para procesar datos en fragmentos manejables, manteniendo la continuidad entre segmentos. Este nodo ofrece opciones avanzadas para controlar cómo se aplican las ventanas de contexto, incluyendo la mezcla de ruido, la retención de condicionamiento y la corrección de ventanas causales.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `modelo` | MODEL | Sí | - | El modelo al que se le aplicarán las ventanas de contexto durante el muestreo. |
| `longitud_contexto` | INT | No | 1+ | La longitud de la ventana de contexto (predeterminado: 16). |
| `superposición_contexto` | INT | No | 0+ | La superposición de la ventana de contexto (predeterminado: 4). |
| `programación_contexto` | COMBO | No | `STATIC_STANDARD`<br>`UNIFORM_STANDARD`<br>`UNIFORM_LOOPED`<br>`BATCHED` | El paso de la ventana de contexto. |
| `paso_contexto` | INT | No | 1+ | El paso de la ventana de contexto; solo aplicable a programaciones uniformes (predeterminado: 1). |
| `bucle_cerrado` | BOOLEAN | No | - | Si se cierra el bucle de la ventana de contexto; solo aplicable a programaciones en bucle (predeterminado: Falso). |
| `método_de_fusión` | COMBO | No | `PYRAMID`<br>`LIST_STATIC` | El método a utilizar para fusionar las ventanas de contexto (predeterminado: PYRAMID). |
| `dimensión` | INT | No | 0-5 | La dimensión a la que se aplicarán las ventanas de contexto (predeterminado: 0). |
| `ruido_libre` | BOOLEAN | No | - | Si se aplica la mezcla de ruido FreeNoise, mejora la combinación de ventanas (predeterminado: Falso). |
| `cond_retain_index_list` | STRING | No | - | Lista de índices latentes a retener en los tensores de condicionamiento para cada ventana; por ejemplo, establecer esto en '0' usará la imagen inicial de inicio para cada ventana (predeterminado: ""). |
| `split_conds_to_windows` | BOOLEAN | No | - | Si se dividen múltiples condicionamientos (creados por ConditionCombine) en cada ventana según el índice de región (predeterminado: Falso). |
| `causal_window_fix` | BOOLEAN | No | - | Si se agrega un fotograma de corrección causal a las ventanas de contexto con índice distinto de 0 (predeterminado: Verdadero). |

**Restricciones de Parámetros:**

- `context_stride` solo se utiliza cuando se seleccionan programaciones uniformes
- `closed_loop` solo es aplicable a programaciones en bucle
- `dim` debe estar entre 0 y 5 inclusive
- `cond_retain_index_list` espera una lista de índices enteros separados por comas como una cadena (ej., "0,1,2")

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `modelo` | MODEL | El modelo con ventanas de contexto aplicadas durante el muestreo. |

---
**Source fingerprint (SHA-256):** `b05ddda0ba38588305e6f733cd218c8b462268c39d16226ca961d09054187261`
