Este nodo organiza una lista de imágenes latentes y sus datos de condicionamiento correspondientes según su resolución. Agrupa elementos que comparten la misma altura y anchura, creando lotes separados para cada resolución única. Este proceso es útil para preparar datos para un entrenamiento eficiente, ya que permite que los modelos procesen múltiples elementos del mismo tamaño juntos.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `latentes` | Lista de diccionarios latentes para agrupar por resolución. | LATENT | Sí | N/A |
| `condicionamiento` | Lista de listas de condicionamiento (debe coincidir con la longitud de latentes). | CONDITIONING | Sí | N/A |

**Nota:** La cantidad de elementos en la lista `latents` debe coincidir exactamente con la cantidad de elementos en la lista `conditioning`. Cada diccionario latente puede contener un lote de muestras, y la lista de condicionamiento correspondiente debe contener una cantidad coincidente de elementos de condicionamiento para ese lote.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `condicionamiento` | Lista de diccionarios latentes agrupados en lotes, uno por grupo de resolución. | LATENT |
| `condicionamiento` | Lista de listas de condicionamiento, una por grupo de resolución. | CONDITIONING |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionBucket/es.md)

---
**Source fingerprint (SHA-256):** `2858de5f0827812002ca72ba5d7ce56411d1ef97e9a12a65fc4bea193a1a0ec0`
