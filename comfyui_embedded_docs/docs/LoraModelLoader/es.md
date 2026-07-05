# Cargar Modelo LoRA

El nodo LoraModelLoader aplica pesos de LoRA (Adaptación de Bajo Rango) entrenados a un modelo de difusión. Modifica el modelo base cargando pesos de LoRA desde un modelo entrenado y ajustando su intensidad de influencia. Esto permite personalizar el comportamiento de los modelos de difusión sin necesidad de reentrenarlos desde cero.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `modelo` | El modelo de difusión al que se aplicará el LoRA. | MODEL | Sí | - |
| `lora` | El modelo LoRA que se aplicará al modelo de difusión. | LORA_MODEL | Sí | - |
| `fuerza_modelo` | La intensidad con la que modificar el modelo de difusión. Este valor puede ser negativo (predeterminado: 1.0). | FLOAT | Sí | -100.0 a 100.0 |
| `bypass` | Cuando está habilitado, aplica LoRA en modo de omisión sin modificar los pesos del modelo base. Útil para entrenamiento y cuando los pesos del modelo están descargados (predeterminado: Falso). | BOOLEAN | Sí | Verdadero o Falso |

**Nota:** Cuando `strength_model` se establece en 0, el nodo devuelve el modelo original sin aplicar ninguna modificación de LoRA.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `model` | El modelo de difusión modificado con los pesos de LoRA aplicados. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraModelLoader/es.md)

---
**Source fingerprint (SHA-256):** `82afa7dbbc990f1a9f202f920aaf8fad7fe69dc35e75ed8a95eb63c9dec74961`
