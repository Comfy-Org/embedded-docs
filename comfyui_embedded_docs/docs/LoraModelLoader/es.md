# Cargar Modelo LoRA

El nodo `LoraModelLoader` aplica pesos LoRA (Adaptación de Bajo Rango) entrenados a un modelo de difusión. Modifica el modelo base cargando pesos LoRA desde un modelo LoRA entrenado y ajustando su fuerza de influencia. Esto permite personalizar el comportamiento de los modelos de difusión sin necesidad de reentrenarlos desde cero.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `model` | El modelo de difusión al que se le aplicará el LoRA. | MODEL | Sí | - |
| `lora` | El modelo LoRA que se aplicará al modelo de difusión. | LORA_MODEL | Sí | - |
| `strength_model` | Qué tan fuertemente modificar el modelo de difusión. Este valor puede ser negativo (predeterminado: 1.0). | FLOAT | Sí | -100.0 a 100.0 |
| `bypass` | Cuando está habilitado, aplica LoRA en modo bypass sin modificar los pesos del modelo base. Útil para el entrenamiento y cuando los pesos del modelo están descargados (predeterminado: False). | BOOLEAN | Sí | True o False |

**Nota:** Cuando `strength_model` se establece en 0, el nodo devuelve el modelo original sin aplicar ninguna modificación LoRA.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `model` | El modelo de difusión modificado. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraModelLoader/es.md)

---
**Source fingerprint (SHA-256):** `81eb2a9b0376fe7453f6e7e422414472e80a3d1b92bb6874b91df6de8aed0d9a`
