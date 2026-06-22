# Recraft Reemplazar Fondo

Reemplazar el fondo de una imagen, basado en el mensaje proporcionado. Este nodo utiliza la API de Recraft para generar nuevos fondos para tus imágenes según tu descripción textual, permitiéndote transformar completamente el fondo mientras mantienes intacto el sujeto principal.

## Entradas

| Parámetro | Descripción | Tipo de Dato | Obligatorio | Rango |
| --- | --- | --- | --- | --- |
| `imagen` | La imagen de entrada a procesar | IMAGE | Sí | - |
| `prompt` | Mensaje para la generación de la imagen (predeterminado: vacío) | STRING | Sí | - |
| `n` | El número de imágenes a generar (predeterminado: 1) | INT | Sí | 1-6 |
| `semilla` | Semilla para determinar si el nodo debe re-ejecutarse; los resultados reales son no deterministas independientemente de la semilla (predeterminado: 0) | INT | Sí | 0-18446744073709551615 |
| `recraft_style` | Selección opcional de estilo para el fondo generado. Si no se proporciona, se utiliza por defecto el estilo "realistic_image" | STYLEV3 | No | - |
| `negative_prompt` | Una descripción textual opcional de elementos no deseados en una imagen (predeterminado: vacío) | STRING | No | - |

**Nota:** El parámetro `seed` controla cuándo el nodo se re-ejecuta, pero no garantiza resultados deterministas debido a la naturaleza de la API externa.

## Salidas

| Nombre de Salida | Descripción | Tipo de Dato |
| --- | --- | --- |
| `IMAGE` | La(s) imagen(es) generada(s) con el fondo reemplazado | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftReplaceBackgroundNode/es.md)

---
**Source fingerprint (SHA-256):** `305cb8c542159a089b1fa03971205b23d50c8a328af006e284fb27011070f6bd`
