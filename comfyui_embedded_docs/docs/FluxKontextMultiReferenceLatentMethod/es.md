> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextMultiReferenceLatentMethod/es.md)

El nodo `FluxKontextMultiReferenceLatentMethod` modifica los datos de condicionamiento estableciendo un método específico de latentes de referencia. Anexa el método seleccionado a la entrada de condicionamiento, lo que afecta cómo se procesan los latentes de referencia en pasos posteriores de generación. Este nodo está marcado como experimental y forma parte del sistema de condicionamiento Flux.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|--------------|-------------|-------|-------------|
| `conditioning` | CONDITIONING | Sí | - | Los datos de condicionamiento que se modificarán con el método de latentes de referencia |
| `reference_latents_method` | STRING | Sí | `"offset"`<br>`"index"`<br>`"uxo/uno"`<br>`"index_timestep_zero"` | El método a utilizar para el procesamiento de latentes de referencia. Si se selecciona "uxo" o "uso", se convertirá a "uxo". Este parámetro está marcado como avanzado. |

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|------------------|--------------|-------------|
| `conditioning` | CONDITIONING | Los datos de condicionamiento modificados con el método de latentes de referencia aplicado |

---
**Source fingerprint (SHA-256):** `9d39a8fee08ae347a745b20b3dc39051ee2f4645392e769247ae32be35491048`
