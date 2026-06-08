El nodo **Ventanas de Contexto (Manual)** te permite configurar manualmente ventanas de contexto para modelos durante el muestreo. Crea segmentos de contexto superpuestos con una longitud, superposición y patrones de programación específicos para procesar datos en fragmentos manejables, manteniendo la continuidad entre segmentos. Este nodo ofrece opciones avanzadas para controlar cómo se aplican las ventanas de contexto, incluyendo la mezcla de ruido, la retención de condicionamiento y la corrección de ventanas causales.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo al que se le aplicarán las ventanas de contexto durante el muestreo. | MODEL | Sí | - |
| `longitud_contexto` | La longitud de la ventana de contexto (predeterminado: 16). | INT | No | 1+ |
| `superposición_contexto` | La superposición de la ventana de contexto (predeterminado: 4). | INT | No | 0+ |
| `programación_contexto` | El paso de la ventana de contexto. | COMBO | No | `STATIC_STANDARD`<br>`UNIFORM_STANDARD`<br>`UNIFORM_LOOPED`<br>`BATCHED` |
| `paso_contexto` | El paso de la ventana de contexto; solo aplicable a programaciones uniformes (predeterminado: 1). | INT | No | 1+ |
| `bucle_cerrado` | Si se cierra el bucle de la ventana de contexto; solo aplicable a programaciones en bucle (predeterminado: Falso). | BOOLEAN | No | - |
| `método_de_fusión` | El método a utilizar para fusionar las ventanas de contexto (predeterminado: PYRAMID). | COMBO | No | `PYRAMID`<br>`LIST_STATIC` |
| `dimensión` | La dimensión a la que se aplicarán las ventanas de contexto (predeterminado: 0). | INT | No | 0-5 |
| `ruido_libre` | Si se aplica la mezcla de ruido FreeNoise, mejora la combinación de ventanas (predeterminado: Falso). | BOOLEAN | No | - |
| `cond_retain_index_list` | Lista de índices latentes a retener en los tensores de condicionamiento para cada ventana; por ejemplo, establecer esto en '0' usará la imagen inicial de inicio para cada ventana (predeterminado: ""). | STRING | No | - |
| `split_conds_to_windows` | Si se dividen múltiples condicionamientos (creados por ConditionCombine) en cada ventana según el índice de región (predeterminado: Falso). | BOOLEAN | No | - |
| `causal_window_fix` | Si se agrega un fotograma de corrección causal a las ventanas de contexto con índice distinto de 0 (predeterminado: Verdadero). | BOOLEAN | No | - |

**Restricciones de Parámetros:**

- `context_stride` solo se utiliza cuando se seleccionan programaciones uniformes
- `closed_loop` solo es aplicable a programaciones en bucle
- `dim` debe estar entre 0 y 5 inclusive
- `cond_retain_index_list` espera una lista de índices enteros separados por comas como una cadena (ej., "0,1,2")

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `modelo` | El modelo con ventanas de contexto aplicadas durante el muestreo. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ContextWindowsManual/es.md)

---
**Source fingerprint (SHA-256):** `b05ddda0ba38588305e6f733cd218c8b462268c39d16226ca961d09054187261`
