# LTXVConditioning

El nodo LTXVConditioning añade información de velocidad de fotogramas a las entradas de condicionamiento tanto positivas como negativas para modelos de generación de video. Toma datos de condicionamiento existentes y aplica el valor de velocidad de fotogramas especificado a ambos conjuntos de condicionamiento, haciéndolos adecuados para el procesamiento de modelos de video.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `positivo` | La entrada de condicionamiento positivo que recibirá la información de velocidad de fotogramas | CONDITIONING | Sí | - |
| `negativo` | La entrada de condicionamiento negativo que recibirá la información de velocidad de fotogramas | CONDITIONING | Sí | - |
| `tasa_fotogramas` | El valor de velocidad de fotogramas a aplicar a ambos conjuntos de condicionamiento (predeterminado: 25.0) | FLOAT | Sí | 0.0 - 1000.0 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `positivo` | El condicionamiento positivo con la información de velocidad de fotogramas aplicada | CONDITIONING |
| `negativo` | El condicionamiento negativo con la información de velocidad de fotogramas aplicada | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConditioning/es.md)

---
**Source fingerprint (SHA-256):** `e8c18b73eb009c1b3ebcc2cb8be3dee4e065d75908607a5cf15d41f89963ee09`
