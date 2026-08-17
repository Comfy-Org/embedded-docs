# Ventanas de Contexto (Manual)

El nodo Context Windows (Manual) le permite configurar manualmente ventanas de contexto para modelos durante el muestreo. Crea segmentos de contexto superpuestos con una longitud, superposición y patrones de programación especificados para procesar datos en fragmentos manejables manteniendo la continuidad entre segmentos. Este nodo proporciona opciones avanzadas para controlar cómo se aplican las ventanas de contexto, incluida la reorganización de ruido, la retención de condicionamiento, la retención de ruido latente y las correcciones de ventana causal.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo al que se le aplicarán ventanas de contexto durante el muestreo. | MODEL | Sí | - |
| `context_length` | La longitud de la ventana de contexto (por defecto: 16). | INT | No | 1+ |
| `context_overlap` | La superposición de la ventana de contexto (por defecto: 4). | INT | No | 0+ |
| `context_schedule` | Algoritmo de programación dependiente del paso para ventanas de contexto (por defecto: STATIC_STANDARD). | COMBO | No | `"STATIC_STANDARD"`<br>`"UNIFORM_STANDARD"`<br>`"UNIFORM_LOOPED"`<br>`"BATCHED"` |
| `context_stride` | El paso (stride) de la ventana de contexto; solo aplicable a programaciones uniformes (por defecto: 1). | INT | No | 1+ |
| `closed_loop` | Si se debe cerrar el bucle de la ventana de contexto; solo aplicable a programaciones en bucle (por defecto: False). | BOOLEAN | No | - |
| `fuse_method` | El método que se utiliza para fusionar las ventanas de contexto (por defecto: PYRAMID). | COMBO | No | `"PYRAMID"`<br>`"LIST_STATIC"` |
| `dim` | La dimensión a la que se aplican las ventanas de contexto (por defecto: 0). | INT | No | 0-5 |
| `freenoise` | Si se debe aplicar la reorganización de ruido FreeNoise, mejora la fusión de ventanas (por defecto: False). | BOOLEAN | No | - |
| `cond_retain_index_list` | Lista de índices latentes a retener en los tensores de condicionamiento para cada ventana. Para modelos I2V de estilo concat (p. ej., Wan I2V, HunyuanVideo I2V, Cosmos I2V, SVD) la imagen inicial codificada reside en los canales de condicionamiento c_concat; establecer esto a '0' retendrá el contenido de esa imagen inicial en la sub-posición 0 de cada ventana (por defecto: ""). | STRING | No | - |
| `split_conds_to_windows` | Si se deben dividir múltiples condicionamientos (creados por ConditionCombine) en cada ventana según el índice de región (por defecto: False). | BOOLEAN | No | - |
| `latent_retain_index_list` | Lista de índices latentes a retener en el propio ruido latente para cada ventana. Útil para flujos de trabajo donde el contenido de referencia (p. ej., una imagen inicial) reside directamente en el ruido latente en lugar de en canales de condicionamiento separados (p. ej., I2V de estilo inplace como LTXV, AnimateDiff). Independiente de `cond_retain_index_list` (por defecto: ""). | STRING | No | - |
| `causal_window_fix` | Si se debe agregar un fotograma de corrección causal a las ventanas de contexto con índice distinto de 0 (por defecto: True). | BOOLEAN | No | - |

**Restricciones de parámetros:**

- `context_stride` solo se usa cuando se seleccionan programaciones uniformes
- `closed_loop` solo es aplicable a programaciones en bucle
- `dim` debe estar entre 0 y 5 inclusive
- `cond_retain_index_list` espera una lista de índices enteros separados por comas como cadena (p. ej., "0,1,2")
- `latent_retain_index_list` espera una lista de índices enteros separados por comas como cadena (p. ej., "0,1,2") y es independiente de `cond_retain_index_list`

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | El modelo con ventanas de contexto aplicadas durante el muestreo. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ContextWindowsManual/es.md)

---
**Source fingerprint (SHA-256):** `39dc39ece3d3c10c13ca8c4b85af4fbbebbcaba8a019145a6d4727c3df7b302b`
