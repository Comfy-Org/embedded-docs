> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionBucket/es.md)

Este nodo organiza una lista de imágenes latentes y sus datos de condicionamiento correspondientes por su resolución. Agrupa elementos que comparten la misma altura y ancho, creando lotes separados para cada resolución única. Este proceso es útil para preparar datos para un entrenamiento eficiente, ya que permite a los modelos procesar múltiples elementos del mismo tamaño juntos.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `latents` | LATENT | Sí | N/A | Lista de diccionarios latentes para agrupar por resolución. |
| `conditioning` | CONDITIONING | Sí | N/A | Lista de listas de condicionamiento (debe coincidir con la longitud de latents). |

**Nota:** El número de elementos en la lista `latents` debe coincidir exactamente con el número de elementos en la lista `conditioning`. Cada diccionario latente puede contener un lote de muestras, y la lista de condicionamiento correspondiente debe contener un número coincidente de elementos de condicionamiento para ese lote.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `latents` | LATENT | Lista de diccionarios latentes agrupados en lotes, uno por grupo de resolución. |
| `conditioning` | CONDITIONING | Lista de listas de condicionamiento, una por grupo de resolución. |
