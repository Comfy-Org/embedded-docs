# EstablecerPrimeraSigma

El nodo `SetFirstSigma` modifica una secuencia de valores sigma reemplazando el primer valor sigma de la secuencia por un valor personalizado. Toma una secuencia sigma existente y un nuevo valor sigma como entradas, y devuelve una nueva secuencia sigma en la que solo se ha cambiado el primer elemento, manteniendo sin cambios todos los demás valores sigma.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `sigmas` | La secuencia de entrada de valores sigma que se va a modificar | SIGMAS | Sí | - |
| `sigma` | El nuevo valor sigma que se establecerá como primer elemento de la secuencia (por defecto: 136.0) | FLOAT | Sí | 0.0 a 20000.0 |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `sigmas` | La secuencia sigma modificada, con el primer elemento reemplazado por el valor sigma personalizado | SIGMAS |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetFirstSigma/es.md)

---
**Source fingerprint (SHA-256):** `5302bc61a7ca094fee9ee2ad8c9dc32997ef0bbf27c9945acd7287e7df6b6db3`
