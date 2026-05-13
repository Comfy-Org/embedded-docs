> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftReplaceBackgroundNode/es.md)

Reemplazar el fondo de una imagen, basado en el mensaje proporcionado. Este nodo utiliza la API de Recraft para generar nuevos fondos para tus imágenes según tu descripción textual, permitiéndote transformar completamente el fondo mientras mantienes intacto el sujeto principal.

## Entradas

| Parámetro | Tipo de Dato | Obligatorio | Rango | Descripción |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Sí | - | La imagen de entrada a procesar |
| `prompt` | STRING | Sí | - | Mensaje para la generación de la imagen (predeterminado: vacío) |
| `n` | INT | Sí | 1-6 | El número de imágenes a generar (predeterminado: 1) |
| `seed` | INT | Sí | 0-18446744073709551615 | Semilla para determinar si el nodo debe re-ejecutarse; los resultados reales son no deterministas independientemente de la semilla (predeterminado: 0) |
| `recraft_style` | STYLEV3 | No | - | Selección opcional de estilo para el fondo generado. Si no se proporciona, se utiliza por defecto el estilo "realistic_image" |
| `negative_prompt` | STRING | No | - | Una descripción textual opcional de elementos no deseados en una imagen (predeterminado: vacío) |

**Nota:** El parámetro `seed` controla cuándo el nodo se re-ejecuta, pero no garantiza resultados deterministas debido a la naturaleza de la API externa.

## Salidas

| Nombre de Salida | Tipo de Dato | Descripción |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | La(s) imagen(es) generada(s) con el fondo reemplazado |

---
**Source fingerprint (SHA-256):** `305cb8c542159a089b1fa03971205b23d50c8a328af006e284fb27011070f6bd`
