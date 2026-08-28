# MétodoLatenteReferenciaMúltipleFluxKontext

El nodo FluxKontextMultiReferenceLatentMethod modifica los datos de condicionamiento al establecer un método específico de latentes de referencia. Agrega el método seleccionado a la entrada `conditioning`, lo que afecta la forma en que se procesan los latentes de referencia en los pasos posteriores de generación. Este nodo está marcado como experimental y forma parte del sistema de condicionamiento de Flux.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `acondicionamiento` | Los datos de condicionamiento que se modificarán con el método de latentes de referencia | CONDITIONING | Sí | - |
| `método_latentes_referencia` | El método que se utilizará para el procesamiento de los latentes de referencia. Si se selecciona "uxo" o "uso", se convertirá a "uxo". Este parámetro está marcado como avanzado. | COMBO | Sí | `"offset"`<br>`"index"`<br>`"uxo/uno"`<br>`"index_timestep_zero"` |

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `conditioning` | Los datos de condicionamiento modificados con el método de latentes de referencia aplicado | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextMultiReferenceLatentMethod/es.md)

---
**Source fingerprint (SHA-256):** `cbe069d0c9f8adbf7f8c909b1cd644d9cd3730e934f0e5856213ff06fa8ecc56`
