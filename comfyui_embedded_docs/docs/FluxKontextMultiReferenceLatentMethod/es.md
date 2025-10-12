> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextMultiReferenceLatentMethod/es.md)

El nodo FluxKontextMultiReferenceLatentMethod modifica los datos de condicionamiento estableciendo un método específico para los latentes de referencia. Añade el método seleccionado a la entrada de condicionamiento, lo que afecta cómo se procesan los latentes de referencia en los pasos subsiguientes de generación. Este nodo está marcado como experimental y forma parte del sistema de condicionamiento Flux.

## Entradas

| Parámetro | Tipo de Datos | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `conditioning` | CONDITIONING | Sí | - | Los datos de condicionamiento que se modificarán con el método de latentes de referencia |
| `reference_latents_method` | STRING | Sí | `"offset"`<br>`"index"`<br>`"uxo/uno"` | El método a utilizar para el procesamiento de latentes de referencia. Si se selecciona "uxo" o "uso", se convertirá a "uxo" |

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|-------------|-----------|-------------|
| `conditioning` | CONDITIONING | Los datos de condicionamiento modificados con el método de latentes de referencia aplicado |
