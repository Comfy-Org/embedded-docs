> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanContextWindowsManual/es.md)

# Ventanas de Contexto WAN (Manual)

El nodo Ventanas de Contexto WAN (Manual) permite configurar manualmente ventanas de contexto para modelos similares a WAN con procesamiento bidimensional. Aplica configuraciones personalizadas de ventanas de contexto durante el muestreo especificando la longitud de la ventana, la superposición, el método de programación y la técnica de fusión. Esto proporciona un control preciso sobre cómo el modelo procesa la información en diferentes regiones de contexto.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|---------------|-----------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo al que se aplicarán las ventanas de contexto durante el muestreo. |
| `context_length` | INT | Sí | 1 a 1048576 | La longitud de la ventana de contexto (predeterminado: 81). |
| `context_overlap` | INT | Sí | 0 a 1048576 | La superposición de la ventana de contexto (predeterminado: 30). |
| `context_schedule` | COMBO | Sí | `"static_standard"`<br>`"uniform_standard"`<br>`"uniform_looped"`<br>`"batched"` | El paso de la ventana de contexto. |
| `context_stride` | INT | Sí | 1 a 1048576 | El paso de la ventana de contexto; solo aplicable a programaciones uniformes (predeterminado: 1). |
| `closed_loop` | BOOLEAN | Sí | - | Si se debe cerrar el bucle de la ventana de contexto; solo aplicable a programaciones en bucle (predeterminado: Falso). |
| `fuse_method` | COMBO | Sí | `"pyramid"`<br>`"gaussian"`<br>`"average"`<br>`"overlap"` | El método a utilizar para fusionar las ventanas de contexto (predeterminado: "pyramid"). |
| `freenoise` | BOOLEAN | Sí | - | Si se debe aplicar la mezcla de ruido FreeNoise, mejora la combinación de ventanas (predeterminado: Falso). |

**Nota:** El parámetro `context_stride` solo afecta a las programaciones uniformes, y `closed_loop` solo se aplica a las programaciones en bucle. Los valores de longitud y superposición de contexto se ajustan automáticamente para garantizar valores mínimos válidos durante el procesamiento. El parámetro `fuse_method` ahora incluye opciones adicionales más allá de solo "pyramid".

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|---------------|-------------|
| `model` | MODEL | El modelo con la configuración de ventana de contexto aplicada. |

---
**Source fingerprint (SHA-256):** `33e539f1e6647a6a2bc98fadc357a25279b0900746f5b3d568e2782cdb770258`
