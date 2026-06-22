# EstablecerPrimeraSigma

El nodo `SetFirstSigma` modifica una secuencia de valores sigma reemplazando el primer valor de la secuencia con un valor personalizado. Toma una secuencia sigma existente y un nuevo valor sigma como entradas, luego devuelve una nueva secuencia sigma donde solo se ha modificado el primer elemento, manteniendo todos los demás valores sigma sin cambios.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `sigmas` | La secuencia de entrada de valores sigma que se modificará | SIGMAS | Sí | - |
| `sigma` | El nuevo valor sigma que se establecerá como primer elemento de la secuencia (predeterminado: 136.0) | FLOAT | Sí | 0.0 a 20000.0 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `sigmas` | La secuencia sigma modificada con el primer elemento reemplazado por el valor sigma personalizado | SIGMAS |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetFirstSigma/es.md)

---
**Source fingerprint (SHA-256):** `2414acd7f3f42032c12bae2c581de4721f4c1daa912255fa0956caaa567291d5`
