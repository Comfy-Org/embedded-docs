> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReplaceVideoLatentFrames/es.md)

El nodo ReplaceVideoLatentFrames inserta fotogramas de un video latente fuente en un video latente de destino, comenzando en un índice de fotograma especificado. Si no se proporciona el latente fuente, se devuelve el latente de destino sin cambios. El nodo maneja índices negativos y emitirá una advertencia si los fotogramas fuente no caben dentro del destino.

## Entradas

| Parámetro | Tipo de dato | Requerido | Rango | Descripción |
|-----------|--------------|-----------|-------|-------------|
| `destination` | LATENT | Sí | - | El latente de destino donde se reemplazarán los fotogramas. |
| `source` | LATENT | No | - | El latente fuente que proporciona los fotogramas a insertar en el latente de destino. Si no se proporciona, se devuelve el latente de destino sin cambios. |
| `index` | INT | Sí | -MAX_RESOLUTION a MAX_RESOLUTION | El índice de fotograma latente inicial en el latente de destino donde se colocarán los fotogramas del latente fuente. Los valores negativos cuentan desde el final (predeterminado: 0). |

**Restricciones:**

* El `index` debe estar dentro de los límites del recuento de fotogramas del latente de destino. Si no es así, se registra una advertencia y se devuelve el destino sin cambios.
* Los fotogramas del latente fuente deben caber dentro de los fotogramas del latente de destino a partir del `index` especificado. Si no es así, se registra una advertencia y se devuelve el destino sin cambios.

## Salidas

| Nombre de salida | Tipo de dato | Descripción |
|------------------|--------------|-------------|
| `output` | LATENT | El video latente resultante después de la operación de reemplazo de fotogramas. |

---
**Source fingerprint (SHA-256):** `b4e2b3dcdaa5c400fefc30262ae05cd1849896e6cb6bbb3a1bd6ce4d31583e23`
