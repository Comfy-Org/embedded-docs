El nodo `SD_4XUpscale_Conditioning` prepara datos de condicionamiento para escalar imágenes mediante modelos de difusión. Toma imágenes de entrada y datos de condicionamiento, luego aplica escalado y aumento de ruido para crear un condicionamiento modificado que guía el proceso de escalado. El nodo genera tanto condicionamiento positivo como negativo, junto con representaciones latentes para las dimensiones escaladas.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `imágenes` | Imágenes de entrada que se escalarán | IMAGE | Sí | - |
| `positivo` | Datos de condicionamiento positivo que guían la generación hacia el contenido deseado | CONDITIONING | Sí | - |
| `negativo` | Datos de condicionamiento negativo que alejan la generación del contenido no deseado | CONDITIONING | Sí | - |
| `relación_escala` | Factor de escalado aplicado a las imágenes de entrada (predeterminado: 4.0) | FLOAT | No | 0.0 - 10.0 |
| `aumento_ruido` | Cantidad de ruido a añadir durante el proceso de escalado (predeterminado: 0.0) | FLOAT | No | 0.0 - 1.0 |

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `negativo` | Condicionamiento positivo modificado con información de escalado aplicada | CONDITIONING |
| `latente` | Condicionamiento negativo modificado con información de escalado aplicada | CONDITIONING |
| `latent` | Representación latente vacía que coincide con las dimensiones escaladas | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SD_4XUpscale_Conditioning/es.md)

---
**Source fingerprint (SHA-256):** `ede1ea8f5a95e7f9e52070b5132a4ed3e87f92230d14a74b9d713f547c74d785`
