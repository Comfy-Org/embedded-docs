> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageToImageNode/es.md)

Este nodo modifica una imagen existente basándose en un texto descriptivo y un parámetro de intensidad. Utiliza la API de Recraft para transformar la imagen de entrada de acuerdo con la descripción proporcionada, manteniendo cierto grado de similitud con la imagen original según la configuración de intensidad.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen de entrada que será modificada |
| `prompt` | STRING | Sí | - | Texto descriptivo para la generación de la imagen (valor por defecto: "") |
| `n` | INT | Sí | 1-6 | El número de imágenes a generar (valor por defecto: 1) |
| `strength` | FLOAT | Sí | 0.0-1.0 | Define la diferencia con la imagen original, debe estar en [0, 1], donde 0 significa casi idéntica y 1 significa similitud mínima (valor por defecto: 0.5) |
| `seed` | INT | Sí | 0-18446744073709551615 | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales son no deterministas independientemente de la semilla (valor por defecto: 0) |
| `recraft_style` | STYLEV3 | No | - | Selección opcional de estilo para la generación de la imagen |
| `negative_prompt` | STRING | No | - | Una descripción de texto opcional de elementos no deseados en una imagen (valor por defecto: "") |
| `recraft_controls` | CONTROLS | No | - | Controles adicionales opcionales sobre la generación a través del nodo Recraft Controls |

**Nota:** El parámetro `seed` solo activa la re-ejecución del nodo pero no garantiza resultados deterministas. El parámetro de intensidad se redondea internamente a 2 decimales.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `image` | IMAGE | La(s) imagen(es) generada(s) basada(s) en la imagen de entrada y el texto descriptivo |