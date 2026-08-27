# Seleccionar Dispositivo del Modelo

## Descripción general

El nodo SelectModelDevice permite elegir manualmente en qué dispositivo (CPU o una GPU específica) se ejecuta un modelo de difusión. Puede mover un modelo a un dispositivo diferente y gestiona automáticamente los conflictos con otros nodos de múltiples GPU.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo de difusión que se colocará en un dispositivo específico. | MODEL | Sí |  |
| `device` | El dispositivo de destino para el modelo. Las opciones se generan dinámicamente según las GPU disponibles. (predeterminado: `"default"`) | COMBO | Sí | `"default"`<br>`"cpu"`<br>`"gpu:0"`<br>`"gpu:1"`<br>... (una entrada `"gpu:N"` por cada GPU detectada) |

**Detalles de los parámetros:**
- `"default"`: Restablece el dispositivo asignado por el cargador de modelos, incluso si un nodo SelectModelDevice anterior lo cambió.
- `"cpu"`: Fija tanto el dispositivo de carga como el de descarga en la CPU.
- `"gpu:N"`: Fija el dispositivo de carga a la enésima GPU disponible (p. ej., `"gpu:0"` para la primera GPU). El dispositivo de descarga se restablece a la elección original del cargador.

**Notas importantes:**
- Si el dispositivo solicitado no existe en la máquina actual (p. ej., un flujo de trabajo creado en una máquina con 2 GPU se abre en una máquina con 1 GPU), el nodo pasará el modelo sin cambios y registrará un mensaje en lugar de fallar.
- Si el modelo ya está en el dispositivo solicitado, el nodo toma una ruta rápida y no vuelve a cargar el modelo.
- Si el cargador de modelos no es compatible con múltiples GPU (sin fábrica de recarga), el nodo pasa el modelo sin cambios y registra una advertencia.
- Cuando un clon de MultiGPU CFG Split ya ocupa el dispositivo seleccionado, ese clon se poda para que dos modelos no queden vinculados al mismo dispositivo.
- Cuando se selecciona un dispositivo específico, el nodo también ajusta el dtype de cómputo del modelo a uno compatible con ese dispositivo.
- Colocar este nodo *después* de un nodo que ya ha consumido el modelo (p. ej., un KSampler) no es recomendable, ya que cualquier estado modificado por el nodo anterior se observará si el dispositivo coincide con el original.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | El modelo de difusión, ahora colocado en el dispositivo seleccionado. Si el dispositivo no era válido o no estaba disponible, el modelo se pasa sin cambios. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelectModelDevice/es.md)

---
**Source fingerprint (SHA-256):** `d02a8bd9612861cf696f03969fe693088351de5a72ccbd4c1aed405b104eb71e`
