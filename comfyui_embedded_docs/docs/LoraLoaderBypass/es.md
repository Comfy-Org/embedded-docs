# Cargar LoRA (Bypass) (Para depuración)

El nodo `LoraLoaderBypass` aplica un LoRA (Adaptación de Bajo Rango) a un modelo de difusión y a un modelo CLIP en un modo especial de bypass. A diferencia de un cargador de LoRA estándar, no modifica permanentemente los pesos del modelo base. En su lugar, añade el efecto del LoRA al paso forward normal del modelo, lo que resulta útil para entrenamiento o para trabajar con modelos cuyos pesos están descargados.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo de difusión al que se le aplicará el LoRA. | MODEL | Sí | N/A |
| `clip` | El modelo CLIP al que se le aplicará el LoRA. | CLIP | Sí | N/A |
| `lora_name` | El nombre del archivo LoRA que se aplicará. Las opciones se cargan desde la carpeta `loras`. | COMBO | Sí | Lista de archivos LoRA disponibles |
| `strength_model` | La intensidad con la que se modifica el modelo de difusión. Este valor puede ser negativo (por defecto: 1.0). | FLOAT | Sí | -100.0 a 100.0 |
| `strength_clip` | La intensidad con la que se modifica el modelo CLIP. Este valor puede ser negativo (por defecto: 1.0). | FLOAT | Sí | -100.0 a 100.0 |

**Nota:** Si tanto `strength_model` como `strength_clip` se establecen en 0, el nodo devuelve las entradas `model` y `clip` originales y sin modificar, sin procesamiento.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `MODEL` | El modelo de difusión con el LoRA aplicado en modo bypass. | MODEL |
| `CLIP` | El modelo CLIP con el LoRA aplicado en modo bypass. | CLIP |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderBypass/es.md)

---
**Source fingerprint (SHA-256):** `025f0638a6690a53b1a6c4548dac24fb7e7f26e04ff4b1c88d29b061430037a8`
