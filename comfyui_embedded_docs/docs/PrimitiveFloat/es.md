> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveFloat/es.md)

El nodo PrimitiveFloat crea un valor numérico de punto flotante que puede utilizarse en su flujo de trabajo. Toma una única entrada numérica y emite ese mismo valor, permitiéndole definir y pasar valores float entre diferentes nodos en su pipeline de ComfyUI.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `valor` | FLOAT | Sí | -sys.maxsize a sys.maxsize | El valor numérico de punto flotante a emitir |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `output` | FLOAT | El valor numérico de punto flotante de entrada |
