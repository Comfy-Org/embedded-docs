> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframesFromFloats/es.md)

Este nodo crea fotogramas clave de enlace a partir de una lista de valores de fuerza de punto flotante, distribuyéndolos uniformemente entre los porcentajes de inicio y fin especificados. Genera una secuencia de fotogramas clave donde cada valor de fuerza se asigna a una posición porcentual específica en la línea de tiempo de la animación. El nodo puede crear un nuevo grupo de fotogramas clave o agregar a uno existente, con una opción para imprimir los fotogramas clave generados con fines de depuración.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `fuerza_flotantes` | FLOATS | Sí | -1 a ∞ | Un único valor flotante o una lista de valores flotantes que representan los valores de fuerza para los fotogramas clave (valor por defecto: -1) |
| `porcentaje_inicio` | FLOAT | Sí | 0.0 a 1.0 | La posición porcentual inicial para el primer fotograma clave en la línea de tiempo (valor por defecto: 0.0) |
| `porcentaje_final` | FLOAT | Sí | 0.0 a 1.0 | La posición porcentual final para el último fotograma clave en la línea de tiempo (valor por defecto: 1.0) |
| `imprimir_keyframes` | BOOLEAN | Sí | True/False | Cuando está habilitado, imprime la información de los fotogramas clave generados en la consola (valor por defecto: False) |
| `prev_hook_kf` | HOOK_KEYFRAMES | No | - | Un grupo existente de fotogramas clave de enlace al que agregar los nuevos fotogramas clave, o crea un nuevo grupo si no se proporciona |

**Nota:** El parámetro `floats_strength` acepta un único valor flotante o una lista iterable de flotantes. Los fotogramas clave se distribuyen linealmente entre `start_percent` y `end_percent` según la cantidad de valores de fuerza proporcionados.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `HOOK_KF` | HOOK_KEYFRAMES | Un grupo de fotogramas clave de enlace que contiene los fotogramas clave recién creados, ya sea como un nuevo grupo o agregados al grupo de fotogramas clave de entrada |
