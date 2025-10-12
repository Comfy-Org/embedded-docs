> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetUnionControlNetType/es.md)

El nodo SetUnionControlNetType permite especificar el tipo de red de control a utilizar para el condicionamiento. Toma una red de control existente y establece su tipo de control según su selección, creando una copia modificada de la red de control con la configuración de tipo especificada.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `controlnet` | CONTROL_NET | Sí | - | La red de control a modificar con una nueva configuración de tipo |
| `tipo` | STRING | Sí | `"auto"`<br>Todas las claves disponibles de UNION_CONTROLNET_TYPES | El tipo de red de control a aplicar. Use "auto" para detección automática de tipo o seleccione un tipo específico de red de control de las opciones disponibles |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `controlnet` | CONTROL_NET | La red de control modificada con la configuración de tipo especificada aplicada |