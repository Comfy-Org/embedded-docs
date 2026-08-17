# EstablecerTipoDeRedDeControlUnion

El nodo SetUnionControlNetType le permite establecer el tipo de control de una red de control utilizada para condicionamiento. Toma una red de control existente, crea una copia modificada de la misma y almacena el tipo de control seleccionado en esa copia, de modo que el original permanezca sin cambios.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `control_net` | La red de control a copiar y modificar con el tipo de control seleccionado | CONTROL_NET | Sí | - |
| `type` | El tipo de control a aplicar a la red de control copiada. Seleccione "auto" para dejar el tipo de control sin establecer, o elija un tipo específico de entre los tipos de red de control unión disponibles (predeterminado: "auto") | COMBO | Sí | `"auto"`<br>`"openpose"`<br>`"depth"`<br>`"hed/pidi/scribble/ted"`<br>`"canny/softedge"`<br>`"normal/bms"`<br>`"seg"`<br>`"inpaint"`<br>`"lineart"`<br>`"s4"`<br>`"tile/color"`<br>`"blur"`<br>`"identity"` |

Nota: Cuando `type` es "auto", la lista de tipos de control en la red de control copiada se vacía. Cuando se selecciona un tipo específico, la red de control copiada almacena el número de tipo correspondiente.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `control_net` | La copia modificada de la red de control con el tipo de control seleccionado aplicado | CONTROL_NET |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetUnionControlNetType/es.md)

---
**Source fingerprint (SHA-256):** `db4b1a3cebafcff2be3172faa09cecbd5e19331376491c491cbe359013ed3da3`
