# Agrupación por resolución

Este nodo organiza una lista de latentes y sus datos de condicionamiento correspondientes según su resolución. Agrupa los elementos que comparten la misma altura y anchura, creando lotes separados para cada resolución única. Este proceso es útil para preparar datos para un entrenamiento eficiente, ya que permite a los modelos procesar múltiples elementos del mismo tamaño juntos.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `latents` | Lista de diccionarios de latentes para agrupar por resolución. | LATENT | Sí | N/A |
| `conditioning` | Lista de listas de condicionamiento (debe coincidir con la longitud de `latents`). | CONDITIONING | Sí | N/A |

**Nota:** El número de elementos en la lista `latents` debe coincidir exactamente con el número de elementos en la lista `conditioning`. Cada diccionario de latentes puede contener un lote de muestras, y la lista de condicionamiento correspondiente debe contener un número igual de elementos de condicionamiento para ese lote.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `latents` | Lista de diccionarios de latentes agrupados en lotes, uno por grupo de resolución. | LATENT |
| `conditioning` | Lista de listas de condicionamiento, una por grupo de resolución. | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionBucket/es.md)

---
**Source fingerprint (SHA-256):** `11687f9916895136c7c5b8146cd7519cbf6c296720e453bac52fe4da237403cd`
