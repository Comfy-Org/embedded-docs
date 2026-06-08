El nodo LoraLoaderBypass aplica un LoRA (Adaptación de Bajo Rango) a un modelo de difusión y a un modelo CLIP en un modo especial de "bypass". A diferencia de un cargador LoRA estándar, este método no modifica permanentemente los pesos del modelo base. En su lugar, calcula la salida añadiendo el efecto del LoRA al paso forward normal del modelo, lo cual es útil para entrenamiento o cuando se trabaja con modelos que tienen sus pesos descargados.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo de difusión al que se aplicará el LoRA. | MODEL | Sí | - |
| `clip` | El modelo CLIP al que se aplicará el LoRA. | CLIP | Sí | - |
| `lora_name` | El nombre del archivo LoRA a aplicar. Las opciones se cargan desde la carpeta `loras`. | COMBO | Sí | *Lista de archivos LoRA disponibles* |
| `strength_model` | La intensidad con la que modificar el modelo de difusión. Este valor puede ser negativo (predeterminado: 1.0). | FLOAT | Sí | -100.0 a 100.0 |
| `strength_clip` | La intensidad con la que modificar el modelo CLIP. Este valor puede ser negativo (predeterminado: 1.0). | FLOAT | Sí | -100.0 a 100.0 |

**Nota:** Si tanto `strength_model` como `strength_clip` se establecen en 0, el nodo devolverá las entradas originales `model` y `clip` sin modificar, sin procesamiento.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `MODEL` | El modelo de difusión con el LoRA aplicado en modo bypass. | MODEL |
| `CLIP` | El modelo CLIP con el LoRA aplicado en modo bypass. | CLIP |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderBypass/es.md)

---
**Source fingerprint (SHA-256):** `2642f4ed98457e5fd08e2103ffb9f2c02f11326590aadf0636fb7db51f484815`
