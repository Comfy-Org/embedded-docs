# LTXVContextWindows

Este nodo establece ventanas de contexto para modelos similares a LTXV durante el muestreo. Divide el proceso de generación de video en ventanas superpuestas para gestionar el uso de memoria y mejorar la coherencia temporal.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Requerido | Rango |
|-----------|-------------|--------------|-----------|-------|
| `model` | El modelo al que se aplicarán las ventanas de contexto durante el muestreo. | MODEL | Sí | - |
| `context_length` | La longitud de la ventana de contexto en fotogramas reales. Debe ser 8*n + 1. (predeterminado: 145) | INT | Sí | Mínimo: 1<br>Máximo: nodes.MAX_RESOLUTION<br>Paso: 8 |
| `context_overlap` | La superposición de la ventana de contexto en fotogramas reales. (predeterminado: 40) | INT | Sí | Mínimo: 0<br>Paso: 8 |
| `context_schedule` | Algoritmo de programación dependiente del paso para ventanas de contexto. (predeterminado: UNIFORM_STANDARD) | COMBO | Sí | `STATIC_STANDARD`<br>`UNIFORM_STANDARD`<br>`UNIFORM_LOOPED`<br>`BATCHED` |
| `context_stride` | El avance de la ventana de contexto; solo aplicable a programaciones uniformes. (predeterminado: 1) | INT | No | Mínimo: 1 |
| `closed_loop` | Si se cierra el bucle de la ventana de contexto; solo aplicable a programaciones en bucle. (predeterminado: False) | BOOLEAN | No | True<br>False |
| `fuse_method` | El método utilizado para fusionar las ventanas de contexto. (predeterminado: PYRAMID) | COMBO | Sí | Opciones de comfy.context_windows.ContextFuseMethods.LIST_STATIC |
| `freenoise` | Si se aplica la mezcla de ruido FreeNoise, mejora la combinación de ventanas. (predeterminado: True) | BOOLEAN | No | True<br>False |
| `retain_first_frame` | Conserva el primer fotograma latente en cada ventana de contexto (puede ayudar a mantener la referencia inicial). (predeterminado: False) | BOOLEAN | No | True<br>False |
| `split_conds_to_windows` | Si se dividen los múltiples condicionamientos (creados por ConditionCombine) en cada ventana según el índice de región. (predeterminado: False) | BOOLEAN | No | True<br>False |

**Nota:** El parámetro `context_length` debe seguir la fórmula 8*n + 1, donde n es un entero positivo. El nodo ajusta automáticamente el valor para cumplir con este requisito convirtiendo fotogramas reales a fotogramas latentes. El `context_overlap` también se convierte de fotogramas reales a fotogramas latentes (dividido entre 8).

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
|------------------|-------------|--------------|
| `MODEL` | El modelo con ventanas de contexto aplicadas para el muestreo. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVContextWindows/es.md)

---
**Source fingerprint (SHA-256):** `ad0b8c54acaab1853f6fe98dbad675478f033caf867df954b40b7db5208f5ae4`
