> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKVCache/es.md)

El nodo Flux KV Cache aplica una optimización de caché de clave-valor (KV) a los modelos de la familia Flux. Esta optimización está diseñada específicamente para mejorar el rendimiento al utilizar imágenes de referencia, almacenando en caché ciertos cálculos, lo que puede acelerar el proceso de generación.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sí | | El modelo sobre el cual aplicar la caché KV. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | El modelo modificado con la caché KV habilitada. |