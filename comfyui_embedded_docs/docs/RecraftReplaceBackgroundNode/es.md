# Recraft Reemplazar Fondo

Reemplaza el fondo de una imagen según la indicación proporcionada. Este nodo utiliza la API de Recraft para generar nuevos fondos para tus imágenes según tu descripción de texto, lo que te permite transformar completamente el fondo mientras mantienes el sujeto principal intacto.

## Entradas

| Parámetro | Descripción | Tipo de datos | Requerido | Rango |
|-----------|-------------|---------------|-----------|-------|
| `imagen` | La imagen de entrada a procesar | IMAGE | Sí | - |
| `prompt` | Indicación para la generación de la imagen (predeterminado: vacío) | STRING | Sí | - |
| `n` | El número de imágenes a generar (predeterminado: 1) | INT | Sí | 1-6 |
| `semilla` | Semilla para determinar si el nodo debe volver a ejecutarse; los resultados reales son no deterministas independientemente de la semilla (predeterminado: 0) | INT | Sí | 0-18446744073709551615 |
| `recraft_style` | Selección opcional de estilo para el fondo generado. Si no se proporciona, se establece por defecto el estilo "realistic_image" | STYLEV3 | No | - |
| `negative_prompt` | Una descripción de texto opcional de elementos no deseados en una imagen (predeterminado: vacío) | STRING | No | - |

**Nota:** El parámetro `seed` controla cuándo se vuelve a ejecutar el nodo, pero no garantiza resultados deterministas debido a la naturaleza de la API externa.

## Salidas

| Nombre de salida | Descripción | Tipo de datos |
|------------------|-------------|---------------|
| `IMAGE` | Las imágenes generadas con el fondo reemplazado. Para cada imagen de entrada, el número de resultados generados está determinado por `n`. | IMAGE |

> Esta documentación fue generada por IA. Si encuentra algún error o tiene sugerencias de mejora, ¡no dude en contribuir! [Editar en GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftReplaceBackgroundNode/es.md)

---
**Source fingerprint (SHA-256):** `45a2607ae73cc67caa98d33bf536feda83a2021d960dec7cca76cbe0b9fc47ef`
