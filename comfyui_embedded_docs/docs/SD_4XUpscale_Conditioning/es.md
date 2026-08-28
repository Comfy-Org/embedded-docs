# SD_4XUpscale_Conditioning

El nodo SD_4XUpscale_Conditioning prepara datos de condicionamiento para ampliar imágenes mediante modelos de difusión. Toma imágenes de entrada y datos de condicionamiento, luego aplica escalado y aumento de ruido para crear un condicionamiento modificado que guía el proceso de ampliación. El nodo genera tanto condicionamiento positivo como negativo, junto con representaciones latentes para las dimensiones ampliadas.

## Entradas

| Parámetro | Descripción | Tipo de datos | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `imágenes` | Imágenes de entrada que se van a ampliar | IMAGE | Sí | - |
| `positivo` | Datos de condicionamiento positivo que guían la generación hacia el contenido deseado | CONDITIONING | Sí | - |
| `negativo` | Datos de condicionamiento negativo que apartan la generación del contenido no deseado | CONDITIONING | Sí | - |
| `relación_escala` | Factor de escala aplicado a las imágenes de entrada (por defecto: 4.0) | FLOAT | No | 0.0 - 10.0 |
| `aumento_ruido` | Cantidad de ruido que se añade durante el proceso de ampliación (por defecto: 0.0) | FLOAT | No | 0.0 - 1.0 |

Nota: `noise_augmentation` es un parámetro avanzado, que se muestra en la interfaz del nodo bajo la opción "Avanzado".

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `positivo` | Condicionamiento positivo modificado con información de ampliación aplicada | CONDITIONING |
| `negativo` | Condicionamiento negativo modificado con información de ampliación aplicada | CONDITIONING |
| `latente` | Representación latente vacía que coincide con las dimensiones ampliadas | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SD_4XUpscale_Conditioning/es.md)

---
**Source fingerprint (SHA-256):** `f215e890bd86f42d4da9c6f575fc92e65844e2e2056c5610310d8089e5d61902`
