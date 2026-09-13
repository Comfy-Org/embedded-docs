# MétodoLatenteReferenciaMúltipleFluxKontext

El nodo FluxKontextMultiReferenceLatentMethod actualiza los datos de condicionamiento almacenando en ellos un método de latentes de referencia elegido. El método almacenado se utiliza luego cuando se procesan los latentes de referencia en pasos de generación posteriores. Este nodo está marcado como experimental y pertenece al sistema de condicionamiento Flux.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `acondicionamiento` | Los datos de condicionamiento que se modificarán con el método de latentes de referencia | CONDITIONING | Sí | - |
| `método_latentes_referencia` | El método utilizado para el procesamiento de latentes de referencia. Si se selecciona un valor que contiene "uxo" o "uso", se convierte a "uxo" antes de almacenarse. Este parámetro está marcado como avanzado. | COMBO | Sí | `"offset"`<br>`"index"`<br>`"uxo/uno"`<br>`"index_timestep_zero"` |

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `conditioning` | Los datos de condicionamiento modificados con el método de latentes de referencia aplicado | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextMultiReferenceLatentMethod/es.md)

---
**Source fingerprint (SHA-256):** `cbe069d0c9f8adbf7f8c909b1cd644d9cd3730e934f0e5856213ff06fa8ecc56`
