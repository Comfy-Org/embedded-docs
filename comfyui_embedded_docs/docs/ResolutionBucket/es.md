# Agrupación por resolución

Este nodo organiza una lista de imágenes latentes y sus datos de condicionamiento correspondientes según su resolución. Agrupa los elementos que comparten la misma altura y ancho, creando lotes separados para cada resolución única. Este proceso es útil para preparar datos para un entrenamiento eficiente, ya que permite a los modelos procesar múltiples elementos del mismo tamaño juntos.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
| --- | --- | --- | --- | --- |
| `latentes` | Lista de dicts latentes para agrupar por resolución. | LATENT | Sí | N/A |
| `condicionamiento` | Lista de listas de condicionamiento (debe coincidir con la longitud de latents). | CONDITIONING | Sí | N/A |

**Nota:** El número de elementos en la lista `latents` debe coincidir exactamente con el número de elementos en la lista `conditioning`. Si los conteos no coinciden, el nodo genera un error. Cada diccionario latente puede contener un lote de muestras, y la lista de condicionamiento correspondiente debe contener un número igual de elementos de condicionamiento para ese lote. Las muestras latentes pueden tener una forma de (B, C, H, W) para imágenes o (B, T, C, H, W) para videos; el nodo las agrupa solo por altura y ancho.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
| --- | --- | --- |
| `latentes` | Lista de dicts latentes agrupados en lotes, uno por grupo de resolución. | LATENT |
| `condicionamiento` | Lista de listas de condicionamiento, una por grupo de resolución. | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionBucket/es.md)

---
**Source fingerprint (SHA-256):** `11687f9916895136c7c5b8146cd7519cbf6c296720e453bac52fe4da237403cd`
