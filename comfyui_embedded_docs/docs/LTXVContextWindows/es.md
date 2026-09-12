# Ventanas de Contexto LTXV

Aquí tienes la traducción al español:

---

Este nodo establece ventanas de contexto para modelos similares a LTXV durante el muestreo. Divide el proceso de generación de video en ventanas superpuestas para gestionar el uso de memoria y mejorar la coherencia temporal.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
|-----------|-------------|-----------|----------|-------|
| `model` | El modelo al que se le aplican las ventanas de contexto durante el muestreo. | MODEL | Sí | - |
| `context_length` | La longitud de la ventana de contexto en fotogramas reales. Debe ser 8*n + 1. (por defecto: 145) | INT | Sí | Mínimo: 1<br>Máximo: nodes.MAX_RESOLUTION<br>Paso: 8 |
| `context_overlap` | La superposición de la ventana de contexto en fotogramas reales. (por defecto: 40) | INT | Sí | Mínimo: 0<br>Paso: 8 |
| `context_schedule` | Algoritmo de programación dependiente del paso para las ventanas de contexto. (por defecto: UNIFORM_STANDARD) | COMBO | Sí | `STATIC_STANDARD`<br>`UNIFORM_STANDARD`<br>`UNIFORM_LOOPED`<br>`BATCHED` |
| `context_stride` | El stride de la ventana de contexto; solo aplicable a las programaciones uniformes. (por defecto: 1) | INT | Sí | Mínimo: 1 |
| `closed_loop` | Si se cierra el bucle de la ventana de contexto; solo aplicable a las programaciones en bucle. (por defecto: False) | BOOLEAN | Sí | True<br>False |
| `fuse_method` | El método que se usará para fusionar las ventanas de contexto. (por defecto: PYRAMID) | COMBO | Sí | Opciones de comfy.context_windows.ContextFuseMethods.LIST_STATIC |
| `freenoise` | Si se aplica la reorganización de ruido FreeNoise; mejora la combinación de ventanas. (por defecto: True) | BOOLEAN | Sí | True<br>False |
| `retain_first_frame` | Conservar el primer fotograma latente en cada ventana de contexto (puede ayudar a mantener la referencia inicial). (por defecto: False) | BOOLEAN | Sí | True<br>False |
| `split_conds_to_windows` | Si se dividen múltiples condicionamientos (creados por ConditionCombine) en cada ventana según el índice de región. (por defecto: False) | BOOLEAN | Sí | True<br>False |

**Nota:** El parámetro `context_length` debe seguir la fórmula 8*n + 1, donde n es un entero positivo. El nodo ajusta automáticamente el valor para cumplir este requisito convirtiendo fotogramas reales a fotogramas latentes. El `context_overlap` también se convierte de fotogramas reales a fotogramas latentes (dividido por 8).

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|-------------|-------------|-----------|
| `MODEL` | El modelo con ventanas de contexto aplicadas para el muestreo. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVContextWindows/es.md)

---
**Source fingerprint (SHA-256):** `148649d0a938e08c932a163f5d7614332626fba37b8f79db7f92bbcf422e692f`
