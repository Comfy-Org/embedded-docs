> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ContextWindowsManual/es.md)

El nodo Ventanas de Contexto (Manual) permite configurar manualmente ventanas de contexto para modelos durante el muestreo. Crea segmentos de contexto superpuestos con longitud, superposición y patrones de programación especificados para procesar datos en fragmentos manejables mientras mantiene la continuidad entre segmentos.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo al que aplicar las ventanas de contexto durante el muestreo. |
| `context_length` | INT | No | 1+ | La longitud de la ventana de contexto (por defecto: 16). |
| `context_overlap` | INT | No | 0+ | La superposición de la ventana de contexto (por defecto: 4). |
| `context_schedule` | COMBO | No | `STATIC_STANDARD`<br>`UNIFORM_STANDARD`<br>`UNIFORM_LOOPED`<br>`BATCHED` | El paso de la ventana de contexto. |
| `context_stride` | INT | No | 1+ | El paso de la ventana de contexto; solo aplicable a programaciones uniformes (por defecto: 1). |
| `closed_loop` | BOOLEAN | No | - | Si cerrar o no el bucle de la ventana de contexto; solo aplicable a programaciones en bucle (por defecto: False). |
| `fuse_method` | COMBO | No | `PYRAMID`<br>`LIST_STATIC` | El método a usar para fusionar las ventanas de contexto (por defecto: PYRAMID). |
| `dim` | INT | No | 0-5 | La dimensión a la que aplicar las ventanas de contexto (por defecto: 0). |

**Restricciones de Parámetros:**

- `context_stride` solo se usa cuando se seleccionan programaciones uniformes
- `closed_loop` solo es aplicable a programaciones en bucle
- `dim` debe estar entre 0 y 5 inclusive

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | El modelo con ventanas de contexto aplicadas durante el muestreo. |
