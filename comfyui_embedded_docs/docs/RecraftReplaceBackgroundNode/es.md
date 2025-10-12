> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftReplaceBackgroundNode/es.md)

Reemplaza el fondo de una imagen basándose en el texto proporcionado. Este nodo utiliza la API de Recraft para generar nuevos fondos para tus imágenes según tu descripción textual, permitiéndote transformar completamente el fondo mientras mantienes intacto el sujeto principal.

## Entradas

| Parámetro | Tipo de Dato | Requerido | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `imagen` | IMAGE | Sí | - | La imagen de entrada a procesar |
| `prompt` | STRING | Sí | - | Texto descriptivo para la generación de la imagen (valor por defecto: vacío) |
| `n` | INT | Sí | 1-6 | El número de imágenes a generar (valor por defecto: 1) |
| `semilla` | INT | Sí | 0-18446744073709551615 | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales son no deterministas independientemente de la semilla (valor por defecto: 0) |
| `recraft_style` | STYLEV3 | No | - | Selección opcional de estilo para el fondo generado |
| `negative_prompt` | STRING | No | - | Una descripción textual opcional de elementos no deseados en una imagen (valor por defecto: vacío) |

**Nota:** El parámetro `seed` controla cuándo el nodo se vuelve a ejecutar pero no garantiza resultados deterministas debido a la naturaleza de la API externa.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | La(s) imagen(es) generada(s) con el fondo reemplazado |