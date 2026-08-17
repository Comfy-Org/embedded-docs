# Seleccionar Dispositivo del Modelo

El nodo SelectModelDevice te permite elegir en qué dispositivo (CPU o una GPU específica) se ejecuta un modelo de difusión. Según la opción seleccionada, restaura el dispositivo original del cargador, fija el modelo en la CPU o lo mueve a una GPU específica, y gestiona automáticamente los conflictos con otros nodos de múltiples GPU.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `model` | El modelo de difusión que se colocará en un dispositivo específico. | MODEL | Sí |  |
| `device` | El dispositivo de destino para el modelo. Las opciones se generan dinámicamente según las GPU disponibles. (predeterminado: "default") | COMBO | Sí | `"default"`<br>`"cpu"`<br>`"gpu:N"` para cada GPU disponible (p. ej. `"gpu:0"`, `"gpu:1"`, ...) |

**Detalles de los parámetros:**
- `"default"`: Restaura el dispositivo asignado por el cargador del modelo, incluso si un nodo SelectModelDevice anterior lo cambió.
- `"cpu"`: Fija tanto el dispositivo de carga como el de descarga a la CPU.
- `"gpu:N"`: Fija el dispositivo de carga a la N-ésima GPU disponible (p. ej., `"gpu:0"` para la primera GPU). El dispositivo de descarga se restaura a la elección original del cargador.

**Notas importantes:**
- Los valores desconocidos `"gpu:N"` se aceptan en el momento de la validación para que los flujos de trabajo portables no fallen en máquinas con menos GPU. En tiempo de ejecución, un dispositivo no disponible hace que el modelo se pase sin cambios con un mensaje de registro.
- Si el dispositivo solicitado no existe en la máquina actual (p. ej., un flujo de trabajo creado en una máquina con 2 GPU se abre en una máquina con 1 GPU), el nodo pasa el modelo sin cambios y registra un mensaje en lugar de fallar.
- Si el modelo ya se encuentra en el dispositivo solicitado, el nodo toma un camino rápido y no vuelve a cargar el modelo.
- Cuando el dispositivo solicitado difiere del actual, se crea un modelo nuevo utilizando la fábrica de recarga del cargador, por lo que el modelo devuelto tiene pesos independientes en el nuevo dispositivo. Los cargadores que no admiten esto hacen que el nodo pase el modelo sin cambios con una advertencia.
- Si el flujo de trabajo ya tiene aplicado MultiGPU CFG Split y la GPU elegida coincide con uno de los clones multigpu existentes, ese clon se elimina para que dos parcheadores no terminen vinculados al mismo dispositivo.
- Colocar este nodo *después* de un nodo que ya ha consumido el modelo (p. ej., un KSampler) no se recomienda, ya que cualquier estado modificado por el nodo anterior se observará si el dispositivo coincide con el original.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `model` | El modelo de difusión, ahora colocado en el dispositivo seleccionado. Si el dispositivo era inválido o no estaba disponible, el modelo se pasa sin cambios. | MODEL |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelectModelDevice/es.md)

---
**Source fingerprint (SHA-256):** `d02a8bd9612861cf696f03969fe693088351de5a72ccbd4c1aed405b104eb71e`
