# SD_4XUpscale_Conditioning

El nodo **SD_4XUpscale_Conditioning** prepara datos de condicionamiento para ampliar imágenes mediante modelos de difusión. Toma imágenes de entrada y datos de condicionamiento, y luego aplica escalado y aumento de ruido para crear un condicionamiento modificado que guía el proceso de ampliación. El nodo genera tanto condicionamiento positivo como negativo, junto con representaciones latentes para las dimensiones ampliadas.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `images` | Imágenes de entrada que se van a ampliar | IMAGE | Sí | - |
| `positive` | Datos de condicionamiento positivos que guían la generación hacia el contenido deseado | CONDITIONING | Sí | - |
| `negative` | Datos de condicionamiento negativos que alejan la generación del contenido no deseado | CONDITIONING | Sí | - |
| `scale_ratio` | Factor de escala aplicado a las imágenes de entrada (predeterminado: 4.0) | FLOAT | Sí | 0.0 - 10.0 |
| `noise_augmentation` | Cantidad de ruido a añadir durante el proceso de ampliación (predeterminado: 0.0) | FLOAT | Sí | 0.0 - 1.0 |

Las dimensiones ampliadas objetivo se calculan multiplicando las dimensiones de la imagen de entrada por `scale_ratio`. La imagen integrada en el condicionamiento y el latente de salida se crean a un cuarto de esas dimensiones objetivo.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `positive` | Condicionamiento positivo modificado con información de ampliación aplicada | CONDITIONING |
| `negative` | Condicionamiento negativo modificado con información de ampliación aplicada | CONDITIONING |
| `latent` | Representación latente vacía que coincide con las dimensiones ampliadas | LATENT |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SD_4XUpscale_Conditioning/es.md)

---
**Source fingerprint (SHA-256):** `f215e890bd86f42d4da9c6f575fc92e65844e2e2056c5610310d8089e5d61902`
