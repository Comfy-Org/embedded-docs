> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraModelLoader/es.md)

El nodo LoraModelLoader aplica pesos LoRA (Low-Rank Adaptation) entrenados a un modelo de difusión. Modifica el modelo base cargando pesos LoRA desde un modelo LoRA entrenado y ajustando su fuerza de influencia. Esto permite personalizar el comportamiento de los modelos de difusión sin necesidad de reentrenarlos desde cero.

## Entradas

| Parámetro | Tipo de Datos | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Sí | - | El modelo de difusión al que se aplicará el LoRA. |
| `lora` | LORA_MODEL | Sí | - | El modelo LoRA que se aplicará al modelo de difusión. |
| `strength_model` | FLOAT | Sí | -100.0 a 100.0 | Qué tan fuerte modificar el modelo de difusión. Este valor puede ser negativo (por defecto: 1.0). |

**Nota:** Cuando `strength_model` se establece en 0, el nodo devuelve el modelo original sin aplicar ninguna modificación LoRA.

## Salidas

| Nombre de Salida | Tipo de Datos | Descripción |
|-------------|-----------|-------------|
| `model` | MODEL | El modelo de difusión modificado con los pesos LoRA aplicados. |
