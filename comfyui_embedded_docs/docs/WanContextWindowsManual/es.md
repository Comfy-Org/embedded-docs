> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanContextWindowsManual/es.md)

El nodo Ventanas de Contexto WAN (Manual) permite configurar manualmente las ventanas de contexto para modelos tipo WAN con procesamiento bidimensional. Aplica configuraciones personalizadas de ventanas de contexto durante el muestreo especificando la longitud de ventana, superposición, método de programación y técnica de fusión. Esto proporciona control preciso sobre cómo el modelo procesa la información a través de diferentes regiones de contexto.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo al que aplicar las ventanas de contexto durante el muestreo. |
| `context_length` | INT | Sí | 1 a 1048576 | La longitud de la ventana de contexto (valor por defecto: 81). |
| `context_overlap` | INT | Sí | 0 a 1048576 | La superposición de la ventana de contexto (valor por defecto: 30). |
| `context_schedule` | COMBO | Sí | "static_standard"<br>"uniform_standard"<br>"uniform_looped"<br>"batched" | El paso de la ventana de contexto. |
| `context_stride` | INT | Sí | 1 a 1048576 | El paso de la ventana de contexto; solo aplicable a programaciones uniformes (valor por defecto: 1). |
| `closed_loop` | BOOLEAN | Sí | - | Si cerrar el bucle de la ventana de contexto; solo aplicable a programaciones en bucle (valor por defecto: False). |
| `fuse_method` | COMBO | Sí | "pyramid" | El método a usar para fusionar las ventanas de contexto (valor por defecto: "pyramid"). |

**Nota:** El parámetro `context_stride` solo afecta a las programaciones uniformes, y `closed_loop` solo se aplica a las programaciones en bucle. Los valores de longitud y superposición de contexto se ajustan automáticamente para garantizar valores mínimos válidos durante el procesamiento.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | El modelo con la configuración de ventana de contexto aplicada. |
