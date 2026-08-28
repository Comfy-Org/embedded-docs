# Cargar LoRA (Bypass) (Para depuración)

El nodo LoraLoaderBypass aplica una LoRA (Adaptación de Bajo Rango) a un modelo de difusión y a un modelo CLIP en un modo especial de «bypass». A diferencia de un cargador de LoRA estándar, este método no modifica permanentemente los pesos del modelo base. En su lugar, calcula la salida añadiendo el efecto de la LoRA al paso hacia adelante normal del modelo, lo cual es útil para el entrenamiento o cuando se trabaja con modelos cuyos pesos se han descargado.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo de difusión al que se aplicará la LoRA. | MODEL | Sí | - |
| `clip` | El modelo CLIP al que se aplicará la LoRA. | CLIP | Sí | - |
| `lora_name` | El nombre de la LoRA. Los archivos LoRA disponibles se cargan desde la carpeta `loras`. | COMBO | Sí | Lista de archivos LoRA disponibles |
| `strength_model` | Cuánto modificar el modelo de difusión. Este valor puede ser negativo (por defecto: 1.0). | FLOAT | Sí | -100.0 a 100.0 (paso: 0.01) |
| `strength_clip` | Cuánto modificar el modelo CLIP. Este valor puede ser negativo (por defecto: 1.0). | FLOAT | Sí | -100.0 a 100.0 (paso: 0.01) |

**Nota:** Si tanto `strength_model` como `strength_clip` se establecen en 0, el nodo devuelve las entradas `model` y `clip` originales sin procesar.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `MODEL` | El modelo de difusión modificado. | MODEL |
| `CLIP` | El modelo CLIP modificado. | CLIP |

**Nota:** Este nodo está marcado como experimental.

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderBypass/es.md)

---
**Source fingerprint (SHA-256):** `025f0638a6690a53b1a6c4548dac24fb7e7f26e04ff4b1c88d29b061430037a8`
