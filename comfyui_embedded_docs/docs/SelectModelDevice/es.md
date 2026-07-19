# Seleccionar Dispositivo del Modelo

## Descripción general

El nodo SelectModelDevice permite elegir manualmente en qué dispositivo (CPU o una GPU específica) se ejecuta un modelo de difusión. Puede mover un modelo a un dispositivo diferente y maneja conflictos con otros nodos multi-GPU automáticamente.

## Entradas

| Parámetro | Descripción | Tipo de dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo de difusión que se colocará en un dispositivo específico. | MODEL | Sí |  |
| `device` | El dispositivo de destino para el modelo. Las opciones se generan dinámicamente según las GPU disponibles. (predeterminado: "default") | COMBO | Sí | `"default"`<br>`"cpu"`<br>`"gpu:0"`<br>`"gpu:1"`<br>`"gpu:2"`<br>`"gpu:3"`<br>`"gpu:4"`<br>`"gpu:5"`<br>`"gpu:6"`<br>`"gpu:7"` |

**Detalles de parámetros:**
- `"default"`: Restaura el dispositivo asignado por el cargador de modelos, incluso si un nodo SelectModelDevice anterior lo cambió.
- `"cpu"`: Fija tanto el dispositivo de carga como el de descarga a la CPU.
- `"gpu:N"`: Fija el dispositivo de carga a la N-ésima GPU disponible (ej., `"gpu:0"` para la primera GPU). El dispositivo de descarga se restaura a la elección original del cargador.

**Notas importantes:**
- Si el dispositivo solicitado no existe en la máquina actual (ej., un flujo de trabajo creado en una máquina con 2 GPU se abre en una máquina con 1 GPU), el nodo pasará el modelo sin cambios y registrará un mensaje en lugar de fallar.
- Si el modelo ya está en el dispositivo solicitado, el nodo toma una ruta rápida y no recarga el modelo.
- No se recomienda colocar este nodo *después* de un nodo que ya ha consumido el modelo (ej., un KSampler), ya que cualquier cambio de estado realizado por el nodo anterior se observará si el dispositivo coincide con el original.

## Salidas

| Nombre de salida | Descripción | Tipo de dato |
| --- | --- | --- |
| `model` | El modelo de difusión, ahora colocado en el dispositivo seleccionado. Si el dispositivo no era válido o no estaba disponible, el modelo se pasa sin cambios. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelectModelDevice/es.md)

---
**Source fingerprint (SHA-256):** `02841975f123cc8ae8152ea86f1798e0e7e68255ecd11e04271da886b75eb0fd`
