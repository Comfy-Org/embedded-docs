> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Mahiro/es.md)

El nodo Mahiro modifica la función de guía para enfocarse más en la dirección del prompt positivo que en la diferencia entre prompts positivos y negativos. Crea un modelo parcheado que aplica un enfoque personalizado de escalado de guía utilizando la similitud coseno entre las salidas normalizadas condicionales e incondicionales del proceso de eliminación de ruido. Este nodo experimental ayuda a dirigir la generación más fuertemente hacia la dirección prevista del prompt positivo.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sí | | El modelo que será parcheado con la función de guía modificada |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `patched_model` | MODEL | El modelo modificado con la función de guía Mahiro aplicada |