# EstablecerTipoDeRedDeControlUnion

El nodo SetUnionControlNetType le permite elegir qué tipo de control utiliza una red de control. Toma una red de control existente y crea una copia modificada con el tipo de control seleccionado, dejando la red de control original sin cambios. Cuando se selecciona "auto", el tipo de control almacenado se limpia para que el tipo pueda detectarse automáticamente.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `controlnet` | La red de control a modificar con una nueva configuración de tipo | CONTROL_NET | Sí | - |
| `tipo` | El tipo de red de control a aplicar. Use "auto" para la detección automática de tipo o seleccione un tipo de red de control específico de las opciones disponibles (predeterminado: "auto") | COMBO | Sí | `"auto"`<br>`"openpose"`<br>`"depth"`<br>`"hed/pidi/softedge"`<br>`"canny"`<br>`"scribble"`<br>`"seg"`<br>`"tile"`<br>`"inpaint"`<br>`"lineart"`<br>`"blur"`<br>`"mlsd"`<br>`"normalbae"`<br>`"mask"` |

Cuando `type` se establece en `"auto"`, el nodo limpia el tipo de control almacenado para que el tipo pueda detectarse automáticamente. Cuando se selecciona un tipo específico, el nodo almacena el tipo de control correspondiente en la red de control copiada.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `control_net` | La red de control modificada con la configuración de tipo especificada aplicada | CONTROL_NET |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetUnionControlNetType/es.md)

---
**Source fingerprint (SHA-256):** `db4b1a3cebafcff2be3172faa09cecbd5e19331376491c491cbe359013ed3da3`
