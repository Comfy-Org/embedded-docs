> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PerpNegGuider/es.md)

El nodo PerpNegGuider crea un sistema de guía para controlar la generación de imágenes utilizando condicionamiento negativo perpendicular. Toma entradas de condicionamiento positivo, negativo y vacío, y aplica un algoritmo de guía especializado para dirigir el proceso de generación. Este nodo está diseñado para fines de prueba y proporciona un control preciso sobre la fuerza de guía y la escala negativa.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `modelo` | MODEL | Sí | - | El modelo a utilizar para la generación de guía |
| `positivo` | CONDITIONING | Sí | - | El condicionamiento positivo que guía la generación hacia el contenido deseado |
| `negativo` | CONDITIONING | Sí | - | El condicionamiento negativo que guía la generación lejos del contenido no deseado |
| `condicionamiento_vacío` | CONDITIONING | Sí | - | El condicionamiento vacío o neutral utilizado como referencia base |
| `cfg` | FLOAT | No | 0.0 - 100.0 | La escala de guía libre de clasificador que controla qué tan fuerte influye el condicionamiento en la generación (valor por defecto: 8.0) |
| `escala_neg` | FLOAT | No | 0.0 - 100.0 | El factor de escala negativa que ajusta la fuerza del condicionamiento negativo (valor por defecto: 1.0) |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `guider` | GUIDER | Un sistema de guía configurado listo para usar en el pipeline de generación |
