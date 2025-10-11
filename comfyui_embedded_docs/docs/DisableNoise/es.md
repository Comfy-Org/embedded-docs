> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DisableNoise/es.md)

El nodo DisableNoise proporciona una configuración de ruido vacía que puede utilizarse para desactivar la generación de ruido en procesos de muestreo. Retorna un objeto de ruido especial que no contiene datos de ruido, permitiendo que otros nodos omitan operaciones relacionadas con ruido cuando están conectados a esta salida.

## Entradas

| Parámetro | Tipo de Datos | Obligatorio | Rango | Descripción |
|-----------|---------------|-------------|-------|-------------|
| *Sin parámetros de entrada* | - | - | - | Este nodo no requiere ningún parámetro de entrada. |

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|------------------|---------------|-------------|
| `NOISE` | NOISE | Retorna una configuración de ruido vacía que puede utilizarse para desactivar la generación de ruido en procesos de muestreo. |