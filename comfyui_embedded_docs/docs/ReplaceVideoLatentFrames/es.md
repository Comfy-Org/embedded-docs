# ReplaceVideoLatentFrames

El nodo ReplaceVideoLatentFrames inserta fotogramas de un video latente de origen en un video latente de destino, comenzando en un índice de fotograma especificado. Si el latente de origen no se proporciona, el latente de destino se devuelve sin cambios. El nodo maneja la indexación negativa y emitirá una advertencia si los fotogramas de origen no caben dentro del destino.

## Entradas

| Parámetro | Descripción | Tipo de dato | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `destination` | El latente de destino donde se reemplazarán los fotogramas. | LATENT | Sí | - |
| `source` | El latente de origen que proporciona los fotogramas para insertar en el latente de destino. Si no se proporciona, el latente de destino se devuelve sin cambios. | LATENT | No | - |
| `index` | El índice de fotograma latente inicial en el latente de destino donde se colocarán los fotogramas del latente de origen. Los valores negativos cuentan desde el final (predeterminado: 0). | INT | Sí | -MAX_RESOLUTION to MAX_RESOLUTION (step: 1) |

**Restricciones:**

* El `index` debe estar dentro de los límites del recuento de fotogramas del latente de destino. Si no es así, se registra una advertencia y el destino se devuelve sin cambios.
* Los fotogramas del latente de origen deben caber dentro de los fotogramas del latente de destino a partir del `index` especificado. Si no caben, se registra una advertencia y el destino se devuelve sin cambios.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `output` | El video latente resultante después de la operación de reemplazo de fotogramas. | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReplaceVideoLatentFrames/es.md)

---
**Source fingerprint (SHA-256):** `5b98d875bdeaec63521bff19fecbc5510036c8b4f90322d8296b216688b557bf`
