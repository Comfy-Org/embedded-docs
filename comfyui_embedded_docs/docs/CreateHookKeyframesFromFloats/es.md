> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframesFromFloats/es.md)

Este nodo crea fotogramas clave de enlace a partir de una lista de valores de intensidad de punto flotante, distribuyéndolos uniformemente entre porcentajes de inicio y fin especificados. Genera una secuencia de fotogramas clave donde cada valor de intensidad se asigna a una posición porcentual específica en la línea de tiempo de la animación. El nodo puede crear un nuevo grupo de fotogramas clave o agregarlo a uno existente, con una opción para imprimir los fotogramas clave generados con fines de depuración.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|--------------|-----------|-------|-------------|
| `fuerza_flotantes` | FLOATS | Sí | -1 a ∞ | Un valor flotante único o una lista de valores flotantes que representan los valores de intensidad para los fotogramas clave (predeterminado: -1) |
| `porcentaje_inicio` | FLOAT | Sí | 0.0 a 1.0 | La posición porcentual inicial para el primer fotograma clave en la línea de tiempo (predeterminado: 0.0) |
| `porcentaje_final` | FLOAT | Sí | 0.0 a 1.0 | La posición porcentual final para el último fotograma clave en la línea de tiempo (predeterminado: 1.0) |
| `imprimir_keyframes` | BOOLEAN | Sí | True/False | Cuando está habilitado, imprime la información de los fotogramas clave generados en la consola (predeterminado: False) |
| `prev_hook_kf` | HOOK_KEYFRAMES | No | - | Un grupo de fotogramas clave de enlace existente al que agregar los nuevos fotogramas clave, o crea un nuevo grupo si no se proporciona |

**Nota:** El parámetro `floats_strength` acepta un único valor flotante o una lista iterable de flotantes. Los fotogramas clave se distribuyen linealmente entre `start_percent` y `end_percent` según la cantidad de valores de intensidad proporcionados. Se garantiza que el primer fotograma clave tenga al menos un paso para asegurar su aplicación.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `HOOK_KF` | HOOK_KEYFRAMES | Un grupo de fotogramas clave de enlace que contiene los fotogramas clave recién creados, ya sea como un grupo nuevo o añadido al grupo de fotogramas clave de entrada |

---
**Source fingerprint (SHA-256):** `566864ec72062d913d95b38b3c53c655d4fdd971a01c4bec54669850b2feddc8`
