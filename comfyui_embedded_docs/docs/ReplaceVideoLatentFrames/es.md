> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReplaceVideoLatentFrames/es.md)

El nodo ReplaceVideoLatentFrames inserta fotogramas de un vídeo latente fuente en un vídeo latente destino, comenzando en un índice de fotograma especificado. Si no se proporciona el latente fuente, se devuelve el latente destino sin cambios. El nodo maneja índices negativos y emitirá una advertencia si los fotogramas fuente no caben dentro del destino.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `destination` | LATENT | Sí | - | El latente destino donde se reemplazarán los fotogramas. |
| `source` | LATENT | No | - | El latente fuente que proporciona los fotogramas a insertar en el latente destino. Si no se proporciona, se devuelve el latente destino sin cambios. |
| `index` | INT | No | -MAX_RESOLUTION a MAX_RESOLUTION | El índice de fotograma latente inicial en el latente destino donde se colocarán los fotogramas del latente fuente. Los valores negativos cuentan desde el final (por defecto: 0). |

**Restricciones:**

* El `index` debe estar dentro de los límites del número de fotogramas del latente destino. Si no lo está, se registra una advertencia y se devuelve el destino sin cambios.
* Los fotogramas del latente fuente deben caber dentro de los fotogramas del latente destino a partir del `index` especificado. Si no es así, se registra una advertencia y se devuelve el destino sin cambios.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | LATENT | El vídeo latente resultante tras la operación de reemplazo de fotogramas. |
